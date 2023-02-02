var studentShiftCoursePLMBS = document.getElementById('studentShiftCoursePLMBS').getContext('2d');
var studentShiftCoursePLMBS_style = new Chart(studentShiftCoursePLMBS,{
  type: 'bar',
  data:{
    labels: ['BSA', 'BSBAFM', 'BSBAMM', 'BSBAOM','BSBAHRM','BSBABE','BSENTRE','BSREM','BSHM'],
    datasets:[
    {
      label: 'Shift',
      data: [bsaShift, bsbafmShift, bsbammShift,bsbaomShift,bsbahrmShift,bsbabeShift,bsentreShift,bsremShift,bshmShift],
      backgroundColor:[
        'rgba(127, 17, 224, 0.5)'
      ],
      borderColor: 'rgba(127, 17, 224, 0.5)',
      fill: true
    }
  ]
  }, 
  options:{
    indexAxis: 'y',
    legend: {
      display: false
  },
    responsive: true,
    maintainAspectRatio: false,
    layout:{
      padding:{
        top: 30
      }
    }
  }
})

var studentYearPLMBS = document.getElementById('studentYearPLMBS').getContext('2d');
var studentYearPLMBS_style = new Chart(studentYearPLMBS,{
  type: 'line',
  data:{
    labels: ['1st', '2nd', '3rd', '4th', '5th', '6th'],
    datasets:[
    {
      label: 'Students',
      data: [plmbsFirstYr, plmbsSecondYr, plmbsThirdYr, plmbsFourthYr, plmbsFifthYr, plmbsSixthYr],
      backgroundColor:[
        'rgba(127, 17, 224, 0.2)'
      ],
      borderColor: 'rgba(127, 17, 224, 0.2)',
      tension: 0.4,
      fill: true
    }]
  },
  options:{
    responsive: true,
    maintainAspectRatio: false,
    layout:{
      padding:{
        top: 20
      }
    }
  }
})

var genderPLMBS = document.getElementById('genderPLMBS').getContext('2d');
var genderPLMBS_style = new Chart(genderPLMBS,{
  type: 'doughnut',
  data:{
    labels: ['Male', 'Female'],
    datasets:[{
      data:[
        plmbsGenderM, plmbsGenderF
      ],
      backgroundColor:[
        'rgba(253, 161, 102, 1)',
        'rgba(205, 233, 215, 1)'
      ]
    }]
  },
  options:{
    responsive: true,
    maintainAspectRatio: false,
    legend: {
        position: 'bottom'
    },
    layout:{
      padding:{
        top: 20
      }
    },

  }
})

//  BS ACCOUNTANCY
var studentShiftAcc = document.getElementById('studentShiftAcc').getContext('2d');
var studentShiftAcc_style = new Chart(studentShiftAcc,{
  type: 'bar',
  data:{
    labels: ['1st', '2nd', '3rd', '4th', '5th', '6th'],
    datasets:[
    {
      label: 'Shift',
      data: [bsaShift1,bsaShift2,bsaShift3,bsaShift4,bsaShift5,bsaShift6],
      backgroundColor:[
        'rgba(253, 161, 102, 1)'
      ],
      borderColor: 'rgba(253, 161, 102, 1)',
      fill: true
    },
    {
      label: 'Stay',
      data: [bsaStay1,bsaStay2,bsaStay3,bsaStay4,bsaStay5,bsaStay6],
      backgroundColor:[
        'rgba(205, 233, 215, 0.5)'
      ],
      borderColor: 'rgba(205, 233, 215, 1)',
      fill: true
    },
  ]
  },
  options:{
    responsive: true,
    maintainAspectRatio: false,
    layout:{
      padding:{
        top: 20
      }
    }
  }
})

//  BS FM
var studentShiftFM = document.getElementById('studentShiftFM').getContext('2d');
var studentShiftFM_style = new Chart(studentShiftFM,{
  type: 'bar',
  data:{
    labels: ['1st', '2nd', '3rd', '4th', '5th', '6th'],
    datasets:[
    {
      label: 'Shift',
      data: [bsbafmShift1,bsbafmShift2,bsbafmShift3,bsbafmShift4,bsbafmShift5,bsbafmShift6],
      backgroundColor:[
        'rgba(253, 161, 102, 1)'
      ],
      borderColor: 'rgba(253, 161, 102, 1)',
      fill: true
    },
    {
      label: 'Stay',
      data: [bsbafmStay1,bsbafmStay2,bsbafmStay3,bsbafmStay4,bsbafmStay5,bsbafmStay6],
      backgroundColor:[
        'rgba(205, 233, 215, 0.5)'
      ],
      borderColor: 'rgba(205, 233, 215, 1)',
      fill: true
    },
  ]
  },
  options:{
    responsive: true,
    maintainAspectRatio: false,
    layout:{
      padding:{
        top: 20
      }
    }
  }
})

