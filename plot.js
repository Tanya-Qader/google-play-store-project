// Load the data from the Flask route
d3.json("/average_type_rating")
  .then(function(data){
      console.log(data);

    // Create an array of objects with key-value pairs
    const chartData = data.map(d => ({
      name: d.Type,
      value: d.Rating
    }));
  
    // Create the chart
    const pieChart = Recharts.generate({
      bindto: "#pie-chart",
      data: {
        columns: chartData,
        type : 'pie',
        colors: {
          Free: '#0088FE',
          Paid: '#00C49F'
        }
      },
      legend: {
        show: true,
        position: 'right'
      },
      tooltip: {
        show: true,
        format: {
          value: function (value, ratio, id) {
            return value.toFixed(2);
          }
        }
      }
    });
  
  });
  