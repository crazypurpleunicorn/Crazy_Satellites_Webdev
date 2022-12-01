// JS

/*SETTERS...i am interseted in being able to change "let vector" since it is the vector used to display the graph
on the div element. The user when has its input parameters ready will click on 'btn1' where it says plot1 and 
a new graph created from this parameter should appear...To do that "vector" should be able to change every time
I click on this button. So i will define a function setVector at the end, to achieve this*/

let colors = JSC.getPalette("default");
let colorText = function (txt, colorIndex) {
  return '<span style="color:' + colors[colorIndex] + '"><b>' + txt + "</b></span>";
};
let titleText = "Monthly " + colorText("Purchases", 0) + " vs. " + colorText("Rent", 1);
let vector = [
  [1, 29.9],
  [2, 97.5],
  [3, 110.4],
  [4, 129.2],
  [5, 144.0],
  [6, 176.0],
];

let chart;

function paintChart() {
  chart = JSC.chart("chartDiv", {
    debug: true,
    type: "area",
    title_label_text: titleText,
    legend_visible: false,
    yAxis: {
      formatString: "c",
      scale_type: "stacked",
    },
    xAxis: {
      crosshair_enabled: true,
      //scale: { type: 'time' }
    },
    defaultSeries: {
      shape: {
        opacity: 0.6,
        /* Dynamic gradient that will work with any color series */
        fill: ["lightenMore", "#f1f1f1", 90],
      },
      defaultPoint_marker: {
        fill: "white",
        type: "circle",
        outline: { width: 1 },
      },
    },

    series: [
      {
        name: "Purchases",
        points: vector, //[

        /*[1, 29.9], 
          [2, 97.5], 
          [3, 110.4], 
          [4, 129.2], 
          [5, 144.0], 
          [6, 176.0] */
        //]
      },
      {
        name: "Rent",
        points: [
          [1, 86.9],
          [2, 79.5],
          [3, 95.4],
          [4, 97.2],
          [5, 123.0],
          [6, 111.0],
        ],
      },
    ],
  });
}

//not exactly a setter since vector is a global variable...This function changes the value of the
//global variable 'vector'
function setVector(array) {
  vector = array;
  paintChart();
}

paintChart();
