let test_result = document.getElementById('test_result').getContext('2d');
let test_result_style = new Chart(test_result,{
  type: 'doughnut',
  data:{
    datasets:[{
      data:[
        100-predict, predict
      ],
      backgroundColor:[
        'rgba(249, 249, 249, 1)',
        'rgba(205, 233, 215, 1)'
      ]
    }]
  },
  options:{
    responsive: true,
    maintainAspectRatio: false,

    layout:{
      padding:{
        top: 100
      }
    },

  }
})




