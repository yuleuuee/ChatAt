const follower_no_div = document.getElementById('follower_no_div');
const following_no_div = document.getElementById('following_no_div');

const all_followers_users_div = document.getElementById('all_followers_users_div');
const all_following_users_div = document.getElementById('all_following_users_div');

// Function to hide both follower and following divs
function hideBothDivs() {
    all_followers_users_div.style.display = 'none';
    all_following_users_div.style.display = 'none';

    follower_no_div.style.color = 'inherit'
    following_no_div.style.color ='inherit';

}


follower_no_div.addEventListener('click', () => {
    all_followers_users_div.style.display = 'flex';
    all_following_users_div.style.display = 'none';

    follower_no_div.style.color = 'rgb(182, 62, 26)';
    following_no_div.style.color ='inherit';


});

following_no_div.addEventListener('click', () => {
    all_followers_users_div.style.display = 'none';
    all_following_users_div.style.display = 'flex';

    follower_no_div.style.color = 'inherit'
    following_no_div.style.color = 'rgb(182, 62, 26)';
    
});

// Event listener for clicks on document body
document.body.addEventListener('click', (event) => {
    // Check if the clicked element is not follower_no_div or following_no_div
    if (event.target !== follower_no_div && event.target !== following_no_div && event.target !== all_followers_users_div &&  event.target !== all_following_users_div) {
        // If not, hide both divs
        hideBothDivs();
    }
});
