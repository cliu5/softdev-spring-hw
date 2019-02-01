var c = document.getElementById("slate");
var ctx = c.getContext("2d");
var clear = document.getElementById("clear");
var toggle = document.getElementById("toggle");

//clear function, uses a clearRect function that takes the width and height of canvas as parameters
clear.addEventListener('click', function(e){
    e.preventDefault()
    ctx.clearRect(0, 0, c.width, c.height)
}
)


//Checks to see what the current mode is-- if it's rectange, switch to dot, if it's dot, switch to rectange
var isRect = true;
toggle.addEventListener('click', function(e) {
    isRect = !isRect;
    if(isRect) {
	this.innerHTML = "rectangle";
  }
  else {
    this.innerHTML = "dot";
  }
});


c.addEventListener('click', function(e){
    //getting coords after offset
    var xcor = e.offsetX;
    var ycor = e.offsetY;
    if (toggle.innerHTML == "dot") {
	ctx.fillStyle="pink";
      ctx.fillRect(xcor, ycor, 90, 50);
    }
    else {
	ctx.fillStyle = "pink";
	//beginPath() allows you to  discard the previous path and start a new one. If you don't have beginpath(),  you'd be appending more and more to the previous path. So the clear method would only clear temporarily and once you start adding more circles, it would just add on to the circles before.
    
      ctx.beginPath(); 
      ctx.ellipse(xcor, ycor, 20, 20, Math.PI / 4, 0, 2 * Math.PI);
      ctx.stroke();
      ctx.fill();
    }

  }
)

