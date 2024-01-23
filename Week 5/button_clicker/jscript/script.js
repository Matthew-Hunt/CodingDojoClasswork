function logIn(element) {
    if (element.innerHTML == "Login") {
        element.innerHTML = "Logout";
    } else {
        element.innerHTML = "Login";
    }
}

function disappear(element) {
    element.remove();
}
function showAlert() {
alert("Ninja was liked");
}