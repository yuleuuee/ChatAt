
// upload image button change :

const defaultBtn = document.querySelector('#default_btn');
function defaultBtnActive() {
    defaultBtn.click();
}

function getImagePreview(event){
  // console.log(event.target.files[0]);
  var image = URL.createObjectURL(event.target.files[0]);
  var profile_img_div = document.getElementById('profile_img_div');
  var new_img = document.createElement('img');
  new_img.src = image;
  new_img.width='100';
  new_img.height='100';
  profile_img_div.innerHTML = '';
  profile_img_div.appendChild(new_img);
}

// const default_img = document.getElementById('custom_img_btn')
// const preview_img_div = document.getElementById('preview_img_div')
// const profile_image_cross = document.getElementById('profile_image_cross')
// profile_image_cross.addEventListener('click',()=>{
//   default_img.style.display='block'
// })



//*********** Password cahnge and delete acc part ***************///

const change_pass_btn = document.getElementById('change_pass_btn');
const delete_acc_btn = document.getElementById('delete_acc_btn');

const password_change_box = document.getElementById('password_change_box');
const acc_delete_box = document.getElementById('acc_delete_box');
const overlay = document.getElementById('overlay');



change_pass_btn.addEventListener('click',()=>{
  password_change_box.style.display="flex";
  password_change_box.style.zIndex="200";
  // acc_delete_box.style.display="none";
  overlay.style.display = "block";
})

delete_acc_btn.addEventListener('click',()=>{
  acc_delete_box.style.display="flex";
  acc_delete_box.style.zIndex="200";
  // password_change_box.style.display="none";
  overlay.style.display = "block";
})

// ********* cross btn clicking **************** :

const cross01 = document.getElementById('cross01');
const cross02 = document.getElementById('cross02');

cross01.addEventListener('click',()=>{
  password_change_box.style.zIndex="none";
  password_change_box.style.display="none";
  overlay.style.display = "none";
})

cross02.addEventListener('click',()=>{
  acc_delete_box.style.zIndex="none";
  acc_delete_box.style.display="none";
  overlay.style.display = "none";
})