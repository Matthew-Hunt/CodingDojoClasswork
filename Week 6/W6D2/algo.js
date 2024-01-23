


function countPositives(arr) {
    var count = 0;
    for (var i = 0; i < arr.length; i++) {
        if (arr[i] > 0) {
            count += arr[i];
        }
    }
    return count
}

myNum = countPositives([-1,1,1,1])

console.log(myNum)