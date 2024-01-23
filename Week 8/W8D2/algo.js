

function maxMinAvg(arr){
    var max = arr[0];
    var min = arr[0];
    var sum = arr[0];

    for (i = 1; i < arr.length; i++) {
    if(arr[i] > max) {
        max = arr[i];
    } 

    if (arr[i] < min) {
        min = arr[i];
    }
    sum += arr[i];

}
var avg = sum / arr.length;
return [max, min, avg];
}

var result = maxMinAvg([1,5,10,-2]);
console.log(result);