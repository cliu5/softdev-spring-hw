function clear()
{
  var c=document.getElementById('slate');
  var ctx=c.getContext("2d");
  ctx.clearRect(0,0,c.width,c.height);
}
var clearButton=document.getElementById("clear");
clearButton.addEventListener("click", clear());

var toggle=function(n)
{

}

//var clearButton = document.getElementById("clear");
//var toggleButton = document.getElementById("toggle");
//clearButton.addEventListener('click',function() {display(clear())});
