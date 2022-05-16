"""
    Development settings and globals
"""

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key should only be used for development and testing.
SECRET_KEY = '508pc(^8(lpv^@thcl!-1=@9_5r9idi4%-%nl&=qv@3%4@maea'

ALLOWED_HOSTS += [
    '127.0.0.1',
    'localhost',
]

# To send emails using SMTP
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.dreamhost.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'info@quitiweb.com'
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True
