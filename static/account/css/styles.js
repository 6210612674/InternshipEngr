
        var startProductBarPos=-1;
        window.onscroll=function(){
            var bar = document.getElementById('nav');
            if(startProductBarPos<0)startProductBarPos=findPosY(bar);
        
            if(pageYOffset>startProductBarPos){
                bar.style.position='fixed';
                bar.style.top=0;
            }else{
                bar.style.position='relative';
            }
        };
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
    
    function openNav() {
      document.getElementById("mySidenav").style.width = "250px";
      document.getElementById("main").style.marginLeft = "250px";
      document.body.style.backgroundColor = "rgba(0,0,0,0.4)";
    }
    
    function closeNav() {
      document.getElementById("mySidenav").style.width = "0";
      document.getElementById("main").style.marginLeft= "0";
      document.body.style.backgroundColor = "white";
    }
    
    
    
    
    
