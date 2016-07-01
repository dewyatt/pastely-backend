"""
Settings for local development.
"""

from .base import *

SECRET_KEY = '&f*et#1f%_g5f1gej^5ij9)d65-p8c6pj7m8$vgd1_8@969naa'

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
