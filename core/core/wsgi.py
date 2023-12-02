"""
WSGI config for core project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
from core.settings import base

from django.core.wsgi import get_wsgi_application

if base.DEBUG:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.local")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.production")

application = get_wsgi_application()
app=application
