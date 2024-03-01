from django.contrib import admin
from .models import UserProfile
from .models import Post
from .models import Like
from .models import FollowersCount
from .models import Comment
from .models import OTPModel
from .models import ChatMessage

# Register your models here.

# by doing this database will have 'website_users' table
# that table contains all the fields we created inside 'Users' models

admin.site.register(UserProfile)

admin.site.register(Post)
admin.site.register(Like)
admin.site.register(FollowersCount)
admin.site.register(Comment)
admin.site.register(OTPModel)
admin.site.register(ChatMessage)
