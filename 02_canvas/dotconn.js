var c = document.getElementById("playground");
var ctx = c.getContext("2d");
var clear = document.getElementById("clear");
var dots=false;
var xcor;
var ycor;

//clear function, uses a clearRect function that takes the width and height of canvas as parameters
clear.addEventListener('click', function(){
    ctx.clearRect(0, 0, c.width, c.height);
    dots=false;
});
c.addEventListener('click', function(e){
  if (!dots){
    ctx.beginPath();
    ctx.fillStyle = "pink";
    xcor=e.offsetX;
    ycor=e.offsetY;
    ctx.ellipse(xcor, ycor, 20, 20, Math.PI / 4, 0, 2 * Math.PI);
ctx.stroke();
 ctx.fill();

 dots=true;

  }
  else{
  ctx.beginPath();
  ctx.fillStyle = "pink";
  ctx.moveTo(xcor,ycor);
   xcor=e.offsetX;
   ycor=e.offsetY;
  ctx.lineTo(xcor,ycor);
  ctx.ellipse(xcor, ycor, 20, 20, Math.PI / 4, 0, 2 * Math.PI);
  ctx.stroke();

  ctx.fill();
}});
