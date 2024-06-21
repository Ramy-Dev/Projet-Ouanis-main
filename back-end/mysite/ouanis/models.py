# models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator, MinValueValidator
from django.core.exceptions import ValidationError

# User model with additional fields
class Utilisateur(AbstractUser):
    email = models.EmailField(unique=True)
    numero_telephone = models.CharField(
        max_length=200, 
        blank=True, 
        null=True, 
        validators=[RegexValidator(r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")]
    )
    adresse = models.CharField(max_length=200, blank=True, null=True)
    date_de_naissance = models.DateField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    numero_passeport = models.CharField(max_length=200, blank=True, null=True)
    photos_passeport = models.ImageField(upload_to='passport_images/', blank=True, null=True)
    is_voyageur = models.BooleanField(default=False)
    total_money = models.FloatField(default=0.0, validators=[MinValueValidator(0.0)])

    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def clean(self):
        super().clean()
        if self.date_de_naissance and self.date_de_naissance > timezone.now().date():
            raise ValidationError("Date of birth cannot be in the future.")

class Annonce(models.Model):
    createur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='annonces')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    lieu_depart = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    poids_max = models.FloatField(validators=[MinValueValidator(0.1)])
    volume_max = models.IntegerField(validators=[MinValueValidator(1)])
    date_heure_depart = models.DateTimeField(default=timezone.now)
    date_heure_arrivee = models.DateTimeField(default=timezone.now)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Annonce de {self.createur.first_name} {self.createur.last_name} vers {self.destination}"

    def clean(self):
        super().clean()
        if self.date_heure_depart >= self.date_heure_arrivee:
            raise ValidationError("Departure date and time must be before arrival date and time.")

class DemandeAnnonce(models.Model):
    STATUT_CHOICES = [
        ('en_attente', 'En Attente'),
        ('accepte', 'Accepté'),
        ('rejete', 'Rejeté')
    ]
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='demandes_annonce')
    annonce = models.ForeignKey(Annonce, on_delete=models.CASCADE, related_name='demandes')
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='en_attente')
    date_creation = models.DateTimeField(auto_now_add=True)
    poids = models.FloatField(blank=True, null=True, validators=[MinValueValidator(0.1)])
    volume = models.FloatField(blank=True, null=True, validators=[MinValueValidator(0.1)])
    prix_total = models.FloatField(blank=True, null=True, validators=[MinValueValidator(0.0)])

    def __str__(self):
        return f"Demande de {self.utilisateur.first_name} {self.utilisateur.last_name} pour {self.annonce}"

    def clean(self):
        super().clean()
        if self.poids and self.poids < 0:
            raise ValidationError("Weight must be positive.")
        if self.volume and self.volume < 0:
            raise ValidationError("Volume must be positive.")
        
class DemandeDeCompteVoyageur(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='demandes_compte_voyageur')
    date_de_creation = models.DateTimeField(auto_now_add=True)
    numero_passeport = models.CharField(max_length=200, blank=True, null=True)
    photos_passeport = models.FileField(upload_to='documents/', blank=True, null=True)
    adresse = models.CharField(max_length=200, blank=True, null=True)
    est_approuve = models.BooleanField(default=False)

    def __str__(self):
        return f"Demande de {self.utilisateur.first_name} {self.utilisateur.last_name}"

class Tag(models.Model):
    nom = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.nom

class AnnonceTag(models.Model):
    annonce = models.ForeignKey(Annonce, on_delete=models.CASCADE, related_name='annonce_tags')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='tag_annonces')

    def __str__(self):
        return f"{self.annonce} {self.tag}"

class Palier(models.Model):
    min = models.FloatField(blank=True, null=True, validators=[MinValueValidator(0.0)])
    max = models.FloatField(blank=True, null=True, validators=[MinValueValidator(0.1)])
    price = models.FloatField(blank=True, null=True, validators=[MinValueValidator(0.0)])

    def __str__(self):
        return f"Palier from {self.from_poids} to {self.to_poids} priced at {self.prix}"

    def clean(self):
        super().clean()
        if self.from_poids and self.to_poids and self.from_poids >= self.to_poids:
            raise ValidationError("from_poids must be less than to_poids.")

class AnnoncePalier(models.Model):
    annonce = models.ForeignKey(Annonce, on_delete=models.CASCADE, related_name='annonce_paliers')
    palier = models.ForeignKey(Palier, on_delete=models.CASCADE, related_name='palier_annonces')

    def __str__(self):
        return f"{self.annonce} {self.palier}"
