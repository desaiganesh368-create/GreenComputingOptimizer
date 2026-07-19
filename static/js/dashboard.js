let cpuChart;
let ramChart;
let powerChart;
let carbonChart;
let ecoChart;
async function loadCharts() {

    const response = await fetch("/chart-data");

    const data = await response.json();

    cpuChart=createChart(
        "cpuChart",
        "CPU Usage",
        data.timestamps,
        data.cpu,
        "rgba(255,99,132,1)"
    );

    ramChart=createChart(
        "ramChart",
        "RAM Usage",
        data.timestamps,
        data.memory,
        "rgba(54,162,235,1)"
    );

    powerChart=createChart(
        "powerChart",
        "Power Consumption",
        data.timestamps,
        data.power,
        "rgba(255,206,86,1)"
    );

    carbonChart=createChart(
        "carbonChart",
        "Carbon Emission",
        data.timestamps,
        data.carbon,
        "rgba(75,192,192,1)"
    );

    ecoChart=createChart(
        "ecoChart",
        "Eco Score",
        data.timestamps,
        data.eco_score,
        "rgba(153,102,255,1)"
    );
}

async function updateCharts(){

    const response = await fetch(
        "/chart-data"
    );

    const data = await response.json();

    cpuChart.data.labels = data.timestamps;
    cpuChart.data.datasets[0].data = data.cpu;
    cpuChart.update();

    ramChart.data.labels = data.timestamps;
    ramChart.data.datasets[0].data = data.memory;
    ramChart.update();

    powerChart.data.labels = data.timestamps;
    powerChart.data.datasets[0].data = data.power;
    powerChart.update();

    carbonChart.data.labels = data.timestamps;
    carbonChart.data.datasets[0].data = data.carbon;
    carbonChart.update();

    ecoChart.data.labels = data.timestamps;
    ecoChart.data.datasets[0].data = data.eco_score;
    ecoChart.update();
}


function createChart(
    canvasId,
    label,
    labels,
    values,
    color
){

    return new Chart(
        document.getElementById(canvasId),
        {
            type: "line",

            data: {
                labels: labels,

                datasets: [{
                    label: label,
                    data: values,
                    borderColor: color,
                    fill: false,
                    tension: 0.3
                }]
            }
        }
    );
}

loadCharts();


async function updateMetrics() {

    const response = await fetch("/live-data");

    const data = await response.json();

    document.getElementById(
        "cpu-value"
    ).innerText = data.cpu + "%";

    document.getElementById(
        "ram-value"
    ).innerText = data.memory + "%";

    document.getElementById(
        "disk-value"
    ).innerText = data.disk + "%";

    document.getElementById(
        "battery-value"
    ).innerText = data.battery;

    document.getElementById(
        "power-value"
    ).innerText = data.power + " W";

    document.getElementById(
        "carbon-value"
    ).innerText =
        data.carbon + " kg CO₂";

    document.getElementById(
        "eco-value"
    ).innerText =
        data.eco_score + "/100";

    document.getElementById(
        "eco-status"
    ).innerText =
        data.eco_status;
}

updateMetrics();
setInterval(
    updateMetrics,
    5000
);

loadCharts();

setInterval(
    updateCharts,
    5000
);