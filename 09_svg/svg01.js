var svg = document.getElementById("vimage");
var clear_button = document.getElementById("but_clear");
var prevX;
var prevY;
var started = false;

var draw = function(e) {
    var c1 = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    c1.setAttribute("cx", e.offsetX);
    c1.setAttribute("cy", e.offsetY);
    c1.setAttribute("r", "20");
    c1.setAttribute("fill", "pink");
    c1.setAttribute("stroke", "pink");
    svg.appendChild(c1);
    if (!started){
      started = true;
    }
    
    else {
      var line = document.createElementNS("http://www.w3.org/2000/svg", "line");
      line.setAttribute("x1", prevX);
      line.setAttribute("y1", prevY);
      line.setAttribute("x2", e.offsetX);
      line.setAttribute("y2", e.offsetY);
      line.setAttribute("stroke", "#000000");
      svg.appendChild(line);
    }
    prevX = e.offsetX;
    prevY = e.offsetY;
}

var clear = function(e) {
    while(svg.lastChild){
	svg.removeChild(svg.lastChild);
    }
  started = false;
}

clear_button.addEventListener("click", clear);
svg.addEventListener("click", draw);
