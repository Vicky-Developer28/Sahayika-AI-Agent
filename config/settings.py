"""
Sahayika Django Settings
========================

A Gemini-powered multilingual voice guide
for government services in India.
"""

import os
from pathlib import Path

from dotenv import load_dotenv


# =============================================================================
# BASE DIRECTORY
# =============================================================================

BASE_DIR = Path(__file__).resolve().parent.parent


# =============================================================================
# ENVIRONMENT VARIABLES
# =============================================================================

load_dotenv(BASE_DIR / ".env")


# =============================================================================
# SECURITY
# =============================================================================

SECRET_KEY = os.environ.get(
    "SECRET_KEY",
    "django-insecure-sahayika-hackathon-dev-key-change-in-production",
)

DEBUG = os.environ.get(
    "DEBUG",
    "True",
).lower() == "true"

ALLOWED_HOSTS = ["*"]


# =============================================================================
# APPLICATIONS
# =============================================================================

INSTALLED_APPS = [
    # -------------------------------------------------------------------------
    # Django
    # -------------------------------------------------------------------------
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.staticfiles",

    # -------------------------------------------------------------------------
    # Sahayika
    # -------------------------------------------------------------------------
    "apps.core",
]


# =============================================================================
# MIDDLEWARE
# =============================================================================

MIDDLEWARE = [
    # Security
    "django.middleware.security.SecurityMiddleware",

    # Sessions
    "django.contrib.sessions.middleware.SessionMiddleware",

    # Internationalization
    #
    # IMPORTANT:
    # LocaleMiddleware must come after SessionMiddleware
    # and before CommonMiddleware.
    #
    "django.middleware.locale.LocaleMiddleware",

    # Common
    "django.middleware.common.CommonMiddleware",

    # CSRF
    "django.middleware.csrf.CsrfViewMiddleware",

    # Clickjacking protection
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# =============================================================================
# URL CONFIGURATION
# =============================================================================

ROOT_URLCONF = "config.urls"


# =============================================================================
# TEMPLATES
# =============================================================================

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",

        "DIRS": [
            BASE_DIR / "templates",
        ],

        "APP_DIRS": True,

        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
            ],
        },
    },
]


# =============================================================================
# WSGI / ASGI
# =============================================================================

WSGI_APPLICATION = "config.wsgi.application"
ASGI_APPLICATION = "config.asgi.application"


# =============================================================================
# DATABASE
# =============================================================================
#
# Sahayika currently uses file-based Django sessions and does not require
# a database for the MVP.
#
# DATABASES = {}
#
# If you later add users, analytics, persistent conversations, etc.,
# this can be changed to SQLite/PostgreSQL.
#
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# =============================================================================
# SESSION CONFIGURATION
# =============================================================================

# Store sessions as files instead of using a database.
SESSION_ENGINE = (
    "django.contrib.sessions.backends.file"
)

# Directory where session files will be stored.
SESSION_FILE_PATH = BASE_DIR / "session_data"

# Create the directory automatically.
SESSION_FILE_PATH.mkdir(
    parents=True,
    exist_ok=True,
)

# Session lifetime: 1 hour.
SESSION_COOKIE_AGE = 60 * 60

# Save session only when modified.
SESSION_SAVE_EVERY_REQUEST = False

# Keep session after browser restart.
SESSION_EXPIRE_AT_BROWSER_CLOSE = False


# =============================================================================
# INTERNATIONALIZATION
# =============================================================================

# -------------------------------------------------------------------------
# DEFAULT LANGUAGE
# -------------------------------------------------------------------------
#
# English is the default UI language.
#
# This MUST match one of the language codes inside LANGUAGES.
#

LANGUAGE_CODE = "en"


# -------------------------------------------------------------------------
# SUPPORTED LANGUAGES
# -------------------------------------------------------------------------
#
# English + 22 languages from the Eighth Schedule.
#

LANGUAGES = [
    # ---------------------------------------------------------------------
    # English
    # ---------------------------------------------------------------------
    ("en", "English"),

    # ---------------------------------------------------------------------
    # Indian Languages
    # ---------------------------------------------------------------------

    # Assamese
    ("as", "অসমীয়া"),

    # Bengali
    ("bn", "বাংলা"),

    # Bodo
    ("brx", "बड़ो"),

    # Dogri
    ("doi", "डोगरी"),

    # Gujarati
    ("gu", "ગુજરાતી"),

    # Hindi
    ("hi", "हिन्दी"),

    # Kannada
    ("kn", "ಕನ್ನಡ"),

    # Kashmiri
    ("ks", "کٲشُر"),

    # Konkani
    ("kok", "कोंकणी"),

    # Maithili
    ("mai", "मैथिली"),

    # Malayalam
    ("ml", "മലയാളം"),

    # Manipuri
    ("mni", "মৈতৈলোন্"),

    # Marathi
    ("mr", "मराठी"),

    # Nepali
    ("ne", "नेपाली"),

    # Odia
    ("or", "ଓଡ଼ିଆ"),

    # Punjabi
    ("pa", "ਪੰਜਾਬੀ"),

    # Sanskrit
    ("sa", "संस्कृतम्"),

    # Santali
    ("sat", "ᱥᱟᱱᱛᱟᱲᱤ"),

    # Sindhi
    ("sd", "سنڌي"),

    # Tamil
    ("ta", "தமிழ்"),

    # Telugu
    ("te", "తెలుగు"),

    # Urdu
    ("ur", "اردو"),
]


# -------------------------------------------------------------------------
# TRANSLATION FILES
# -------------------------------------------------------------------------

LOCALE_PATHS = [
    BASE_DIR / "locale",
]


# -------------------------------------------------------------------------
# TIME ZONE
# -------------------------------------------------------------------------

TIME_ZONE = "Asia/Kolkata"


# -------------------------------------------------------------------------
# ENABLE INTERNATIONALIZATION
# -------------------------------------------------------------------------

USE_I18N = True


# -------------------------------------------------------------------------
# ENABLE TIMEZONE SUPPORT
# -------------------------------------------------------------------------

USE_TZ = True


# =============================================================================
# STATIC FILES
# =============================================================================

STATIC_URL = "/static/"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]


# =============================================================================
# DEFAULT PRIMARY KEY
# =============================================================================

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# =============================================================================
# GEMINI CONFIGURATION
# =============================================================================

GEMINI_API_KEY = os.environ.get(
    "GEMINI_API_KEY",
    "",
)


# =============================================================================
# SAHAYIKA CONFIGURATION
# =============================================================================

# Default AI language.
#
# This is separate from Django's LANGUAGE_CODE.
#
# LANGUAGE_CODE:
#     Controls the Django interface.
#
# SAHAYIKA_LANGUAGE:
#     Fallback language for Gemini conversations.
#

SAHAYIKA_LANGUAGE = "en"


# Maximum number of conversation messages stored in the session.
#
# 20 messages ≈ 10 user/model exchanges.
#

SAHAYIKA_MAX_HISTORY = 20


# Main government scheme/resource for the MVP.
#

SAHAYIKA_SCHEME = "PM Ujjwala Yojana"
