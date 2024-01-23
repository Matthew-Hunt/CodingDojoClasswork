
document.getElementById("Burbank").addEventListener("click", cityClick);
document.getElementById("Chicago").addEventListener("click", cityClick);
document.getElementById("Dallas").addEventListener("click", cityClick);
document.querySelector(".cookie-btn").addEventListener("click", acceptClick);
document.querySelector("#temp-selector").addEventListener("change", tempChange);

function cityClick() {
    alert("Loading weather report for " + this.id);
}

function acceptClick() {
    this.parentNode.remove();
}

function tempChange() {

    if (this.value == "fah") {
        document.querySelectorAll(".degree").forEach(item => {
            let c = parseInt(item.innerText, 10);
            let f = ((9 * c) + (32 * 5)) / 5;
            f = Math.round(f);
            item.innerText = f;
        })
    } else {
        document.querySelectorAll(".degree").forEach(item => {
            let f = parseInt(item.innerHTML, 10);
            let c = (5 / 9) * (f - 32);
            c = Math.round(c);
            item.innerText = c;
        })
    }
}