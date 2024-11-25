from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

# Desactiva validadores de contraseña en pruebas
AUTH_PASSWORD_VALIDATORS = []
