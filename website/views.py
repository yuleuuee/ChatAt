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

# # --------------------------------- LOGIN -----------------------------------------------------------------------

def user_login(request):

    # user_profile = UserProfile.objects.get(user=request.user)
    # user_profile = UserProfile.objects.get(user=request.user)  # Access id to fetch

    
    if request.method == 'POST':
        u_name = request.POST['username']
        p_word = request.POST['password']

        #User.objects.filter(username=u_name).first()
        if User.objects.filter(username=u_name).exists(): # to check if the username is in the 'auth_user' table exists
            
            user = authenticate(request,username=u_name, password=p_word)

            if user is not None: # if there is user with  provided password matches the stored password
                login(request, user)
                messages.success(request, "Successfully logged in!")
                return redirect('public') #,{'user_profile':user_profile}
            else:
                messages.error(request, "Password Incorrect!")
                return redirect('login')
        else:
            messages.error(request, "User Doesn't Exist")
            return redirect('login')
    else:
        return render(request, 'login.html')
    
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
# ------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------

@login_required(login_url='login')
def public_page(request):
    user_profile = UserProfile.objects.get(user=request.user)
    # user_post, created = Post.objects.get_or_create(user=request.user)

    posts = Post.objects.all()

    current_user = request.user
   
    current_time = datetime.now().time()
    #  today_date = datetime.now().date()
    # 'current_time': current_time,'today_date':today_date ,


    if current_time.hour < 12:
        greeting = "Good morning"
    elif current_time.hour < 18:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"

    return render(request, 'public.html', {'current_user': current_user, 'greeting': greeting ,'user_profile':user_profile,'posts': posts})

# ------------------------------------------------------------------------------------------------------

@login_required(login_url='login')
def profile_page(request):
    current_user = request.user

    # this is the UserProfile Object, we can now assign value to the object's entities
    # object's entities includes : profile_picture,bio,phone
    user_profile = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':
        if request.FILES.get('new_profile_pic') == None: # if the user is'nt submitting profile picture, #getting the default profile pic from the media
            new_profile_pic =user_profile.profile_picture 
        else: # if the user is submitting a profile picture ,# getting from the uploaded file
            new_profile_pic =request.FILES.get('new_profile_pic') 

        if len(request.POST['new_phone_no']) == 0:
            new_phone_no = user_profile.phone
        else:
            new_phone_no = request.POST['new_phone_no']
        
        if len(request.POST['new_bio']) == 0:
            new_bio = user_profile.bio
        else:
            new_bio = request.POST['new_bio']

        # new_phone_no = request.POST['new_phone_no']
        # new_bio = request.POST['new_bio']
    
        user_profile.profile_picture = new_profile_pic
        user_profile.phone = new_phone_no
        user_profile.bio = new_bio

        user_profile.save()  # Saving the changes in UserProfile

        messages.success(request, " Save Change Success! ")
        return render(request,'profile.html',{'user_profile':user_profile})
    else:
        return render(request,'profile.html',{'user_profile':user_profile})

    
# ------------------------------------------------------------------------------------------------------
    

@login_required(login_url='login')
def add_post(request):

    # user_post, created = Post.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        user = request.user
        # post_img =request.FILES.get('post_img')
        # post_caption = request.POST['post_caption']

        if request.FILES.get('post_img') == None:
            messages.error(request, "Must select an Image before posting")
            return redirect('public')
        else:
           post_img =request.FILES.get('post_img')

        if len(request.POST['post_caption']) == 0:
            post_caption = 'No Caption'
        else:
            post_caption = request.POST['post_caption']

        new_post = Post.objects.create(user = user, image = post_img, caption = post_caption)
        
        # user_post.image = post_img
        # user_post.caption = post_caption

        new_post.save()
        messages.success(request, "Post Added Succesfully!")
        return redirect('public')

    else:    
        return redirect('public') # this helps to go the the view public_page ,as it is using the name of the url



