# views.py
from datetime import timezone
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authtoken.models import Token
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from django.utils import timezone
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import (
    Utilisateur, DemandeDeCompteVoyageur,
    Annonce, DemandeAnnonce, Tag, AnnonceTag, Palier, AnnoncePalier
)
from .serializers import (
    UserRegistrationSerializer, UtilisateurSerializer, DemandeDeCompteVoyageurSerializer, 
    AnnonceSerializer, DemandeAnnonceSerializer,  PasswordResetRequestSerializer, PasswordResetConfirmSerializer,
    TagSerializer, AnnonceTagSerializer, PalierSerializer, AnnoncePalierSerializer, UserLoginSerializer
)

# Password reset request view
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

class PasswordResetRequestView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = PasswordResetRequestSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            user = Utilisateur.objects.filter(email=email).first()
            if user:
                token = default_token_generator.make_token(user)
                uid = urlsafe_base64_encode(force_bytes(user.pk))
                reset_link = f"{request.scheme}://{settings.SVELTE_APP_URL}/reset_password_confirm/{uid}/{token}/"

                # Render the HTML email template
                html_message = render_to_string('emails/password_reset_email.html', {
                    'user': user,
                    'reset_link': reset_link,
                    'year': timezone.now().year,
                })
                plain_message = strip_tags(html_message)

                send_mail(
                    'Password Reset Request',
                    plain_message,
                    settings.DEFAULT_FROM_EMAIL,  # Ensure this is set in your settings.py
                    [user.email],
                    html_message=html_message,
                    fail_silently=False,
                )
            return Response({"message": "Password reset link has been sent to your email."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Password reset confirm view

class PasswordResetConfirmView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = Utilisateur.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, Utilisateur.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            return Response({"message": "Token is valid."}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Invalid token or user ID."}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, uidb64, token):
        serializer = PasswordResetConfirmSerializer(data=request.data)
        if serializer.is_valid():
            try:
                uid = force_str(urlsafe_base64_decode(uidb64))
                user = Utilisateur.objects.get(pk=uid)
            except (TypeError, ValueError, OverflowError, Utilisateur.DoesNotExist):
                user = None

            if user is not None and default_token_generator.check_token(user, token):
                user.set_password(serializer.validated_data['new_password'])
                user.save()
                return Response({"message": "Password has been reset successfully."}, status=status.HTTP_200_OK)
            else:
                return Response({"message": "Invalid token or user ID."}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# User registration view
class UserRegistrationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.create(user=user)
            return Response({"user": serializer.data, "token": token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# User login view
from django.contrib.auth import authenticate

class UserLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# ViewSet for managing users
class UtilisateurViewSet(viewsets.ModelViewSet):
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Optionally restricts the returned users by filtering against a `username` query parameter in the URL."""
        username = self.request.query_params.get('username', None)
        if username:
            return Utilisateur.objects.filter(username=username)
        return Utilisateur.objects.all()

    def get_object(self):
        """Retrieve and return the authenticated user."""
        return get_object_or_404(Utilisateur, pk=self.request.user.pk)

# ViewSet for managing travel account requests
class DemandeDeCompteVoyageurViewSet(viewsets.ModelViewSet):
    queryset = DemandeDeCompteVoyageur.objects.all()
    serializer_class = DemandeDeCompteVoyageurSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Filter requests by the authenticated user."""
        return DemandeDeCompteVoyageur.objects.filter(utilisateur=self.request.user)
    
    @action(detail=True, methods=['post'])
    def approve(self, request, pk=None):
        """Approve a travel account request."""
        demande = self.get_object()
        demande.est_approuve = True
        demande.save()
        return Response({'status': 'Demande approuvée'}, status=status.HTTP_200_OK)

# ViewSet for managing announcements
class AnnonceViewSet(viewsets.ModelViewSet):
    queryset = Annonce.objects.all()
    serializer_class = AnnonceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Optionally filter announcements by the creator."""
        creator_id = self.request.query_params.get('createur', None)
        if creator_id:
            return Annonce.objects.filter(createur_id=creator_id)
        return Annonce.objects.all()

    def perform_create(self, serializer):
        """Set the creator to the logged-in user."""
        serializer.save(createur=self.request.user)

# ViewSet for managing tags
class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated]

# ViewSet for managing announcement tags
class AnnonceTagViewSet(viewsets.ModelViewSet):
    queryset = AnnonceTag.objects.all()
    serializer_class = AnnonceTagSerializer
    permission_classes = [IsAuthenticated]

# ViewSet for managing tiers
class PalierViewSet(viewsets.ModelViewSet):
    queryset = Palier.objects.all()
    serializer_class = PalierSerializer
    permission_classes = [IsAuthenticated]

# ViewSet for managing announcement tiers
class AnnoncePalierViewSet(viewsets.ModelViewSet):
    queryset = AnnoncePalier.objects.all()
    serializer_class = AnnoncePalierSerializer
    permission_classes = [IsAuthenticated]


import requests
from django.conf import settings
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import DemandeAnnonce
from .serializers import DemandeAnnonceSerializer
from .services import LemonSqueezyService, EmailService
from rest_framework.exceptions import PermissionDenied

class DemandeAnnonceViewSet(viewsets.ModelViewSet):
    queryset = DemandeAnnonce.objects.all()
    serializer_class = DemandeAnnonceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return DemandeAnnonce.objects.filter(utilisateur=self.request.user)

    @action(detail=False, methods=['post'], url_path='confirm_requests')
    def confirm_requests(self, request):
        request_ids = request.data.get('request_ids', [])
        demandes = DemandeAnnonce.objects.filter(id__in=request_ids, statut='en_attente')

        for demande in demandes:
            if demande.annonce.createur != request.user:
                raise PermissionDenied("Vous n'êtes pas autorisé à confirmer cette demande.")

        if not demandes:
            return Response({'status': 'No valid requests found.'}, status=status.HTTP_400_BAD_REQUEST)

        lemon_squeezy = LemonSqueezyService()
        email_service = EmailService()

        for demande in demandes:
            total_price = demande.prix_total 
            payment_link = lemon_squeezy.create_payment_link(demande.utilisateur.email, total_price, demande.id)

            if not payment_link:
                continue  # Log error internally within the service

            demande.statut = 'accepte'
            demande.save()

            email_service.send_confirmation_email(demande.utilisateur, demande.annonce, total_price, payment_link)

        return Response({'status': 'Requests confirmed and emails sent.'}, status=status.HTTP_200_OK)
