//console.log("stuff")

function disappear(element) {
    element.remove();
}

let likeCount1 = 68;
let likeNum1 = document.querySelector(".num1");

function heart1(){
    likeCount1++;
    likeNum1.innerText = likeCount1 
}

let likeCount2 = 212;
let likeNum2 = document.querySelector(".num2");

function heart2(){
    likeCount2++;
    likeNum2.innerText = likeCount2 
}

let likeCount3 = 33;
let likeNum3 = document.querySelector(".num3");

function heart3(){
    likeCount3++;
    likeNum3.innerText = likeCount3 
}

const searchInput = document.querySelector('#search-bar');

searchInput.addEventListener('change', (event) => {
    const searchValue = event.target.value;
    alert(`You are searching for "${searchValue}"`);
});
