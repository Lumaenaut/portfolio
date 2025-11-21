const input = require('sync-input');

// We have imported the 'sync-input' package for you.
// This package allows you to get user input.
// Like so:
// let name = input("Type your name: ");
// let age = Number(input("Type your age: "));
// You will need it in later stages.

let bubbleG = 202;
let toffee = 118;
let iceC = 2250;
let milkC = 1680;
let doughnut = 1075;
let pancake = 80;
let total = bubbleG + toffee + iceC + milkC + doughnut + pancake;

console.log("Earned amount:");
console.log("Bubblegum: $" + bubbleG);
console.log("Toffee: $" + toffee);
console.log("Ice cream: $" + iceC);
console.log("Milk chocolate: $" + milkC);
console.log("Doughnut: $" + doughnut);
console.log("Pancake: $" + pancake);
console.log("\nIncome: $" + total);

let staffE = Number(input("Staff expenses: "));
let otherE = Number(input("Other expenses: "));

console.log("Net income: " + (total - staffE - otherE));
