"""
WSGI config for backend project.

It exposes the WSGI callable as a module-level variable named ``application``.
"""

import os
from dotenv import load_dotenv
from django.core.wsgi import get_wsgi_application

load_dotenv()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

application = get_wsgi_application()
