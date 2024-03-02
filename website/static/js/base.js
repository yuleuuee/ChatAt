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



// ///*********** Sound part ***************///

// love sound :
function playAudioBulb() {
  var audio = document.getElementById('click-sound');
  audio.play();
}

/*********** Bulb ***************///
let bulb_box = document.getElementById("light_bulb");
let body = document.querySelector("body");
let bulb = document.querySelector("#light_bulb>i");

bulb_box.addEventListener("click", change);
function change() {
  if (body.className == "black") {
    body.className = "white";
    // bulb_box.style.border = "3px solid black";
    bulb.style.color = "orange";
    // bulb.style.textShadow = "none";
    bulb.style.textShadow = "2px 2px 3px black,-1px -1px 3px black";
  } else if (body.className == "white") {
    body.className = "black";
    // bulb_box.style.border = "3px solid black";
    bulb.style.color = "black";
    bulb.style.textShadow = "2px 2px 3px white,-1px -1px 3px white";
  }
}