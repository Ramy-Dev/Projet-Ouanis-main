import email
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import Utilisateur, Annonce, DemandeAnnonce, DemandeDeCompteVoyageur, Tag, AnnonceTag, Palier, AnnoncePalier

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, min_length=8)
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Utilisateur
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')

    def validate_email(self, value):
        if Utilisateur.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email is already in use.")
        return value

    def validate_username(self, value):
        if Utilisateur.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username is already in use.")
        return value

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        if not any(char.isdigit() for char in attrs['password']):
            raise serializers.ValidationError({"password": "Password must contain at least one digit."})
        if not any(char.isalpha() for char in attrs['password']):
            raise serializers.ValidationError({"password": "Password must contain at least one letter."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        user = Utilisateur.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(username=email, password=password)  # Use username=email here for email-based authentication
            if not user:
                raise serializers.ValidationError("Invalid credentials.")
        else:
            raise serializers.ValidationError("Both email and password are required.")
        
        attrs['user'] = user
        return attrs
class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = [
            'id', 'username', 'password', 'first_name', 'last_name', 'email', 'numero_telephone', 
            'adresse', 'date_de_naissance', 'profile_picture', 'numero_passeport', 'photos_passeport', 'is_voyageur'
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def validate_email(self, value):
        if self.instance and self.instance.email != value and Utilisateur.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email is already in use.")
        return value

    def validate_username(self, value):
        if self.instance and self.instance.username != value and Utilisateur.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username is already in use.")
        return value

    def validate_numero_telephone(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("Phone number must contain only digits.")
        if not (9 <= len(value) <= 15):
            raise serializers.ValidationError("Phone number must be between 9 and 15 digits.")
        return value

    def create(self, validated_data):
        user = Utilisateur.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        if password:
            instance.set_password(password)
        return super().update(instance, validated_data)

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

    def validate_nom(self, value):
        if not value:
            raise serializers.ValidationError("Tag name cannot be empty.")
        return value

class PalierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Palier
        fields = ['id', 'min', 'max', 'price']

    def validate(self, data):
        if data['from_poids'] >= data['to_poids']:
            raise serializers.ValidationError("from_poids must be less than to_poids.")
        return data

class AnnonceTagSerializer(serializers.ModelSerializer):
    tag = TagSerializer()

    class Meta:
        model = AnnonceTag
        fields = ['id', 'tag']

class AnnoncePalierSerializer(serializers.ModelSerializer):
    palier = PalierSerializer()

    class Meta:
        model = AnnoncePalier
        fields = ['id', 'palier']

class AnnonceSerializer(serializers.ModelSerializer):
    createur = serializers.PrimaryKeyRelatedField(queryset=Utilisateur.objects.all())
    tags = serializers.PrimaryKeyRelatedField(many=True, queryset=Tag.objects.all(), write_only=True)
    paliers = AnnoncePalierSerializer(many=True, write_only=True)

    class Meta:
        model = Annonce
        fields = [
            'id', 'createur', 'created_at', 'updated_at', 'lieu_depart', 
            'destination', 'poids_max', 'volume_max', 'date_heure_depart', 'date_heure_arrivee', 'tags', 'paliers'
        ]

    def validate_date_heure_depart(self, value):
        if value < timezone.now():
            raise serializers.ValidationError("Departure date and time must be in the future.")
        return value

    def validate(self, data):
        if data['date_heure_depart'] >= data['date_heure_arrivee']:
            raise serializers.ValidationError("Departure date and time must be before arrival date and time.")
        return data

    def create(self, validated_data):
        tags_data = validated_data.pop('tags')
        paliers_data = validated_data.pop('paliers')
        annonce = Annonce.objects.create(**validated_data)

        for tag in tags_data:
            AnnonceTag.objects.create(annonce=annonce, tag=tag)

        for palier_data in paliers_data:
            palier = Palier.objects.create(**palier_data)
            AnnoncePalier.objects.create(annonce=annonce, palier=palier)

        return annonce
    
    def update(self, instance, validated_data):
        tags_data = validated_data.pop('tags', None)
        paliers_data = validated_data.pop('paliers', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        if tags_data:
            instance.annonce_tags.all().delete()
            for tag in tags_data:
                AnnonceTag.objects.create(annonce=instance, tag=tag)

        if paliers_data:
            instance.annonce_paliers.all().delete()
            for palier_data in paliers_data:
                palier = Palier.objects.create(**palier_data)
                AnnoncePalier.objects.create(annonce=instance, palier=palier)

        instance.save()
        return instance

class DemandeAnnonceSerializer(serializers.ModelSerializer):
    utilisateur = serializers.PrimaryKeyRelatedField(queryset=Utilisateur.objects.all())
    annonce = serializers.PrimaryKeyRelatedField(queryset=Annonce.objects.all())

    class Meta:
        model = DemandeAnnonce
        fields = ['id', 'utilisateur', 'annonce', 'statut', 'date_creation', 'poids', 'volume']

    def validate_poids(self, value):
        if value and value <= 0:
            raise serializers.ValidationError("Weight must be a positive number.")
        return value

    def validate_volume(self, value):
        if value and value <= 0:
            raise serializers.ValidationError("Volume must be a positive number.")
        return value

    def create(self, validated_data):
        return DemandeAnnonce.objects.create(**validated_data)

class DemandeDeCompteVoyageurSerializer(serializers.ModelSerializer):
    utilisateur = UtilisateurSerializer()

    class Meta:
        model = DemandeDeCompteVoyageur
        fields = [
            'id', 'utilisateur', 'date_de_creation', 'numero_passeport', 
            'photos_passeport', 'adresse', 'est_approuve'
        ]

    def validate_numero_passeport(self, value):
        if not value.isalnum():
            raise serializers.ValidationError("Passport number must contain only alphanumeric characters.")
        return value

    def create(self, validated_data):
        utilisateur_data = validated_data.pop('utilisateur')
        utilisateur = Utilisateur.objects.create(**utilisateur_data)
        demande = DemandeDeCompteVoyageur.objects.create(utilisateur=utilisateur, **validated_data)
        return demande

    def update(self, instance, validated_data):
        utilisateur_data = validated_data.pop('utilisateur', None)
        if utilisateur_data:
            UtilisateurSerializer().update(instance.utilisateur, utilisateur_data)
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        instance.save()
        return instance

class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        if not Utilisateur.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email address not found.")
        return value

class PasswordResetConfirmSerializer(serializers.Serializer):
    new_password = serializers.CharField(write_only=True, min_length=8)
    confirm_password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        if attrs['new_password'] != attrs['confirm_password']:
            raise serializers.ValidationError("Passwords do not match.")
        if not any(char.isdigit() for char in attrs['new_password']):
            raise serializers.ValidationError({"new_password": "Password must contain at least one digit."})
        if not any(char.isalpha() for char in attrs['new_password']):
            raise serializers.ValidationError({"new_password": "Password must contain at least one letter."})
        return attrs
