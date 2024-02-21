from django.contrib import admin
from .models import Users

# Register your models here.

# by doing this database will have 'website_users' table
# that table contains all the fields we created inside 'Users' models

admin.site.register(Users)
