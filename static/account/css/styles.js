var startProductBarPos=-1;
window.onscroll=function(){
  var bar = document.getElementById('nav');
  var navbar = document.getElementById("mySidenav");
  var notibar = document.getElementById("myNoti")

  if(startProductBarPos<0)startProductBarPos=findPosY(bar);

  if(window.pageYOffset>startProductBarPos){
    //Main Menu
    bar.style.position='fixed';
    bar.style.top=0;
    //Side Menu
    navbar.classList.add("sticky");
    navbar.classList.add("mytopstyle");
    //Noti bar
    notibar.classList.add("sticky");
    notibar.classList.add("mytopstyle");
    

  }else{
    //Main Menu
    bar.style.position='relative';
    //Side Menu
    navbar.classList.remove("sticky");
    navbar.classList.remove("mytopstyle");
    //Noti bar
    notibar.classList.remove("sticky");
    notibar.classList.remove("mytopstyle");
  }
};

//Find where current top is
function findPosY(obj) {
  var curtop = 0;
  if (typeof (obj.offsetParent) != 'undefined' && obj.offsetParent) {
    while (obj.offsetParent) {
      curtop += obj.offsetTop;
      obj = obj.offsetParent;
    }
    curtop += obj.offsetTop;
  }
  else if (obj.y)
    curtop += obj.y;
  return curtop;
}

//Open Side Menu
function openNav() {
  document.getElementById("mySidenav").style.width = "250px";
  document.getElementById("main").style.marginLeft = "250px";
  document.body.style.backgroundColor = "rgba(0,0,0,0.4)";
  }
//Close Side Menu
function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
  document.getElementById("main").style.marginLeft= "0";
  document.body.style.backgroundColor = "white";
  }

//Open Notification 
function openNoti() {
  document.getElementById("myNoti").style.width = "250px";
  document.getElementById("myNoti").style.height = "200px";
  document.getElementById("main").style.marginLeft = "250px";
  document.body.style.backgroundColor = "rgba(0,0,0,0.4)";
  }
//Close Notification 
function closeNoti() {
  document.getElementById("myNoti").style.width = "0";
  document.getElementById("main").style.marginLeft= "0";
  document.body.style.backgroundColor = "white";
  }

  