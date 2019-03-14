var svg = document.getElementById("vimage");
var clear_button = document.getElementById("but_clear");
var started = false;
var clicks=false;

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

var clear = function(e) {
    svg.innerHTML="";
}

clear_button.addEventListener("click", clear);
svg.addEventListener("click", drawCircle);
svg.addEventListener('click', colorCircle);
