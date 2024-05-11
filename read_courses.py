# Django specific settings
import inspect
import os

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

# Import necessary modules
from django.db import connection
from django.core.wsgi import get_wsgi_application

# Ensure Django settings are read
application = get_wsgi_application()

# Import models from the CRUD app
from crud.models import *
from datetime import date

# Find all courses
# Query all Course objects from the database
courses = Course.objects.all()
# Print the retrieved Course objects
print(courses)