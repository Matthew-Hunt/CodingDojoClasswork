//Print Odds
for (let i = 1; i <= 20; i++) {
    if (i % 2 !== 0) {
        console.log(i);
    }
}

//Decreasing Multiples of 3
for (let t = 100; t >= 0; t--) {
    if (t % 3 === 0) {
        console.log(t);
    }
}

//Print the sequence
const sequence = [4, 2.5, 1, -0.5, -2, -3.5];

for (let s = 0; s < sequence.length; s++) {
    console.log(sequence[s]);
}

//Sigma
let sum = 0;

for (let a = 1; a <= 100; a++) {
    sum += a;
}

console.log(sum);

//Factorial
let product = 1;

for (let p = 1; p <= 12; p++) {
  product *= p;
}

console.log(product);

