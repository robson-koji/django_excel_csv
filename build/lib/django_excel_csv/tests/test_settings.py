import os

SETTINGS_PATH = os.path.dirname(os.path.dirname(__file__))


SECRET_KEY = 'fake-key'
INSTALLED_APPS = [
    "django_excel_csv",
]

DATABASES={
    "default": {
        "ENGINE": "django.db.backends.dummy",
    }
}

TEMPLATE_DIRS = (
    os.path.join(SETTINGS_PATH, 'templates'),
)