var studentShiftCourseCET = document.getElementById('studentShiftCourseCET').getContext('2d');
var studentShiftCourseCET_style = new Chart(studentShiftCourseCET,{
  type: 'bar',
  data:{
    labels: ['BSIT', 'BSCS', 'BSCHE', 'BSCE','BSCpE','BSEE','BSECE','BSME','BSMfgE'],
    datasets:[
    {
      label: 'Shift',
      data: [bsitShift, bscsShift, bscheShift, bsceShift,bscpeShift,bseeShift,bseceShift,bsmeShift,bsmfgeShift],
      backgroundColor:[
        'rgba(127, 17, 224, 0.5)'
      ],
      borderColor: 'rgba(127, 17, 224, 0.5)',
      fill: true
    }
  ]
  },
  options:{
    indexAxis: 'y',
    legend: {
      display: false
  },
    responsive: true,
    maintainAspectRatio: false,
    layout:{
      padding:{
        top: 30
      }
    }
  }
})

var studentYearCET = document.getElementById('studentYearCET').getContext('2d');
var studentYearCET_style = new Chart(studentYearCET,{
  type: 'line',
  data:{
    labels: ['1st', '2nd', '3rd', '4th', '5th', '6th'],
    datasets:[
    {
      label: 'Students',
      data: [cetFirstYr, cetSecondYr, cetThirdYr, cetFourthYr, cetFifthYr, cetSixthYr],
      backgroundColor:[
        'rgba(127, 17, 224, 0.2)'
      ],
      borderColor: 'rgba(127, 17, 224, 0.2)',
      tension: 0.4,
      fill: true
    }]
  },
  options:{
    responsive: true,
    maintainAspectRatio: false,
    layout:{
      padding:{
        top: 20
      }
    }
  }
})

var genderCET = document.getElementById('genderCET').getContext('2d');
var genderCET_style = new Chart(genderCET,{
  type: 'doughnut',
  data:{
    labels: ['Male', 'Female'],
    datasets:[{
      data:[
        cetGenderM, cetGenderF
      ],
      backgroundColor:[
        'rgba(253, 161, 102, 1)',
        'rgba(205, 233, 215, 1)'
      ]
    }]
  },
  options:{
    responsive: true,
    maintainAspectRatio: false,
    legend: {
        position: 'bottom'
    },
    layout:{
      padding:{
        top: 20
      }
    },

  }
})

// PER DEPARTMENT GRAPHS

//  BS IT
var studentShiftIT = document.getElementById('studentShiftIT').getContext('2d');
var studentShiftIT_style = new Chart(studentShiftIT,{
  type: 'bar',
  data:{
    labels: ['1st', '2nd', '3rd', '4th', '5th', '6th'],
    datasets:[
    {
      label: 'Shift',
      data: [bsitShift1,bsitShift2,bsitShift3,bsitShift4,bsitShift5,bsitShift6],
      backgroundColor:[
        'rgba(253, 161, 102, 1)'
      ],
      borderColor: 'rgba(253, 161, 102, 1)',
      fill: true
    },
    {
      label: 'Stay',
      data: [bsitStay1,bsitStay2,bsitStay3,bsitStay4,bsitStay5,bsitStay6],
      backgroundColor:[
        'rgba(205, 233, 215, 0.5)'
      ],
      borderColor: 'rgba(205, 233, 215, 1)',
      fill: true
    },
  ]
  },
  options:{
    responsive: true,
    maintainAspectRatio: false,
    layout:{
      padding:{
        top: 20
      }
    }
  }
})

//  BS CS
var studentShiftCS = document.getElementById('studentShiftCS').getContext('2d');
var studentShiftCS_style = new Chart(studentShiftCS,{
  type: 'bar',
  data:{
    labels: ['1st', '2nd', '3rd', '4th', '5th', '6th'],
    datasets:[
    {
      label: 'Shift',
      data: [bscsShift1,bscsShift2,bscsShift3,bscsShift4,bscsShift5,bscsShift6],
      backgroundColor:[
        'rgba(253, 161, 102, 1)'
      ],
      borderColor: 'rgba(253, 161, 102, 1)',
      fill: true
    },
    {
      label: 'Stay',
      data: [bscsStay1,bscsStay2,bscsStay3,bscsStay4,bscsStay5,bscsStay6],
      backgroundColor:[
        'rgba(205, 233, 215, 0.5)'
      ],
      borderColor: 'rgba(205, 233, 215, 1)',
      fill: true
    },
  ]
  },
  options:{
    responsive: true,
    maintainAspectRatio: false,
    layout:{
      padding:{
        top: 20
      }
    }
  }
})


