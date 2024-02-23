from django.contrib.auth.models import User
from django.db import models

# # Create your models here.

# Note : User class is already there in "auth_models" which has all authentication features

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    bio = models.TextField(blank=True,max_length=100)
    profile_picture = models.ImageField(upload_to='profile_pics/', default='dummy.png' ,blank=True, null=True) # must install : pip3 install Pillow

    # helps to see the username in the admin pannel insted of object 1 or object2
    def __str__(self):
        return self.user.username 

class Post(models.Model):
    # 'id' primary key will get generated automatically
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # because we have a ForeignKey field named 'user', 
    # Django will create a column named 'user_id' in database table.
    
    def __str__(self):
        return f"Post by {self.user.username}"
    
class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    liked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Like by {self.user.username} on {self.post}"
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    commented_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Comment by {self.user.username} on {self.post}"