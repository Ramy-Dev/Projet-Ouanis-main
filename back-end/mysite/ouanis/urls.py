#urls.py 
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token
from .views import (
    UtilisateurViewSet, DemandeDeCompteVoyageurViewSet, 
    AnnonceViewSet, DemandeAnnonceViewSet, TagViewSet, UserRegistrationView, UserLoginView,
    AnnonceTagViewSet, PalierViewSet, AnnoncePalierViewSet, PasswordResetRequestView, PasswordResetConfirmView
    )

router = DefaultRouter()
router.register(r'utilisateurs', UtilisateurViewSet)
router.register(r'demandes_compte_voyageur', DemandeDeCompteVoyageurViewSet)
router.register(r'annonces', AnnonceViewSet)
router.register(r'demandes_annonce', DemandeAnnonceViewSet)
router.register(r'tags', TagViewSet)
router.register(r'annonce_tags', AnnonceTagViewSet)
router.register(r'paliers', PalierViewSet)
router.register(r'annonce_paliers', AnnoncePalierViewSet)

urlpatterns = [
    # In your urls.py (add this view to the admin urls)
    path('reset_password/', PasswordResetRequestView.as_view(), name='reset_password'),
    path('reset_password_confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='reset_password_confirm'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('', include(router.urls)),
]
