"""
WSGI config for owners_parcels project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os, sys

from django.core.wsgi import get_wsgi_application
from django.conf import settings

sys.path.append('/home/admin/owners_parcels/src/')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "owners_parcels.settings")

# prevenimos UnicodeEncodeError
os.environ.setdefault('LANG', 'en_US.UTF-8')
os.environ.setdefault('LC_ALL', 'en_US.UTF-8')

if settings.DEBUG == False:
    # activamos nuestro virtualenv
    activate_this = '/home/admin/owners_parcels/bin/activate_this.py'
    execfile(activate_this, dict(__file__=activate_this))

application = get_wsgi_application()
