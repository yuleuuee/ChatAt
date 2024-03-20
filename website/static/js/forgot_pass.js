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
cross_mark.addEventListener('click',()=>{
  error_msg.style.display = 'none';
});

cross_mark.addEventListener('click',()=>{
  success_msg.style.display = 'none';
});


// *********************** :: OTP Green Tick mark hide and show with Number restrictions :: ***********************


const verify_otp_btn = document.getElementById('verify_otp_btn')
const check_mark = document.getElementById("check_mark");
function CheckmarkVisibility(input) {
    if (input.value.length === 6) {
        check_mark.style.display = "block";
        verify_otp_btn.style.backgroundPosition='right center';
    } else {
        check_mark.style.display = "none";
        verify_otp_btn.style.backgroundPosition='left center';
    }
    input.value = input.value.replace(/[^0-9]/g, ''); // Restrict to numbers only(replaces any characters that are not numbers with an empty string)
}