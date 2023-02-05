

  let OpenBtn = document.querySelector('.bi-list');
  let CloseBtn = document.querySelector(".bi-x-lg");
  let menu = document.querySelector(".navbar__menu");
  let menuItems = document.querySelectorAll(".navbar__menu--item");


  OpenBtn.addEventListener("click",()=>{
    OpenBtn.classList.toggle('hide');
    CloseBtn.classList.toggle('hide');
    menu.classList.toggle("hidden");
   

  });

  CloseBtn.addEventListener("click",()=>{
    OpenBtn.classList.toggle('hide');
    CloseBtn.classList.toggle('hide');
    menu.classList.toggle("hidden");
    
  });

menuItems.forEach((item) => {
  item.addEventListener("click",()=>{
    OpenBtn.classList.toggle('hide');
    CloseBtn.classList.toggle('hide');
    menu.classList.toggle("hidden");
    });
  
});



