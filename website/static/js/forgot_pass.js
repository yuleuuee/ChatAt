// *********************** notify_msg css ***************************/

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


// --------------------- OTP checkmark hidea and show + Number restrictions ------------------------


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
    input.value = input.value.replace(/[^0-9]/g, ''); // Restrict to numbers only
}