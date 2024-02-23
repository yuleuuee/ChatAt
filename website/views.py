from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# from django.contrib.auth.forms import UserCreationForm
# from .forms import CustomUserCreationForm

from django.contrib.auth.models import User
from .models import UserProfile,Post

from datetime import datetime

from django.utils.datastructures import MultiValueDictKeyError

# from django.contrib.auth.hashers import check_password,make_password

# Create your views here.

# # ------------------------------------------------------------------------------------------------------

def home(request):
    return render(request,'home.html',{})

# # ------------------------------ LOGIN -----------------------------------------------------------------------

def user_login(request):
    
    if request.method == 'POST':
        u_name = request.POST['username']
        p_word = request.POST['password']

        #User.objects.filter(username=u_name).first()
        if User.objects.filter(username=u_name).exists(): # to check if the username is in the 'auth_user' table exists
            
            user = authenticate(request,username=u_name, password=p_word)

            if user is not None: # if there is user with  provided password matches the stored password
                login(request, user)
                messages.success(request, "Successfully logged in!")
                return redirect('public')
            else:
                messages.error(request, "Password Incorrect!")
                return redirect('login')
        else:
            messages.error(request, "User Doesn't Exist")
            return redirect('login')
    else:
        return render(request, 'login.html', {})
    

# ----------------------------------- SIGNUP -------------------------------------------------------------------
    
def user_signup(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('signup')
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists!")
            return redirect('signup')
        elif pass1 == pass2:
            user = User.objects.create_user(username=username,email=email,password=pass1)
            user.save()

            #creating a UserProfile object for the New User: 
            # this means a row will be created for the 'New_user' in the 'UserProfile' table
            user_model = User.objects.get(username=username)
            new_UserProfile = UserProfile.objects.create(user =user_model) 
            new_UserProfile.save()

            messages.success(request, "Successfully registered")
            return redirect('login')
        else:
            messages.error(request, "Password dosn't match!")
            return redirect('signup')
    else:
        return render(request, 'signup.html') 
            
# ----------------------------------- LOGOUT -------------------------------------------------------------------
@login_required(login_url='login')
def user_logout(request):
    logout(request)
    messages.success(request,'Succesfully logged out!')
    return redirect('login')

# ------------------------------------------
@login_required(login_url='login')
def public_page(request):
    current_user = request.user
    today_date = datetime.now().date()
    current_time = datetime.now().time()

    if current_time.hour < 12:
        greeting = "Good morning"
    elif current_time.hour < 18:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"

    return render(request, 'public.html', {'current_user': current_user, 'greeting': greeting ,'current_time': current_time,'today_date':today_date})

# ------------------------------------------------------------------------------------------------------

# @login_required(login_url='login')    
# def user_profile(request):
#     current_user = request.user
#     # {'current_user': current_user}
#     # user_profile = UserProfile.objects.get(user=request.user)
#     if request.method == 'POST':
#        return render(request, 'profile.html',{'current_user': current_user})
#     else:
#         if request.user.is_authenticated:
#             return render(request, 'profile.html',{'current_user': current_user})
#         else:
#             messages.error(request, "You must log in before visiting that page.")
#             return redirect('login')

# ------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------
# ----------------------------------------: FUNCTIONS :-------------------------------------------------
# ------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------

@login_required(login_url='login')
def delete_account(request):
    if request.method == 'POST':
        confirm_pass = request.POST['confirm_pass']

         # Authenticate the user with entered password
        user = authenticate(username=request.user.username, password=confirm_pass)
        
        #Password is correct for the current user then
        if user is not None:
            user.delete()
            messages.success(request,'Succesfully Deleted Account!')
            return redirect('login')
        else:
            messages.error(request, "Password dosn't match!")
            return redirect('public')
    else:    
        # will never be this
        return redirect('public')
    

# ------------------------------------------------------------------------------------------------------


@login_required(login_url='login')
def change_password(request):
    if request.method == 'POST':
        old_password = request.POST['old_password']
        new_password1 = request.POST['new_password1']
        new_password2 = request.POST['new_password2']

        # Authenticate the user with entered old password
        user = authenticate(username=request.user.username, password=old_password)
        
        #Password is correct for the current user then
        if user is not None:
            if new_password1 == new_password2:
                user.set_password(new_password1)
                user.save()
                messages.success(request, "Password Successfully Changed")
                return redirect('public')
            else:
                messages.error(request, "New Passwords dosn't match!")
                return redirect('public')
        else:
            messages.error(request,'Old Password was Incorrect!, go to "Forgot password"')
            return redirect('public')
    else:    
        # will never be this
        return redirect('public')
    
# ------------------------------------------------------------------------------------------------------

@login_required(login_url='login')
def profile_page(request):
    current_user = request.user

    # this is the UserProfile Object, we can now assign value to the object's entities
    # object's entities includes : profile_picture,bio,phone
    user_profile = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':
        if request.FILES.get('new_profile_pic') == None:
            new_profile_pic =user_profile.profile_picture #getting the default profile pic from the media
        else:
            new_profile_pic =request.FILES.get('new_profile_pic') #getting from the uploaded file

        
        new_phone_no = request.POST['new_phone_no']
        new_bio = request.POST['new_bio']
    
        user_profile.profile_picture = new_profile_pic
        user_profile.phone = new_phone_no
        user_profile.bio = new_bio

        user_profile.save()  # Save the UserProfile

        messages.success(request, " Save Change Success! ")
        return render(request,'profile.html',{'user_profile':user_profile})
        # return render(request, 'profile.html',{'current_user': current_user})
    else:
        return render(request, 'profile.html',{'user_profile':user_profile})



    # if request.method == 'POST':

    #     current_user, created = UserProfile.objects.get_or_create(user=request.user)

    #     try:
    #         uploaded_profile_pic = request.FILES['uploaded_profile_pic']
    #         current_user.profile_picture = uploaded_profile_pic
    #     except MultiValueDictKeyError: # if there is a error in getting profile_pic :
    #         phone_no = request.POST['phone_no']
    #         if len(phone_no) == 0:
    #             messages.error(request, "Phone no. Can't be Blank ! ")
    #             return redirect('profile')
    #         else:
    #             current_user.phone = phone_no
       
    #     current_user.save()  # Save the UserProfile

    #     messages.success(request, " Save Change Success! ")
    #     return redirect('profile')
    # else:
    #     messages.error(request, "No chaange were made")
    #     return redirect('public')


    
# ------------------------------------------------------------------------------------------------------
# @login_required(login_url='login')
# def add_post(request):

#     if request.method == 'POST':
#         current_user, created = Post.objects.get_or_create(user=request.user)
#         try:
#             uploaded_post_img = request.FILES['uploaded_post_img']
#             current_user.image = uploaded_post_img
#         except MultiValueDictKeyError:
#             content = request.POST['content']
#             if  content :
#                 current_user.content = content
#             else:
#                 current_user.content = 'Null'

#         current_user.save()     
#         # current_user.image = uploaded_post_img

#          # Create a new Post instance
#         # new_post = Post(user=request.user,content=content)

#         # if uploaded_post_img:
#         #     new_post.image = uploaded_post_img
#         # else:
#         #     new_post.content = content
        

#         # new_post.save()  # Save the UserProfile

#         messages.success(request, "New Post Added! ")
#         return redirect('public')
#     else:
#         return redirect('public')
