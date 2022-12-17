//EVENT LISTENERS
//global variable
let globalUnformattedArray=[];
//add default values to inputboxes, so you don`t have to write them every time
document.addEventListener("DOMContentLoaded", function (event) {
  document.getElementById("input1").value = "1400000";
  document.getElementById("input2").value = "3000";
  document.getElementById("input3").value = "100";
  document.getElementById("input4").value = "2";

  //fill div with svg inner html
  
  document.getElementById("divtofillwithsvg").innerHTML=createSVGRectangle(100,100)
});

//add event listener to button1, so capture the data inputed by the user
document.getElementById("btn1").addEventListener("click", function (event) {
  //Take input from text input boxes and assign them to given variables
  var assetValue = parseFloat(document.getElementById("input1").value);
  var baseIncome = parseFloat(document.getElementById("input2").value);
  var monthlyGain = parseFloat(document.getElementById("input3").value);
  var desiredTimeToUnlock = parseFloat(document.getElementById("input4").value);

  var unformattedArray = returnArrayTimeToUnlockTillTimeToUnlockIsEqualTo(
    assetValue,
    baseIncome,
    monthlyGain,
    desiredTimeToUnlock
  );
  globalUnformattedArray=unformattedArray;
  var formattedArray = formatVector(unformattedArray);

  setVector(formattedArray);});



//add event listener to button2, to change size of svg as wanted
document.getElementById("btn2").addEventListener("click", function (event) {
  let width=document.getElementById("input5").value;
  let height=document.getElementById("input6").value;
  let innerHtml=createSVGRectangle(width,height);
  document.getElementById("divtofillwithsvg").innerHTML=innerHtml;
  

});

//add event listener to button3, to add data points to the svg box
document.getElementById("btn3").addEventListener("click", function (event) {

  let extraInnerHtml=returnStringOfCircles(globalUnformattedArray)

  htmlInnerBefore=document.getElementById("divtofillwithsvg").childNodes[0].innerHTML;
  htmlInnerAfter=htmlInnerBefore.concat("\n\t",extraInnerHtml)
  document.getElementById("divtofillwithsvg").childNodes[0].innerHTML=htmlInnerAfter;




});