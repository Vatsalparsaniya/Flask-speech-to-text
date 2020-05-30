function myFunction() {
    var x = document.getElementById("myFootnav");
    if (x.className === "footnov") {
      x.className += " responsive";
    } else {
      x.className = "footnov";
    }
  }