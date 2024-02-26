const notify_msg = document.getElementById('notify_msg');

// Function to hide the message after 4s
if (notify_msg) {
  setTimeout(() => {
    notify_msg.style.display = 'none';
  }, 4000); // 4000ms = 4s
}

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


