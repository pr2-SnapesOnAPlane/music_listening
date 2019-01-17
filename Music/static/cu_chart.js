var ctx = document.getElementById("myChart2");
var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ["Album", "Single", "Shortform Album", "Video Longform"],
        datasets: [{
            label: 'Sum of Certified Units',
            data: [6447, 3173, 2, 9.9],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
            ],
            borderColor: [
                'rgba(255,99,132,1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            yAxes: [{
                scaleLabel: {
                    display: true,
                    labelString: 'Total Certified Units'
                },
                ticks: {
                    beginAtZero:true
                }
            }],
            xAxes: [{
                scaleLabel: {
                    display: true,
                    labelString: 'Format Type'
                }
            }]
        }
    }
});
