"""
WSGI config for learning_users project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""
#
# import os
#
# from django.core.wsgi import get_wsgi_application
#
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learning_users.settings")
#
# application = get_wsgi_application()
import os
import sys

# # add your project directory to the sys.path
project_home = u'/home/lemayr1/Plaga/learning_users/'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# set environment variable to tell django where your settings.py is
os.environ['DJANGO_SETTINGS_MODULE'] = 'learning_users/learning_users.settings'


# serve django via WSGI
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
