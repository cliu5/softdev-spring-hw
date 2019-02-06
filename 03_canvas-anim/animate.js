var c = document.getElementById("playground");
var ctx = c.getContext("2d");

var animation=document.getElementById("circle");
var stopButton = document.getElementById("stop");

var id;
var radius = 1;
var growing = true;

var clear = function(e){
    ctx.clearRect(0, 0, c.width, c.height);
}

var stop = function(){
    window.cancelAnimationFrame(id);
}
var draw = function(){
    window.cancelAnimationFrame(id);
    ctx.clearRect(0, 0, c.width, c.height);
    ctx.beginPath();
    ctx.arc(c.width/2,c.height/2,radius,0,2*Math.PI);
    ctx.stroke();
    ctx.fillStyle = "pink";
    ctx.fill();
    if(c.width/2 == radius){
	     growing = false;
    }
    if(radius == 1){
	     growing = true;
    }
    if(growing){
	     radius++;
    }
    else{
	     radius--;
    }
    id = window.requestAnimationFrame(draw);
}

animation.addEventListener("click", draw);
stopButton.addEventListener("click", stop);
