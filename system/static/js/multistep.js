var currentTab = 0; // Current tab is set to be the first tab (0)
showTab(currentTab); // Display the current tab

function showTab(n) {
  // This function will display the specified tab of the form ...
  var x = document.getElementsByClassName("tab");
  x[n].style.display = "block";
  // ... and fix the Previous/Next buttons:
  if (n == 0) {
    document.getElementById("prevBtn").style.display = "none";
  } else {
    document.getElementById("prevBtn").style.display = "inline";
  }
  if (n == (x.length - 1)) {
    document.getElementById("nextBtn").innerHTML = "Submit";
  } else {
    document.getElementById("nextBtn").innerHTML = "Next";
  }
  // ... and run a function that displays the correct step indicator:
  fixStepIndicator(n)
}

function nextPrev(n) {
  // This function will figure out which tab to display
  var x = document.getElementsByClassName("tab");
  // Exit the function if any field in the current tab is invalid:
  if (n == 1 && !validateForm()) return false;
  // Hide the current tab:
  x[currentTab].style.display = "none";
  // Increase or decrease the current tab by 1:
  currentTab = currentTab + n;
  // if you have reached the end of the form... :
  if (currentTab >= x.length) {
    //...the form gets submitted:
    document.getElementById("shiftTest").submit();
    return false;
  }
  // Otherwise, display the correct tab:
  showTab(currentTab);
}

function validateForm() {
  // This function deals with validation of the form fields
  var x, y, i, valid = true;
  x = document.getElementsByClassName("tab");
  y = x[currentTab].getElementsByTagName("input");
  // A loop that checks every input field in the current tab:
  for (i = 0; i < y.length; i++) {
    // If a field is empty...
    if (y[i].value == "") {
      // add an "invalid" class to the field:
      y[i].className += " invalid";
      // and set the current valid status to false:
      valid = false;
    }
  }
  // If the valid status is true, mark the step as finished and valid:
  if (valid) {
    document.getElementsByClassName("step")[currentTab].className += " finish";
  }
  return valid; // return the valid status
}

function fixStepIndicator(n) {
  // This function removes the "active" class of all steps...
  var i, x = document.getElementsByClassName("step");
  for (i = 0; i < x.length; i++) {
    x[i].className = x[i].className.replace(" active", "");
  }
  //... and adds the "active" class to the current step:
  x[n].className += " active";
}

$(document).ready(function(){
  $("input.dm1").click(function(){$("fieldset.dm2").addClass("highlight");});
  $("input.dm2").click(function(){$("fieldset.dm3").addClass("highlight");});
  $("input.dm3").click(function(){$("fieldset.dm4").addClass("highlight");});
  $("input.dm4").click(function(){$("fieldset.pa1").addClass("highlight");});

  $("input.pa1").click(function(){$("fieldset.pa2").addClass("highlight");});
  $("input.pa2").click(function(){$("fieldset.pa3").addClass("highlight");});
  $("input.pa3").click(function(){$("fieldset.pa4").addClass("highlight");});
  $("input.pa4").click(function(){$("fieldset.ce1").addClass("highlight");});

  $("input.ce1").click(function(){$("fieldset.ce2").addClass("highlight");});
  $("input.ce2").click(function(){$("fieldset.ce3").addClass("highlight");});
  $("input.ce3").click(function(){$("fieldset.ce4").addClass("highlight");});
  $("input.ce4").click(function(){$("fieldset.cs1").addClass("highlight");});

  $("input.cs1").click(function(){$("fieldset.cs2").addClass("highlight");});
  $("input.cs2").click(function(){$("fieldset.cs3").addClass("highlight");});
  $("input.cs3").click(function(){$("fieldset.cs4").addClass("highlight");});
  $("input.cs4").click(function(){$("fieldset.cs5").addClass("highlight");});
  $("input.cs5").click(function(){$("fieldset.ae1").addClass("highlight");});


  $("input.ae1").click(function(){$("fieldset.ae2").addClass("highlight");});
  $("input.ae2").click(function(){$("fieldset.ae3").addClass("highlight");});
  $("input.ae3").click(function(){$("fieldset.ae4").addClass("highlight");});
  $("input.ae4").click(function(){$("fieldset.ae5").addClass("highlight");});
  $("input.ae5").click(function(){$("fieldset.ae6").addClass("highlight");});


});

$( "#current_college" ).change(function() {
  if($(this).val() == "College of Engineering"){
    $(".plmbs").hide();
    $(".arch").hide();
    $(".ced").hide();
    $(".chass").hide();
    $(".cpt").hide();
    $(".cn").hide();
    $(".cs").hide();
    $(".cet").show();
  }
  else if($(this).val() == "PLM Business School"){
    $(".cet").hide();
    $(".arch").hide();
    $(".ced").hide();
    $(".chass").hide();
    $(".cpt").hide();
    $(".cn").hide();
    $(".cs").hide();
    $(".plmbs").show();
  }
  else if($(this).val() == "College of Architecture and Urban Planning"){
    $(".cet").hide();
    $(".plmbs").hide();
    $(".ced").hide();
    $(".chass").hide();
    $(".cpt").hide();
    $(".cn").hide();
    $(".cs").hide();
    $(".arch").show();
  }
  else if($(this).val() == "College of Education"){
    $(".cet").hide();
    $(".plmbs").hide();
    $(".arch").hide();
    $(".chass").hide();
    $(".cpt").hide();
    $(".cn").hide();
    $(".cs").hide();
    $(".ced").show();
  }
  else if($(this).val() == "College of Humanities, Arts, and Social Sciences"){
    $(".cet").hide();
    $(".plmbs").hide();
    $(".arch").hide();
    $(".ced").hide();
    $(".cpt").hide();
    $(".cn").hide();
    $(".cs").hide();
    $(".chass").show();
  }
  else if($(this).val() == "College of Physical Therapy"){
    $(".cet").hide();
    $(".plmbs").hide();
    $(".arch").hide();
    $(".ced").hide();
    $(".chass").hide();
    $(".cn").hide();
    $(".cs").hide();
    $(".cpt").show();
  }
  else if($(this).val() == "College of Nursing"){
    $(".cet").hide();
    $(".plmbs").hide();
    $(".arch").hide();
    $(".ced").hide();
    $(".chass").hide();
    $(".cpt").hide();
    $(".cs").hide();
    $(".cn").show();
  }
  else if($(this).val() == "College of Science"){
    $(".cet").hide();
    $(".plmbs").hide();
    $(".arch").hide();
    $(".ced").hide();
    $(".chass").hide();
    $(".cpt").hide();
    $(".cn").hide();
    $(".cs").show();
  }
  else if($(this).val() == ""){
    $(".cet").hide();
    $(".plmbs").hide();
    $(".arch").hide();
    $(".ced").hide();
    $(".chass").hide();
    $(".cpt").hide();
    $(".cn").hide();
    $(".cs").hide();
  }
});

// Remove the transition class
const square = document.querySelector('.card-green');
square.classList.remove('square-transition');

// Create the observer, same as before:
const observer = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      square.classList.add('square-transition');
      return;
    }

    square.classList.remove('square-transition');
  });
});

observer.observe(document.querySelector('.square-wrapper'));

