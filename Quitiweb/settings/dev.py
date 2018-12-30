"""Development settings and globals"""

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE += [
    # ...
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    # ...
]

ALLOWED_HOSTS += [
    '127.0.0.1',
    'localhost',
]

# For test pourposes
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# To send emails using SMTP
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'sub5.mail.dreamhost.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'info@quitiweb.com'
EMAIL_HOST_PASSWORD = 'Bernardito84'
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True