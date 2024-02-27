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


//  let  cmt_btn = document.querySelector('#cmt_btn')
//  let  cmt_box = document.querySelector('#cmt_box')

// ///*********** comment part ***************///


//  let  cmt_btn = document.getElementById('cmt_btn')
//  let  cmt_box = document.getElementById('cmt_box')

//  cmt_btn.addEventListener('click',()=>{
//     if (cmt_box.style.display=='none'){
//         cmt_box.style.display='block'
//     }else{
//         cmt_box.style.display='none'
//     }
//  });


// ///*********** Sound part ***************///

// const audio1 = new Audio();
// audio1.src = "./audios/click.mp3";

// // function play() {
// //   var audio = new Audio("./audios/love.mp3");
// //   audio.play();
// // }

// const audio = new Audio( "./audios/love.mp3");
// // audio.src = "./audios/love.mp3";


