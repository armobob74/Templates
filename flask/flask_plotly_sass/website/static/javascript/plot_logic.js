let plotForm;

function randomFloatArray(n, minval = 0, maxval = 1) {
  let arr = [];
  for (let i = 0; i < n; i++) {
    arr.push(Math.random() * (maxval - minval) + minval);
  }
  return arr;
}

async function getData() {
	let formData = new FormData(plotForm)
	let response = await fetch('/api/make-data', {
	    method: 'POST',
	    body: formData
	})
	// response format is {"x":x,"y":y}
	let trace1 = await response.json()
  return [trace1];
}

let data = [{}]
data[0].mode = "lines";
data[0].line = { color: "rgb(75, 192, 192)" };

const layout = {
  title: "Just a Line",
  xaxis: { title: "X Axis Title", range:[0,1]},
  yaxis: { title: "Y Axis Title", range: [0, 1] },
};

async function updatePlot() {
  Plotly.animate(
    "myPlot",
    {
      data: await getData(),
      traces: [0],
    },
    {
      transition: {
        duration: 200,
        easing: "cubic-in-out",
      },
      frame: {
        duration: 200,
        redraw: false,
      },
    }
  );
}

document.addEventListener("DOMContentLoaded", function() {
    Plotly.newPlot("myPlot", data, layout);
    plotForm = document.getElementById('plot-form');
    document.querySelectorAll('#plot-form input').forEach((inpt)=>{
	    inpt.addEventListener('change', updatePlot)
    })
    updatePlot()
});
