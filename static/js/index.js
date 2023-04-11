// const sign_up = document.getElementById("sign-up");
// const sign_in = document.getElementById("sign-in");
// const modal_container = document.getElementById("modal-container");
// const close = document.getElementById("modal-container");
// const modal = document.getElementById("modal");
// const su = document.getElementById("su");
// const si = document.getElementById("si");
// const form = document.getElementById("form");
// const ham = document.getElementById("ham");
// const hamMenuContainer = document.getElementById("ham-menu-container");
// const hamMenu = document.getElementById("ham-menu");
// const close2 = document.getElementById("ham-menu-container");


// login for users
// var check = 0;
// modal_container.addEventListener("mouseover", () => {
//   check = 0;
// });
// modal.addEventListener("click", () => {
//   check = 1;
// });

// sign_up.addEventListener("click", () => {
//   modal_container.classList.add("show");
//   si.classList.remove("selected");
//   su.classList.add("selected");
//   form.innerHTML =
//     "<br><br><center><input type='text' name='username' placeholder='Username'></center><br><br><center><input type='email' name='email' placeholder='E-mail'></center><br><br><center><input type='password' name='password1' placeholder='Password'></center><br><br><center><input type='password2' name='password' placeholder='Confirm Password'></center><br><br><center><button id='crtacc'>Create Account</button></center>";
// });

// su.addEventListener("click", () => {
//   si.classList.remove("selected");
//   su.classList.add("selected");
//   form.innerHTML =
//     "<br><br><center><input type='text' name='username' placeholder='Username'></center><br><br><center><input type='email' name='email' placeholder='E-mail'></center><br><br><center><input type='password' name='password1' placeholder='Password'></center><br><br><center><input type='password2' name='password' placeholder='Confirm Password'></center><br><br><center><button id='crtacc'>Create Account</button></center>";
// });

// sign_in.addEventListener("click", () => {
//   modal_container.classList.add("show");
//   su.classList.remove("selected");
//   si.classList.add("selected");
//   form.innerHTML =
//     "<br><br><center><input type='text' name='username' placeholder='Username'></center><br><br><center><input type='password' name='password' placeholder='Password'></center><br><br><center><button id='login'>Login</button></center>";
// });

// si.addEventListener("click", () => {
//   su.classList.remove("selected");
//   si.classList.add("selected");
//   form.innerHTML =
//     "<br><br><center><input type='text' name='username' placeholder='Username'></center><br><br><center><input type='password' name='password' placeholder='Password'></center><br><br><center><button id='login'>Login</button></center>";
// });

// close.addEventListener("click", () => {
//   if (check === 0) modal_container.classList.remove("show");
// });


// side bar menu 
// var check2 = 0;
// hamMenuContainer.addEventListener("mouseover", () => {
//   check2 = 0;
// });
// hamMenu.addEventListener("click", () => {
//   check2 = 1;
// });

// ham.addEventListener("click", () => {
//   hamMenuContainer.classList.add("show");
//   //setTimeout( () => {
//   hamMenu.classList.remove("ham-menu");
//   hamMenu.classList.add("ham-menu2");
//   //}, 300 );
// });

// close2.addEventListener("click", () => {
//   if (check2 === 0) {
//     hamMenu.classList.remove("ham-menu2");
//     hamMenu.classList.add("ham-menu");
//     hamMenuContainer.classList.remove("show");
//   }
// });


//carousel

// var slidePosition = 0;
// SlideShow();

// function SlideShow() {
//   var i;
//   var slides = document.getElementsByClassName("Containers");
//   for (i = 0; i < slides.length; i++) {
//     slides[i].style.display = "none";
//   }
//   slidePosition++;
//   if (slidePosition > slides.length) {
//     slidePosition = 1;
//   }
//   slides[slidePosition - 1].style.display = "block";
//   setTimeout(SlideShow, 2000); // Change image every 2 seconds
// } 

// var slidePosition = 1;
// SlideShow(slidePosition);

// // forward/Back controls
// function plusSlides(n) {
//   SlideShow((slidePosition += n));
// }

// //  images controls
// function currentSlide(n) {
//   SlideShow((slidePosition = n));
// }

// function SlideShow(n) {
//   var i;
//   var slides = document.getElementsByClassName("Containers");
//   var circles = document.getElementsByClassName("dots");
//   if (n > slides.length) {
//     slidePosition = 1;
//   }
//   if (n < 1) {
//     slidePosition = slides.length;
//   }
//   for (i = 0; i < slides.length; i++) {
//     slides[i].style.display = "none";
//   }
//   for (i = 0; i < circles.length; i++) {
//     circles[i].className = circles[i].className.replace(" enable", "");
//   }
//   slides[slidePosition - 1].style.display = "block";
//   circles[slidePosition - 1].className += " enable";
// }

// Preloader
// window.addEventListener("load", function () {
//   var preloader = document.getElementById("preloader");
//   preloader.style.display = "none";
// });
