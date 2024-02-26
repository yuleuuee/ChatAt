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

// const audio1 = new Audio();
// audio1.src = "./audios/click.mp3";

// // function play() {
// //   var audio = new Audio("./audios/love.mp3");
// //   audio.play();
// // }

// const audio = new Audio( "./audios/love.mp3");
// // audio.src = "./audios/love.mp3";


