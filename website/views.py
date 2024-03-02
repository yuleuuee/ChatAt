from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from django.contrib.auth.models import User
from .models import UserProfile,Post,Like,FollowersCount,Comment

from datetime import datetime

from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from .models import OTPModel
from chat_app.settings import EMAIL_HOST_USER


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

            login(request, user) # making the user logged in 

            messages.success(request, "Successfully registered")
            return redirect('settings') # after succesful account creation users are sent to account settings page
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


    #  object of the curreltly logged in user :
    user_profile = UserProfile.objects.get(user=request.user)


    # getting all comments object
    comments = Comment.objects.all()

    likes = Like.objects.all()


    current_user = request.user # i dont theink this is necessary , you can delete 
   
    current_time = datetime.now().time()
    #  today_date = datetime.now().date()
    # 'current_time': current_time,'today_date':today_date ,



    # ************ Show feeds of only following users and current user ***************

    user_following_list = []
    feed = []

    # Retrieve all posts of the current user
    my_posts = Post.objects.filter(user=request.user)

    # Include the posts of the current user in the feed
    feed.extend(my_posts)

    user_following = FollowersCount.objects.filter(follower=request.user.username)

    # Retrieve User objects corresponding to the usernames
    for user_follow in user_following:
        user = get_object_or_404(User, username=user_follow.user)
        user_following_list.append(user)

    # Filter posts by the retrieved User objects
    for user in user_following_list:
        feed_lists = Post.objects.filter(user=user)
        feed.extend(feed_lists)


    # ****************************  User suggestions *********************************
    import random 

      # Get all users except the current user and the admin user
    all_users = User.objects.exclude(username=request.user.username).exclude(is_superuser=True)

    # Get the usernames of users whom the current user is following
    following_usernames = FollowersCount.objects.filter(follower=request.user.username).values_list('user', flat=True)

    # Exclude the users whom the current user is already following
    suggested_users = all_users.exclude(username__in=following_usernames)

    
    
     # Shuffle the suggested users and limiting the number of users shown
    suggested_users_subset = random.sample(list(suggested_users), min(len(suggested_users), 4))



    #**************************** greeting for the users *********************************
        

    if current_time.hour < 12:
        greeting = "Good morning"
    elif current_time.hour < 18:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"

     # Checking if the user has liked each post and pass the information to the template
    for post in feed:
        post.user_has_liked = post.likes.filter(user=request.user).exists()
    
    context={
        'current_user': current_user, 
        'greeting': greeting ,
        'user_profile':user_profile,
        'posts': feed,
        'suggested_users': suggested_users_subset,
        'comments':comments,
        'likes':likes,

        
    }

    # ****************************** Searching Users :*******************************
    

    query = request.GET.get('query')

    if query:
        search_results = User.objects.filter(username__icontains=query).exclude(is_superuser=True)
        if search_results.exists():
            # messages.success(request, 'Username was found successfully!')
            pass
        else:
            messages.error(request, 'Username does not match any existing user.')
    else:
        search_results = None

    context['search_results'] = search_results
    return render(request, 'public.html', context)

# ------------------------------------------------------------------------------------------------------

@login_required(login_url='login')
def settings(request):
    # current_user = request.user

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
        # return render(request,'other_profile.html',{'user_profile':user_profile})

        return redirect('profile', pk=user_profile.user)
    else:
        return render(request,'settings.html',{'user_profile':user_profile})

    
