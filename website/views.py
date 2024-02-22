from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# from django.contrib.auth.forms import UserCreationForm
# from .forms import CustomUserCreationForm

from django.contrib.auth.models import User
from .models import UserProfile

# from django.contrib.auth.hashers import check_password,make_password

# Create your views here.

# # ------------------------------------------------------------------------------------------------------

def home(request):
    return render(request,'home.html',{})

# # ------------------------------------------------------------------------------------------------------

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
    

# ------------------------------------------------------------------------------------------------------

# Using Own form :
    
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
            messages.success(request, "Successfully registered")
            return redirect('login')
        else:
            messages.error(request, "Password dosn't match!")
            return redirect('signup')
    else:
        return render(request, 'signup.html') 
    
    
# Using Django "UserCreationForm" and overriding it  as "CustomUserCreationForm":
    
# def user_signup(request):  

#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)

#         if form.is_valid():
#             # creating a user
#             # user =form.save(commit=False)
#             form.save()
#             #authenticate and logging in the user
#             u_name = form.cleaned_data['username']
#             p_word = form.cleaned_data['password1']

#             user = authenticate(request, username=u_name,password =p_word)

#             if user is not None:
#                 login(request,user)
#                 messages.success(request, "Successfully registered")
#                 return redirect('profile')
#             else:
#                 messages.error(request, "There was an error")
#                 return redirect('signup')
#         else:
#              messages.error(request, "Form was not valid,try again")
#              return redirect('signup')
#     else:
#         form = CustomUserCreationForm()
#         context={'form':form}
#         return render(request, 'signup.html',context)
            

# ------------------------------------------------------------------------------------------------------

@login_required(login_url='login')
def public_page(request):
    user = request.user
    return render(request, 'public.html', {'user': user})

# ------------------------------------------------------------------------------------------------------
@login_required(login_url='login')
def user_logout(request):
    logout(request)
    messages.success(request,'Succesfully logged out!')
    return redirect('login')

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
    

@login_required(login_url='login')
def edit_profile(request):
    if request.method == 'POST':
        phone_no = request.POST['phone_no']
        uploaded_profile_pic = request.FILES['uploaded_profile_pic']
        
        current_user, created = UserProfile.objects.get_or_create(user=request.user)

        current_user.phone = phone_no
        current_user.profile_picture = uploaded_profile_pic
        current_user.save()  # Save the UserProfile

        messages.success(request, " Saved Chnage Success! ")
        return redirect('profile')
    else:
        messages.error(request, "No chaange were made")
        return redirect('public')


@login_required(login_url='login')    
def user_profile(request):
    current_user = request.user
    if request.method == 'POST':
        return render(request, 'profile.html', {'current_user': current_user})
    else:
        return render(request, 'profile.html', {'current_user': current_user})
    