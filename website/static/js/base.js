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

/*********** dark_light mode:  sun_moon ***************///

let dark_light = document.getElementById("dark_light");
let body = document.querySelector("body");
let sun_moon_icon = document.querySelector("#dark_light>i");

dark_light.addEventListener("click", ()=>{
  if (body.className == "black") {
    body.className = "white";
    dark_light.innerHTML='<i class="fa-solid fa-moon"></i>';
    sun_moon_icon.style.transform = 'scale(1.2)';
  } else if (body.className == "white") {
    body.className = "black";
    sun_moon_icon.style.transform = 'scale(1.2)';
    dark_light.innerHTML='<i class="fa-solid fa-sun"></i>';
  }

  // Reseting the transformation after 500 milliseconds
  setTimeout(() => {
    sun_moon_icon.style.transform = 'none';
  }, 200);  // in 2ms
});


// active status of the nav list------:

// ------------- Chat users ----------- :

const chat_btn = document.querySelector('#chat_btn')
const users_to_chat_div = document.querySelector('#users_to_chat')
users_to_chat_div.style.display='none';
chat_btn.addEventListener('click',()=>{
  if(users_to_chat_div.style.display ==='none'){
    users_to_chat_div.style.display='flex';
  }else{
    users_to_chat_div.style.display='none';
  }
  
})

