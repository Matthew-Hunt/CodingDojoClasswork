
var x = document.getElementById("waves");
document.getElementById("waves").onmouseover = function() {};
document.getElementById("waves").onmouseout = function() {};

waves.controls = true;
function playPause() { 
    if (x.pause){ 
    x.play();
    }
    else {
    x.pause(); 
    } 
}

document.querySelectorAll('#waves').forEach(function(vid) {
    vid.onmouseover = function() {
        this.play();
    }
    vid.onmouseout = function() {
        this.pause();
    }
    })