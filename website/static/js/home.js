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


// *********************** Nice login page css **********************/


// ************* block mving **********************


const container = document.getElementById('container');
const registerBtn = document.getElementById('register');
const loginBtn = document.getElementById('login');

registerBtn.addEventListener('click', () => {
    container.classList.add("active");
});

loginBtn.addEventListener('click', () => {
    container.classList.remove("active");
});


// *************** login eye ********************

const password = document.querySelector("[type=password]");
const eye_div = document.querySelector("#eye_div");


password.addEventListener("focus", () => {
    if (password.type == "password") {
        eye_div.innerHTML='<i class="fa-solid fa-eye-slash password_eye"></i>'
    } else {
        eye_div.innerHTML='<i class="fa-solid fa-eye password_eye"></i>'
    }

  });

  eye_div.addEventListener("click", () => {
    if (password.type == "password") {
      password.type = "text";
      eye_div.innerHTML='<i class="fa-solid fa-eye password_eye"></i>'
    } else {
      password.type = "password";
      eye_div.innerHTML='<i class="fa-solid fa-eye-slash password_eye"></i>'
    }
  });

//   This event listener will trigger when the password field loses focus
  password.addEventListener("blur", () => {
    if (password.type != "password") {
        password.type = "password";
        eye_div.innerHTML = '<i class="fa-solid fa-eye-slash password_eye"></i>';
    }
    });


  // **************** sigin up eye *******************

  const pass01 = document.getElementById("pass01");
  const pass02 = document.getElementById("pass02");

  const eye_div1 = document.querySelector("#ac_eye_div1");
  const eye_div2 = document.querySelector("#ac_eye_div2");

// pass01
  pass01.addEventListener("focus", () => {
    if (pass01.type == "password") {
        eye_div1.innerHTML='<i class="fa-solid fa-eye-slash password_eye"></i>'
    } else {
        eye_div1.innerHTML='<i class="fa-solid fa-eye password_eye"></i>'
    }

  });

  eye_div1.addEventListener("click", () => {
    if (pass01.type == "password") {
      pass01.type = "text";
      eye_div1.innerHTML='<i class="fa-solid fa-eye password_eye"></i>'
    } else {
      pass01.type = "password";
      eye_div1.innerHTML='<i class="fa-solid fa-eye-slash password_eye"></i>'
    }
  });

  pass01.addEventListener("blur", () => {
    if (pass01.type != "password") {
        pass01.type = "password";
        eye_div1.innerHTML = '<i class="fa-solid fa-eye-slash password_eye"></i>';
    }
    });

  


// pass02
pass02.addEventListener("focus", () => {
    if (pass02.type == "password") {
        eye_div2.innerHTML='<i class="fa-solid fa-eye-slash password_eye"></i>'
    } else {
        eye_div2.innerHTML='<i class="fa-solid fa-eye password_eye"></i>'
    }

  });

  eye_div2.addEventListener("click", () => {
    if (pass02.type == "password") {
      pass02.type = "text";
      eye_div2.innerHTML='<i class="fa-solid fa-eye password_eye"></i>'
    } else {
      pass02.type = "password";
      eye_div2.innerHTML='<i class="fa-solid fa-eye-slash password_eye"></i>'
    }
  });

  pass02.addEventListener("blur", () => {
    if (pass02.type != "password") {
        pass02.type = "password";
        eye_div2.innerHTML = '<i class="fa-solid fa-eye-slash password_eye"></i>';
    }
    });