# ------------------------------------------------------------------------------------------------------
@login_required(login_url='login')
def profile(request,pk):
    user_object = User.objects.get(username =pk)
    user_profile = UserProfile.objects.get(user=user_object)
    user_posts = Post.objects.filter(user =user_profile.id) #getting the user_post info by using user_profile.id
    user_post_no = len(user_posts)


     # Retrieve following and followers data for the current user
    following_usernames = FollowersCount.objects.filter(follower=request.user.username).values_list('user', flat=True)
    followers_usernames = FollowersCount.objects.filter(user=request.user.username).values_list('follower', flat=True)


    # Query UserProfile to get profile pictures of following and followers
    following_profiles = UserProfile.objects.filter(user__username__in=following_usernames)
    followers_profiles = UserProfile.objects.filter(user__username__in=followers_usernames)

    follower = request.user.username
    user =pk

    # if the user was already followed then 
    if FollowersCount.objects.filter(follower=follower,user=user).first():
        button_text ='Unfollow'
    else:
        button_text ='Follow'

    # no. of followers and no. following
    no_of_followers = len(FollowersCount.objects.filter(user=pk)) # here the 'user : view' is the person that has been followed
    no_of_following = len(FollowersCount.objects.filter(follower=pk)) # here the 'follower : viewer' is the person that has been followed

    context={
        'user_object':user_object,
        'user_profile':user_profile,
        'user_posts':user_posts,
        'user_post_no' : user_post_no,
        'button_text':button_text,
        'no_of_followers':no_of_followers,
        'no_of_following':no_of_following,
        'following_profiles':following_profiles,
        'followers_profiles':followers_profiles,

    }

    return render(request,'profile.html',context)


# ------------------------------------------------------------------------------------------------------

@login_required(login_url='login')
def add_post(request):

    # user_post, created = Post.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        user = request.user
        # post_img =request.FILES.get('post_img')
        # post_caption = request.POST['post_caption']

        if request.FILES.get('post_img') == None:
            messages.error(request, "Before posting, please make sure to upload an image!")
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

# ------------------------------------------------------------------------------------------------------
    
@login_required(login_url='login')
def like_post(request):

        post_id = request.GET.get('post_id') ; # if only GET request , using <a></a>
    # if request.method =='POST':
        user = request.user
        # user_id = request.POST['user_id']
        # post_id = request.POST['post_id'] # getting the post id which was just  liked 

        post = Post.objects.get(id=post_id) # getting the post object which was liked by comparing the id

        like_filter = Like.objects.filter(post_id=post_id,user_id = user.id).first()

        if like_filter == None:
            # new_like =Like.objects.create(post_id=post_id,user_id= user.id)
            # new_like.save()
            # post.no_of_likes=post.no_of_likes +1
            # post.save()
            messages.success(request, 'You just liked a post')
            return redirect('public')
        else:
            # like_filter.delete()
            # post.no_of_likes=post.no_of_likes -1
            # post.save()
            messages.success(request, 'You Unliked a post')
            return redirect('public')
        

# ------------------------------------------------------------------------------------------------------

    
@login_required(login_url='login')
def follow(request):
    if request.method =='POST':
        #getting the information from the 'form'
        follower = request.POST['follower'] # Viewer : currently logged in user
        user = request.POST['user'] # view : user which the viewer is viewing

        # checking whether or not the currerently logged in user is already followeing this user
        # if already followed case :
        if FollowersCount.objects.filter(follower=follower,user=user).first():
            delete_follower = FollowersCount.objects.get(follower=follower,user=user)
            delete_follower.delete()
            return redirect('/profile/'+user) #going to the profile of the same user whch the viewer was viewing
        else: 
             # if already not followed case :
            new_follower = FollowersCount.objects.create(follower=follower,user=user)
            new_follower.save()
            return redirect('/profile/'+user) 
    else:
        return redirect('public')
    
@login_required(login_url='login')
def delete_post(request,post_id):
    user = request.user
    # post_id = request.GET.get('post_id') # getting the post id which was just clicked for deleting

    # post = Post.objects.get(id=post_id) # getting the post object which was clicked by comparing the id

    post_to_delete = Post.objects.get(id=post_id, user=user)
    post_to_delete.delete()
    messages.success(request, 'Your Post Was deleted successfully.')
    return redirect('public')


# comment part

@login_required(login_url='login')
def comment(request):
    if request.method == 'POST':

        commentor = request.user # who just wrote a comment

        po_usr = request.POST.get('po_usr')  #  --> whose post was commented
        po_id = request.POST.get('po_id')    #  -->  id of post that was commented

        content = request.POST.get('cmt_content')  # comment text

        # Retrieve the Post instance using the username
        # post = get_object_or_404(Post, id=po_id)

        # getting the post object which was commented by comparing the id
        post = Post.objects.get(id=po_id)

        print(f'commenter: {commentor}')
        print('Post of : '+ po_usr)
        print('Post id : '+ po_id)
        if len(content) !=0 :
            new_comment = Comment.objects.create(post_id=po_id, user_id=commentor.id, content=content)
            post.no_of_comments=post.no_of_comments +1 # increasing the "no_of_comments" every time post with the particular id is commented
            post.save() # Save the updated Post object
            new_comment.save()
            messages.success(request, 'Comment posted successfully.')
        else:
            messages.error(request, 'Comment content cannot be empty.')

        return redirect('public') # as 'public view' gives all containts required for the 'public page'
    else:
        return redirect('public')  # Redirect to public page if not a POST request

