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

    path('profile_page/',views.profile_page,name ='profile_page'),
    path('add_post/',views.add_post,name ='add_post'),
]

