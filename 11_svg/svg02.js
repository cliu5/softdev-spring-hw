var svg = document.getElementById("vimage");
var clear_button = document.getElementById("but_clear");
var move_button=document.getElementById("but_move");


var drawCircle = function(e) {
    
   var c1 = document.createElementNS("http://www.w3.org/2000/svg", "circle");

  if (e.target.nodeName == "circle") {
      pass
  }
    
    c1.setAttribute("cx", e.offsetX);
    c1.setAttribute("cy", e.offsetY);
    c1.setAttribute("r", "20");
    c1.setAttribute("fill", "pink");
    svg.appendChild(c1);
    circles.push(c1);
}  

var colorCircle=function(e){
     if(e.target.getAttribute("fill")=="pink"){
	e.target.setAttribute("fill","green");
    }
    else{
	e.target.setAttribute("cx", Math.floor(Math.random() * 500));
        e.target.setAttribute("cy", Math.floor(Math.random() * 500));
        e.target.setAttribute("fill", "pink");
    }
}

var circles=[];
var started = false;
var clicks=false;
var radius=1;
var id;
var xVel=1;
var yVel=1;

var moveCircle=function(){
    started=true;
    var animate=function(){
	window.cancelAnimationFrame(id);
	for(var i=0;i<circles.length;i++){
	    var circle=circles[i];
	    var curX=Number(circle.getAttribute("cx"));
	    var curY=Number(circle.getAttribute("cy"));
	    circle.setAttribute("cx", curX+xVel);
	    circle.setAttribute("cy", curY+yVel);
	    var curX=Number(circle.getAttribute("cx"));
	    var curY=Number(circle.getAttribute("cy"));
    

	    if(curX <= 0 || (curX  >= 500)){
        xVel *= -1;

      }
	    if(curY <= 0 || (curY >= 500)){
        yVel *= -1;

	    }

	
	}
    id = window.requestAnimationFrame(animate);
  }
	     animate();
	    }

var clear = function(e) {
    svg.innerHTML="";
}

clear_button.addEventListener("click", clear);
move_button.addEventListener('click',moveCircle);

svg.addEventListener("click", drawCircle);
svg.addEventListener('click', colorCircle);
