function myFunction() {
    var x = document.getElementById("mytopnav");
    if (x.className === "topnav") {
      x.className += " responsive";
    } else {
      x.className = "topnav";
    }
  }