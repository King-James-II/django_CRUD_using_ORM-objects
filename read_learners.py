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

# Find students with last name "Smith"
# Query all Learner objects where the last name contains "Smith" (case-insensitive)
learners_smith = Learner.objects.filter(last_name__icontains="Smith")
print("1. Find learners with last name `Smith`")
print(learners_smith)
print("\n")

# Order by dob descending, and select the first two objects
# Sort Learner objects by date of birth (dob) in descending order and select the first two objects
learners = Learner.objects.order_by("-dob")[0:2]
print("2. Find top two youngest learners")
print(learners)