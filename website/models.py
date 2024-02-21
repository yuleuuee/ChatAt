from django.db import models
# from django.contrib.auth.hashers import make_password

# Create your models here.

class Users(models.Model):  
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name =  models.CharField(max_length=50,null=True)
    username =  models.CharField(max_length=50)
    password = models.CharField(max_length=128)
    email =  models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True) # must install : pip3 install Pillow


    # Add last_login field
    last_login = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return self.username  # if only 'User' is used to get data then it will only display the username 