from .base import *

INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE.insert(0, 'debug_toolbar.middleware.DebugToolbarMiddleware')

# Email
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
