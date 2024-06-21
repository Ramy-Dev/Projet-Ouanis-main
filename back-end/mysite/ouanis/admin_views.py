from django.contrib.auth.admin import UserAdmin, admin_site
from django.contrib.auth.models import Group
from django.utils.html import format_html
from .models import (
    Utilisateur, Annonce, DemandeAnnonce, DemandeDeCompteVoyageur, 
    Tag, AnnonceTag, Palier, AnnoncePalier
)

# Unregister the Group model from the admin site
admin_site.unregister(Group)

class UtilisateurAdmin(UserAdmin):
    model = Utilisateur
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_voyageur', 'date_de_naissance', 'date_joined', 'last_login', 'profile_picture_tag', 'status_indicator', 'photos_passeport_tag')
    list_filter = ('is_voyageur', 'date_de_naissance', 'date_joined', 'last_login')
    search_fields = ('username', 'email', 'first_name', 'last_name', 'numero_telephone')
    ordering = ('username',)
    readonly_fields = ('date_joined', 'last_login', 'profile_picture_tag', 'photos_passeport_tag')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'date_de_naissance', 'numero_telephone', 'profile_picture', 'photos_passeport')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('date_joined', 'last_login')}),
    )

    def profile_picture_tag(self, obj):
        if obj.profile_picture:
            return format_html('<img src="{}" width="50" height="50" class="zoomable" />'.format(obj.profile_picture.url))
        return "-"
    profile_picture_tag.short_description = 'Profile Picture'

    def photos_passeport_tag(self, obj):
        if obj.photos_passeport:
            return format_html('<img src="{}" width="150" height="80" class="zoomable" />'.format(obj.photos_passeport.url))
        return "-"
    photos_passeport_tag.short_description = 'Passport Image'

    def status_indicator(self, obj):
        color = 'green' if obj.is_active else 'red'
        return format_html('<span style="color: {};">{}</span>', color, 'Active' if obj.is_active else 'Inactive')
    status_indicator.short_description = 'Status'

    class Media:
        js = ('js/zoom_image.js',)

class AnnonceTagInline(admin.TabularInline):
    model = AnnonceTag
    extra = 1

class AnnoncePalierInline(admin.TabularInline):
    model = AnnoncePalier
    extra = 1

class AnnonceAdmin(admin.ModelAdmin):
    list_display = ('createur', 'lieu_depart', 'destination', 'poids_max', 'volume_max', 'date_heure_depart', 'date_heure_arrivee', 'created_at', 'updated_at')
    list_filter = ('createur', 'lieu_depart', 'destination', 'date_heure_depart', 'date_heure_arrivee')
    search_fields = ('createur__username', 'lieu_depart', 'destination')
    ordering = ('-created_at',)
    inlines = [AnnonceTagInline, AnnoncePalierInline]
    actions = ['mark_as_completed']

    def mark_as_completed(self, request, queryset):
        queryset.update(statut='completed')
    mark_as_completed.short_description = "Mark selected annonces as completed"

class DemandeAnnonceAdmin(admin.ModelAdmin):
    list_display = ('utilisateur', 'annonce', 'statut', 'date_creation', 'poids', 'volume')
    list_filter = ('statut', 'date_creation')
    search_fields = ('utilisateur__username', 'annonce__lieu_depart', 'annonce__destination')
    ordering = ('-date_creation',)
    actions = ['approve_demand']
    
    def approve_demand(self, request, queryset):
        queryset.update(statut='approved')
    approve_demand.short_description = "Approve selected demands"

class DemandeDeCompteVoyageurAdmin(admin.ModelAdmin):
    list_display = ('utilisateur_full_name', 'date_de_creation', 'numero_passeport', 'est_approuve', 'photos_passeport_tag')
    list_filter = ('est_approuve', 'date_de_creation')
    search_fields = ('utilisateur__username', 'numero_passeport')
    ordering = ('-date_de_creation',)
    actions = ['approve_account']
    list_editable = ('est_approuve',)

    def utilisateur_full_name(self, obj):
        return f"{obj.utilisateur.first_name} {obj.utilisateur.last_name}"
    utilisateur_full_name.short_description = 'Utilisateur'

    def approve_account(self, request, queryset):
        for demande in queryset:
            demande.est_approuve = True
            demande.utilisateur.is_voyageur = True
            demande.utilisateur.save()
            demande.save()
    approve_account.short_description = "Approve selected accounts"

    def save_model(self, request, obj, form, change):
        if obj.est_approuve:
            obj.utilisateur.is_voyageur = True
        else:
            obj.utilisateur.is_voyageur = False
        obj.utilisateur.save()
        super().save_model(request, obj, form, change)

    def photos_passeport_tag(self, obj):
        if obj.photos_passeport:
            return format_html('<img src="{}" width="150" height="80" class="zoomable" />'.format(obj.photos_passeport.url))
        return "-"
    photos_passeport_tag.short_description = 'Passport Image'

    class Media:
        js = ('js/zoom_image.js',)

class TagAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ('nom',)

class AnnonceTagAdmin(admin.ModelAdmin):
    list_display = ('annonce', 'tag')
    list_filter = ('annonce', 'tag')
    search_fields = ('annonce__lieu_depart', 'tag__nom')

class PalierAdmin(admin.ModelAdmin):
    list_display = ('from_poids', 'to_poids', 'prix')
    list_filter = ('from_poids', 'to_poids')
    search_fields = ('prix',)

class AnnoncePalierAdmin(admin.ModelAdmin):
    list_display = ('annonce', 'palier')
    list_filter = ('annonce', 'palier')
    search_fields = ('annonce__lieu_depart', 'palier__prix')

admin.site.register(Utilisateur, UtilisateurAdmin)
admin.site.register(Annonce, AnnonceAdmin)
admin.site.register(DemandeAnnonce, DemandeAnnonceAdmin)
admin.site.register(DemandeDeCompteVoyageur, DemandeDeCompteVoyageurAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(AnnonceTag, AnnonceTagAdmin)
admin.site.register(Palier, PalierAdmin)
admin.site.register(AnnoncePalier, AnnoncePalierAdmin)
