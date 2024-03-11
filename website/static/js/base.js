const error_msg = document.getElementById('error_msg');

// Function to hide the message after 4s
if (error_msg) {
  setTimeout(() => {
    error_msg.style.display = 'none';
  }, 5000); // 4000ms = 4s
}


const success_msg = document.getElementById('success_msg');

// Function to hide the message after 4s
if (success_msg) {
  setTimeout(() => {
    success_msg.style.display = 'none';
  }, 5000); // 4000ms = 4s
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
// let a_link = document.querySelector(".nav_list>a");

bulb_box.addEventListener("click", change);
function change() {
  if (body.className == "black") {
    body.className = "white";
    // a_link.style.color ="black";
    bulb.style.color = "orange";
    bulb.style.textShadow = "2px 2px 3px black,-1px -1px 3px black";

  } else if (body.className == "white") {
    body.className = "black";
    bulb.style.color = "black";
    bulb.style.textShadow = "2px 2px 3px white,-1px -1px 3px white";
    // a_link.style.color ="white";
  }
}


// search clear 

// const clearBtn = document.getElementById("clear-btn");
// clearBtn.addEventListener("click", () => {
//   const searchInput = document.getElementById('searchInput');
//   searchInput.value = "";
// })
