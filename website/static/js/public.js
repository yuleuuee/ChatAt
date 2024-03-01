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
