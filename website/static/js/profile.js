const follower_no_div = document.getElementById('follower_no_div');
const following_no_div = document.getElementById('following_no_div');

const all_followers_users_div = document.getElementById('all_followers_users_div');
const all_following_users_div = document.getElementById('all_following_users_div');

follower_no_div.addEventListener('click', () => {
    all_followers_users_div.style.display = 'block';
    all_following_users_div.style.display = 'none';
});

following_no_div.addEventListener('click', () => {
    all_followers_users_div.style.display = 'none';
    all_following_users_div.style.display = 'block';
});

