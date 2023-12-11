#!/usr/bin/node
// Script that prints x times "C is fun"
let argVar = parseInt(process.argv[2]);
if (argVar) {
  for (; argVar > 0; argVar--) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
