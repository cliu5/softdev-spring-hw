var data;
var tot = document.getElementById("tot");
var fifth = document.getElementById("fifth");
var tot5 = document.getElementById("tot5");

d3.json("https://raw.githubusercontent.com/stuy-softdev/workshop/master/thluffy/21_js-mfr/2006_-_2012_School_Demographics_and_Accountability_Snapshot.json?token=AFRFQK7N644MC7AUI4U22J242DI26", function(error, d) {
  data = d;
  //console.log(data)

  // filter out row entries that represent school PS015
  var PS015 = data.filter(function(n){
      return (n["DBN"]=="01M015");
  })
  console.log(PS015)

  var num_enrolled = PS015.map(function(n){
      return parseInt(n["total_enrollment"])
  });

  tot.innerHTML = num_enrolled
  console.log(num_enrolled)

  var num_fifth = PS015.map(function(n){
      return parseInt(n["grade5"])
  });

  fifth.innerHTML = num_fifth
  console.log(num_fifth)

  var sum_fifth = num_fifth.reduce(function(a,b){
      return a+b;
  });

  tot5.innerHTML = sum_fifth
  console.log(sum_fifth)
});
