"""
WSGI config for projectmushrooms project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projectmushrooms.settings')

application = WhiteNoise(application, root='/static/assets/img/')
application.add_files('/static/assets/img/', prefix='more-files/')

application = get_wsgi_application()