#  Deketing comment part :
    
@login_required(login_url='login')
def delete_comment(request, comment_id):
    if request.method == 'POST':
        comment = get_object_or_404(Comment, id=comment_id)
        if comment.user == request.user:  # Check if the current user is the owner of the comment
            post = comment.post  # Get the associated post
            comment.delete()  # Delete the comment
            post.no_of_comments -= 1  # Decrement the number of comments of the post
            post.save()  # Save the updated Post object
            messages.success(request, 'Comment deleted successfully.')
        else:
            messages.error(request, 'You are not authorized to delete this comment.')
    return redirect('public')  # Redirect to the public page after deletion



#********************************* generating and sending otp in gmail ****************************************************
    
def forgot_pas(request):
    if request.method == 'POST':

        email = request.POST.get('email')

        if len(email) != 0: # this prevents the empty email box sending
            
            user = User.objects.filter(email=email).first() # check there is a user with that email

            if user:
                # Check if an OTPModel instance already exists for the user
                otp_instance = OTPModel.objects.filter(user=user).first()

                if otp_instance:
                    # Update the existing OTPModel instance with a new OTP
                    otp_instance.otp = get_random_string(length=6, allowed_chars='1234567890')
                    otp_instance.save()
                else:
                    # Create a new OTPModel instance for the user
                    otp_instance = OTPModel.objects.create(user=user, otp=get_random_string(length=6, allowed_chars='1234567890'))

                
                subject ='Your Password Reset OTP'                               # title of email
                message =f'Your OTP for resetting password is : {otp_instance}'  # message of email
                #  EMAIL_HOST_USER is the sender's' gmail
                receiver_email = [email]                                         # we can also pass list of receiver email

                send_mail(subject, message, EMAIL_HOST_USER,receiver_email, fail_silently=False)
                messages.success(request, 'OTP was just send to your email.')
                return render(request, 'forgot_pas.html',{'email':email})
            else:
                messages.error(request, 'That email does not have an account.')
                return redirect('forgot_pas')
        else:
            messages.error(request, 'Must enter email before sending')
            return redirect('forgot_pas')
    else:
        return render(request, 'forgot_pas.html')

def verify_otp(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        otp_entered = request.POST.get('otp')
        otp_obj = OTPModel.objects.filter(user__email=email, otp=otp_entered).first()
        if otp_obj:
            can_change_password = 'ok'
            messages.success(request, 'You can now Recover your password')
            return render(request, 'forgot_pas.html',{'can_change_password':can_change_password,'email_for_identity':email})
        else:
            messages.error(request, 'OTP Dose not match')
            return render(request, 'login.html')
    return render(request, 'forgot_pas.html')


# chnanging the forgot password part :

def change_forgot_password(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        new_password1 = request.POST['new_password1']
        new_password2 = request.POST['new_password2']


        user = User.objects.filter(email=email).first() # if email field is empty then this will give admin 
        if user.username != 'admin':
            if new_password1 == new_password2:
                user.set_password(new_password1)
                user.save()
                messages.success(request, "Password Was Succesfully Changed!")
                return redirect('login')
            else:
                messages.error(request, "New Passwords dosn't match!")
                return redirect('forgot_pas')
        else:
            messages.error(request, "User name doesnt exists!")
            return redirect('forgot_pas')
    else:
        return redirect('login')
    


# from django.http import HttpResponseBadRequest
# from .models import ChatMessage

@login_required(login_url='login')
def chat_room(request):

    user = request.user # this is the current user

    context={
        'user':user,
    }

   
    return render(request,'chat_room.html',{'context':context})
    
