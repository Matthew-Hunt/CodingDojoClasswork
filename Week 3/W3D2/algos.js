// # given an array with multiple values, write a 
// function that replaces each value in the array
// with the product of the original value multiplied
//by itself (e.g. [1,5,10,-1] will become [1,25,100,4])

//Pseudo Code

//Arr Varibale - Done
//Function - Done
//console.log
//for loop iterate thru array

var arr = [1,5,10,-2]


function squareVal(arr){
    for(i = 0; i < arr.length; i++){
        //arr[i] = arr[i] * arr[i]
        arr[i] *= arr[i]
        console.log(arr[i]);
    }
    return arr
}

console.log(squareVal([1, 5, 10, -2]))