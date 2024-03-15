const error_msg = document.getElementById('error_msg');

// Function to hide the message after 4s
if (error_msg) {
  setTimeout(() => {
    error_msg.style.display = 'none';
  }, 6000); // 6000ms = 6s
}


const success_msg = document.getElementById('success_msg');

// Function to hide the message after 4s
if (success_msg) {
  setTimeout(() => {
    success_msg.style.display = 'none';
  }, 6000); // 6000ms = 6s
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




// search clear 

// const clearBtn = document.getElementById("clear-btn");
// clearBtn.addEventListener("click", () => {
//   const searchInput = document.getElementById('searchInput');
//   searchInput.value = "";
// })
