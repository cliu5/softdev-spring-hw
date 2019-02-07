
var c = document.getElementById("playground");
var ctx = c.getContext("2d");

var animation=document.getElementById("circle");
var stopButton = document.getElementById("stop");
var dvdButton=document.getElementById("dvd");

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



var dvdAnimation=function(){
  window.cancelAnimationFrame(id);
  var rectWidth=100;
  var rectHeight=50;
  var xVel=1;
  var yVel=1;
  var cur_x=Math.floor(Math.random() * (c.width-rectWidth));
  var cur_y= Math.floor(Math.random() * (c.height-rectHeight));
    // make a new animate function so that whenever you click the button it starts at a new random location
    var animate=function(){
      window.cancelAnimationFrame(id);
      ctx.clearRect(0, 0, c.width, c.height);
      var logo=new Image();
      logo.src="logo_dvd.jpg";
      ctx.drawImage(logo,cur_x,cur_y,rectWidth,rectHeight);
      if(cur_x <= 0 || cur_x  + rectWidth >= c.width){
        xVel*=-1;
      }
      if(cur_y<=0 || cur_y+ rectHeight>= c.height){
        yVel*=-1;
      }
      cur_x+=xVel;
      cur_y+=yVel;
      id = window.requestAnimationFrame(animate);
}
animate();
}

dvdButton.addEventListener("click",dvdAnimation);
animation.addEventListener("click", draw);
stopButton.addEventListener("click", stop);
