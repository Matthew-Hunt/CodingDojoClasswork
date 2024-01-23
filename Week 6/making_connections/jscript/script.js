console.log("page loaded...");

var connections = 2
var new_user1 = document.querySelector('.new_user1')
var new_user2 = document.querySelector('.new_user2')
var num = document.querySelector('.badge')
var addNum = document.querySelector('.badge2')
var addConnections = 500


function accept1() {
    new_user1.remove()
    connections--
    console.log(connections)
    num.innerText = connections
    addConnections++
    console.log(addConnections);
    addNum.innerText = addConnections
}
function accept2() {
    new_user2.remove()
    connections--
    console.log(connections)
    num.innerText = connections
    addConnections++
    console.log(addConnections);
    addNum.innerText = addConnections
}
function deny1() {
    new_user1.remove()
    connections--
    console.log(connections)
    num.innerText = connections
}
function deny2() {
    new_user2.remove()
    connections--
    console.log(connections)
    num.innerText = connections
}

function nameChange() {
    document.querySelector('#name1').innerText = "George Clinton"
}