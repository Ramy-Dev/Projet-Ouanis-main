
from pathlib import Path
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-)8cscfad@kn=-=@l7ujd+qv=0=&x#uez@dbinw@w4!qg2+d(dj'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Email settings

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.office365.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
# settings.py
DEFAULT_FROM_EMAIL = 'imansoura.ramy@outlook.com'

INSTALLED_APPS = [
    'jazzmin',
    'admin_interface',
    'colorfield',
    'ouanis',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
]

X_FRAME_OPTIONS = 'SAMEORIGIN'
SILENCED_SYSTEM_CHECKS = ['security.W019']

# Customization for django-admin-interface
ADMIN_INTERFACE_THEME = {
    'css': {
        'header': 'bg-lightblue-500',
        'title': 'font-bold text-white',
        'user_info': 'text-gray-200',
        'sidebar': 'bg-gray-900 text-white',
        'sidebar_active': 'bg-lightblue-500 text-white',
        'footer': 'text-gray-200',
    }
}
# Define the Svelte app URL
SVELTE_APP_URL = 'localhost:5173'

JAZZMIN_SETTINGS = {
    "site_title": "En voyage",
    "site_header": "En voyage",
    "site_brand": "Admin En voyage",
    "welcome_sign": "Welcome to My Admin",
    "copyright": "EN voyage RAMY / AMINE",
    "user_avatar": "profile_picture",
    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs"},
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "ouanis.utilisateur": "fas fa-user-circle",
        "ouanis.annonce": "fas fa-bullhorn",
        "ouanis.demandeannonce": "fas fa-hand-paper",
        "ouanis.demandedecomptevoyageur": "fas fa-passport",
        "ouanis.tag": "fas fa-tag",
        "ouanis.annoncetag": "fas fa-tags",
        "ouanis.palier": "fas fa-weight",
        "ouanis.annoncepalier": "fas fa-balance-scale",
    },
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",
    "topmenu_links": [
        {"name": "AR Panel", "permissions": ["auth.view_user"]},
        {"app": "auth"},
    ],
    "usermenu_links": [
        {"name": "Support", "url": "", "new_window": True},
    ],
    "show_sidebar": True,
    "order_with_respect_to": ["auth", "ouanis", "settings"],
    "custom_links": {
        "ouanis": [
            {"name": "Dashboard", "url": "admin:dashboard", "icon": "fas fa-tachometer-alt", "permissions": ["ouanis.view_utilisateur"]},
           # {"name": "User Reports", "url": "/admin/reports/users/", "icon": "fas fa-chart-line", "permissions": ["ouanis.view_utilisateur"]},
        ]
    },
    "related_modal_active": True,  # Utiliser des modals pour les champs liés
    "theme": {
        "navbar": {
            "background_color": "#2c3e50",
            "text_color": "white",
            "hover_background_color": "#1abc9c",
            "hover_text_color": "lightgrey",
        },
        "sidebar": {
            "background_color": "#34495e",
            "text_color": "white",
            "hover_background_color": "#1abc9c",
            "hover_text_color": "lightgrey",
        },
        "footer": {
            "background_color": "#2c3e50",
            "text_color": "white",
        },
        "buttons": {
            "default": "btn-primary",
            "primary": "btn-primary",
            "success": "btn-success",
            "info": "btn-info",
            "warning": "btn-warning",
            "danger": "btn-danger",
        },

    },
        "custom_css": "css/custom_admin.css",  # Add this line

}
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'ouanis.backends.EmailBackend',
]


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
}

AUTH_USER_MODEL = 'ouanis.Utilisateur'

# settings.py

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",  # Add your frontend's origin
    "http://127.0.0.1:5173",  # Add this if you're using another localhost port
]

# settings.py

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # Doit être avant AuthenticationMiddleware
    'django.middleware.common.CommonMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Doit être présent
    'django.contrib.messages.middleware.MessageMiddleware',  # Doit être présent
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Ensure this points to the correct path
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


WSGI_APPLICATION = 'mysite.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True
import os

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]



LEMON_SQUEEZY_API_KEY = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI5NGQ1OWNlZi1kYmI4LTRlYTUtYjE3OC1kMjU0MGZjZDY5MTkiLCJqdGkiOiIyZjBmMmYwZjc2YmFiZmYxZWQ5Y2VjMDllMWNkOWU1ZWE3ZTU5YTJhODVjNGVkYmRhOTZlNTg3NTM1NmE2NWU3ZDkxZDU4NmQwYTUzNzAzMyIsImlhdCI6MTcxODMyNjQ3Ni4zMzY5OCwibmJmIjoxNzE4MzI2NDc2LjMzNjk4MiwiZXhwIjoyMDMzODU5Mjc2LjMyMjU2Mywic3ViIjoiMjU0MjY0MSIsInNjb3BlcyI6W119.LBZD9Z1NQyXp3z07LZqmGaqN6yHR72f7s-wnHKgv4irX89cVdOvoDw8wddQ9Ffma50adm0L7xNjizVOcfJYu0gA3CSwQS5cLAIXZaLeO0Ed4gybpHf8leqZBrkyOTjLT49JN6XJhFcaldd5-3QDPH8gOipo3nkOE_WRtd3DSyiMo4lETGdb4hrUzZR0-MRCqtXgVwAovZryDXJ4DJiaJ_d8e0-M-NqLfgK_aVndH8DHAkiON_m-iMCRJ0OeJjdKmQMqwXM63_SAPe2D-vZTmcGETNS6ddQJV_G3UnTYAD4LP5OvuimR26TMgbSE0EfPcjJ1mtsYJSJDrropWD77gkuGCPTSufmdQLldoV4QBX5x-iMX8yBjMOyy6MGw5owaoT-oba7yPHgXVISuEI7Erigc-aph1cEIdY_74kTXIF9ycYF_NCeNjppuACHYWn3j34lUB7uk_aWZ5KxOwQ-5rHdWMLJHE0w9sPquZKwhQNR-8DNJxCKipFU_WcQcVog6C'
