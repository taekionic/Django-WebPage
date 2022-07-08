

function togglenav() {
    var x = document.getElementById("nav");
    var y = document.getElementById("menuicon")
    var z = document.getElementById("pageblur")

    //selecting our contact form+
      if (x.style.transform == "translateX(-105%)") { //transition for navbar
        x.style.transform = "translateX(0%)"
        x.style.transition = ".75s ease-in-out"
        z.style.backdropFilter = "blur(4px)"
        z.style.transition = ".75s ease-in-out"
        z.style.zIndex = "50"
        y.style.transform = "rotate(90deg)"
      }

      else {
        x.style.transform = "translateX(-105%)"
        x.style.transition = ".75s ease-in"
        z.style.backdropFilter = "blur(0px)"
        z.style.transition = ".75s ease-in-out"
        z.style.zIndex = "50"
        z.style.zIndex = "-2"
        y.style.transform = "rotate(0deg)"
      }
    }


var formbox = document.getElementById("formcontainer")
var formbtn = document.getElementsByClassName("formopen")
var contactme = document.getElementById("formpopup")
var contact = document.getElementById("formopenbutton")


function formdisplay() {
  if (formbox.style.transform == "translateY(100vh)") {
    formbox.style.transform = "translateY(0vh)";
    formbox.style.transition = ".75s ease-in"
    contact.style.transform = "translateX(200px)"
    contact.style.transition = ".5s ease-in-out"
  } else {
    formbox.style.transform = "translateY(100vh)"
    formbox.style.transition = ".75s ease-out"
    contact.style.transform = "translateX(0px)"
    contact.style.transition = ".5s ease-in-out"
  }

}

for (i=0; i < formbtn.length; i++) {
  formbtn[i].addEventListener("click", formdisplay)
}


const months = [
"January",
"February",
"March",
"April",
"May",
"June",
"July",
"August",
"September",
"October",
"November",
"December",
]

function updateTime() {
    var date = new Date();
    var year = date.getFullYear();
    var month = date.getMonth();
    var day = date.getDate();
    var hours = date.getHours()
    var minutes = date.getMinutes()
    var seconds = date.getSeconds()
    if (minutes <10 ){
        minutes = "0" + minutes
    }
    if (seconds <10 ){
        seconds = "0"+ seconds
    }
    var time = hours + ":" + minutes + ":" + seconds + " ";
    if(hours > 11) {
        time += "PM"
    } else {
        time += "AM"
    }
    document.getElementById("time").innerHTML = time;
}
setInterval(updateTime, 1000);