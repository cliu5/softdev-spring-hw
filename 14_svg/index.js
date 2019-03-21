var array = [42];
var selection = d3.select("body");
var tds = d3.selectAll("tr").selectAll("td");
var spans = d3.selectAll("tr").selectAll("td").selectAll("span");
var sections = d3.selectAll("section");
var numbers = [4, 5, 18, 23, 42];
var divs = d3.selectAll("h2").data(numbers)
divs.enter();
var letters = [
  {name: "A", frequency: .08167},
  {name: "B", frequency: .01492},
  {name: "C", frequency: .02780},
  {name: "D", frequency: .04253},
  {name: "E", frequency: .12702}
];
