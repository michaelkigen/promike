"""
WSGI config for pro project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
import sys
print("THIS ID THE WSGI FILE THAT GIVE SOME ERROR")
print("THE PATH",sys.path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pro.settings')

application = get_wsgi_application()
  