const wrapper = document.querySelector('.wrapper');
const fileName = document.querySelector('.file-name');
const cancelBtn = document.querySelector('#cancel-btn');
const defaultBtn = document.querySelector('#default-btn');
const img = document.querySelector('#upload_img');
const regularExp = /[0-9a-zA-Z\^\&\'\@\{\}\[\]\,\$\=\!\-\#\(\)\.\%\+\~\_ ]+$/;
let imageRemoved = false; // Flag to track if the image has been removed


function defaultBtnActive() {
    defaultBtn.click();
    wrapper.style.height = '360px';
}

defaultBtn.addEventListener('change', function() {
    const file = this.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function() {
            const result = reader.result;
            img.src = result;
            wrapper.classList.add('active');
            imageRemoved = false; //  --> image is still there 
        };
        reader.readAsDataURL(file);
    } else {
        // No file selected, decrease the size of the wrapper div
        wrapper.style.height = 'auto';
        imageRemoved = true;
    }

    // Update file name if available
    if (this.files.length > 0) {
        let valueStore = this.files[0].name;
        fileName.textContent = valueStore;
    }
});


cancelBtn.addEventListener('click', function() {
    img.src = "";
    wrapper.style.height = 'auto';
    wrapper.classList.remove('active');
    imageRemoved = true; // --> image is removed 

});


document.getElementById('add_post_form').addEventListener('submit', function(event) {
    // Prevent form submission if the image has been removed
    if (imageRemoved) {
        event.preventDefault();
    }
});
 

 /********** Scroll up ******* */

 let day = document.querySelector('#stop');
 let goTop= document.querySelector('#goTop');
 goTop.addEventListener('click', () => scrollup()); 

 function scrollup() {
         day.scrollIntoView(
         {
             block:'center', 
             behavior:'smooth'
         }
         );
 };


// ///*********** Sound part ***************///

// love sound :
function playAudio() {
    var audio = document.getElementById('love-sound');
    audio.play();
}



///***********  Date in human redable format ***************///

document.addEventListener("DOMContentLoaded", function() {
    // Get all elements with the data-posted-at attribute
    const postedAtElements = document.querySelectorAll("[data-posted-at]");
    postedAtElements.forEach(function(element) {
        // Parse the posted datetime from the data attribute
        const postedAt = new Date(element.dataset.postedAt);
        // Get the current datetime
        const now = new Date();
        // Calculate the time difference in milliseconds
        const diff = now - postedAt;
        // Convert milliseconds to seconds, minutes, hours, days, weeks, months, or years
        let time;
        const seconds = Math.floor(diff / 1000);
        const minutes = Math.floor(diff / 60000);
        const hours = Math.floor(diff / 3600000);
        const days = Math.floor(diff / 86400000);
        const weeks = Math.floor(diff / 604800000);
        const months = Math.floor(diff / 2629800000);
        const years = Math.floor(diff / 31557600000);
        
        if (seconds < 60) {
            time = seconds === 1 ? "1 second ago" : seconds + " seconds ago";
        } else if (minutes < 60) {
            time = minutes === 1 ? "1 minute ago" : minutes + " minutes ago";
        } else if (hours < 24) {
            time = hours === 1 ? "1 hour ago" : hours + " hours ago";
        } else if (days < 7) {
            time = days === 1 ? "1 day ago" : days + " days ago";
        } else if (weeks < 4.35) {
            time = weeks === 1 ? "1 week ago" : weeks + " weeks ago";
        } else if (months < 12) {
            time = months === 1 ? "1 month ago" : months + " months ago";
        } else {
            time = years === 1 ? "1 year ago" : years + " years ago";
        }
        
        // Update the text content of the element
        element.textContent = time;
    });
});