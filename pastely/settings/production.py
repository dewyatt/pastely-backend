"""
Settings specific to the production environment.
"""

from .base import *
from pastely.utils import get_config_ini

config = get_config_ini(CONFIG_INI_PATH)

DEBUG = False

SECRET_KEY = config['SECRET_KEY']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config['DATABASE_NAME'],
        'USER': config['DATABASE_USER'],
        'PASSWORD': config['DATABASE_PASSWORD'],
        'HOST': config['DATABASE_HOST'],
        'PORT': config['DATABASE_PORT'],
    }
}
