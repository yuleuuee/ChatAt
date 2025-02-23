from django.contrib.auth.models import User
from django.db import models

# # Create your models here.

# Note : User class is already there in "auth_models" which has all authentication features

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # OneToOneField :  1 user can only have 1 UserProfile
    phone = models.CharField(max_length=15)
    bio = models.TextField(blank=True,max_length=100)
    profile_picture = models.ImageField(upload_to='profile_pics/', default='dummy.png') # must install : pip3 install Pillow

    # New field to track active status
    is_online = models.BooleanField(default=False)
    dark_mode = models.BooleanField(default=False)

    # helps to see the username in the admin pannel insted of object 1 or object2
    def __str__(self):
        return self.user.username 

class Post(models.Model):
    # 'id' primary key will get generated automatically
    user = models.ForeignKey(User, on_delete=models.CASCADE) #ForeignKey:  Allows a many-to-one relationship , 1 user can have N post
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    caption = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True) # auto_now_add=True: Sets the field to the current date and time only when the object is first created.  # default=datetime.now(): Sets the field to the current date and time both when creating and updating the object.
    no_of_likes =models.IntegerField(default=0)
    no_of_comments =models.IntegerField(default=0)
    # because we have a ForeignKey field named 'user', # Django will create a column named 'user_id' in database table.
    
    def __str__(self):
        return f"Post of {self.user.username}"
    
    
class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    liked_at = models.DateTimeField(auto_now_add=True)

    # New field to track active status
    # already_liked = models.BooleanField(default=False)


    def __str__(self):
        return f"Liked by {self.user.username} on {self.post}"
    
class FollowersCount(models.Model):
    follower =models.CharField(max_length=100) # stores the 'username' of user who follow
    user = models.CharField(max_length=100)   # stores the 'username' of a user who is being followed

    def __str__(self):
        return f"{self.follower} just followed {self.user}"
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments') # id of the post which was commented
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # id of the user who wrote comment
    content = models.TextField(max_length = 200)
    commented_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Comment by {self.user.username} on {self.post.user}"
    

class OTPModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'OTP for {self.user.username}: {self.otp}'


class ChatMessage(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages',null=True)
    message = models.TextField(max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=True)
    group = models.ForeignKey('Group',on_delete=models.CASCADE,null=True)  # to represent the group name of chat

    def __str__(self):
        return f'meaaage send by {self.sender} to  {self.receiver}'

class Group(models.Model):
    group_name =models.CharField(max_length=255)

    def __str__(self):
        return self.group_name



    