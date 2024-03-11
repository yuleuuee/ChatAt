//*********** Password cahnge and delete acc part ***************///
const password_change_box = document.getElementById('password_change_box');
const acc_delete_box = document.getElementById('acc_delete_box');

function confirm_box2(){
  password_change_box.style.display="block";
  acc_delete_box.style.display="none";
}
        
function confirm_box() {
  acc_delete_box.style.display="block";
  password_change_box.style.display="none";
}


// # ****************************  Only my followers suggestions *********************************

// # Retrieve the usernames of users who follow you
// followers_usernames = FollowersCount.objects.filter(user=request.user.username).values_list('follower', flat=True)

// # Find users who follow you but you don't follow them back
// followers_without_following_back = set(followers_usernames) - set(following_usernames)

// # Shuffle the list of followers without following them back and limit the number of users shown
// followers_without_following_back_subset = random.sample(list(followers_without_following_back), min(len(followers_without_following_back), 3))

// # Query UserProfile to get profiles of users who follow you but you don't follow back
// followers_without_following_back_profiles = UserProfile.objects.filter(user__username__in=followers_without_following_back_subset)