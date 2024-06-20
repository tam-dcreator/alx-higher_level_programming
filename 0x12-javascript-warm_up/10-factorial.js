#!/usr/bin/node
// Script that computes and prints a factorial
function factorial (a) {
  if (isNaN(a) || a < 2) {
    return (1);
  }
  return (a * factorial(a - 1));
}
const numb = parseInt(process.argv[2]);
const result = factorial(numb);
console.log(result);
