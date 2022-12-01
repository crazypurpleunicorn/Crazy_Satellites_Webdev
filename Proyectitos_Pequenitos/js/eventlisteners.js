//EVENT LISTENERS

//add default values to inputboxes, so you don`t have to write them every time
document.addEventListener("DOMContentLoaded", function (event) {
  document.getElementById("input1").value = "14000";
  document.getElementById("input2").value = "3000";
  document.getElementById("input3").value = "100";
  document.getElementById("input4").value = "2";
});

//add event listener to button, so capture the data inputed by the user
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
  var formattedArray = formatVector(unformattedArray);

  setVector(formattedArray);
});
