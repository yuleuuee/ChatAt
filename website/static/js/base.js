// *********************** :: Notify message Part :: ***************************/

// auto hide msg
const error_msg = document.getElementById('error_msg');
const success_msg = document.getElementById('success_msg');

// Function to hide the message after 6s ( 6000ms = 6s )

if (error_msg) {
  setTimeout(() => {
    error_msg.style.display = 'none';
  }, 6000); 
}

if (success_msg) {
  setTimeout(() => {
    success_msg.style.display = 'none';
  }, 6000); 
}

// cross mark hide message
const cross_mark = document.getElementById('cross_mark');
if(cross_mark){
  cross_mark.addEventListener('click',()=>{
    error_msg.style.display = 'none';
  });

  cross_mark.addEventListener('click',()=>{
    success_msg.style.display = 'none';
  });
}



// ///*********** Sound part ***************///

// love sound :
function playAudioBulb() {
  var audio = document.getElementById('click-sound');
  audio.play();
}


// ------------- Chat users of nav part----------- :

const chat_btn = document.querySelector('#chat_btn')
const users_to_chat_div = document.querySelector('#users_to_chat')
users_to_chat_div.style.display='none';
chat_btn.addEventListener('click',()=>{
  if(users_to_chat_div.style.display ==='none'){
    users_to_chat_div.style.display='flex';
    chat_btn.classList.add('active_nav_list');
  }else{
    users_to_chat_div.style.display='none';
    chat_btn.classList.remove('active_nav_list');
  }
  
})

