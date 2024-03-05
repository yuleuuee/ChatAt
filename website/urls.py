from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name ='home'),
    path('login/',views.user_login,name ='login'),
    path('signup/',views.user_signup,name ='signup'),
    path('public/',views.public_page,name ='public'),
    path('logout/',views.user_logout,name ='logout'),
    path('delete_account/',views.delete_account,name ='delete_account'),
    path('change_password/',views.change_password,name ='change_password'),

    path('settings',views.settings,name ='settings'),

    path('profile/<str:pk>/',views.profile,name ='profile'),
    path('add_post/',views.add_post,name ='add_post'),
   
    path('like_post/',views.like_post,name ='like_post'),
    
    path('follow/',views.follow,name ='follow'),
    
    path('search_users/',views.public_page,name ='search_users'),
    
    path('delete_post/<int:post_id>/',views.delete_post,name ='delete_post'),

    path('comment/',views.comment,name ='comment'),

    path('forgot_pas/',views.forgot_pas,name ='forgot_pas'),
    path('verify_otp/',views.verify_otp,name ='verify_otp'),

    path('change_forgot_password/',views.change_forgot_password,name ='change_forgot_password'),


    path('delete_comment/<int:comment_id>/',views.delete_comment,name ='delete_comment'),

    path('chat_room/',views.chat_room, name='chat_room'),

    path('chat/<str:current_user>_<str:friend_user>/', views.private_chat, name='chat'),

]

