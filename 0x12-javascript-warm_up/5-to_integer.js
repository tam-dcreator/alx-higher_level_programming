#!/usr/bin/node
// Script that prints `My number: <first argument converted in integer>`
// if the first argument can be converted to an integer:
const argVar = parseInt(process.argv[2]);
if (argVar) {
  console.log('My number: ' + argVar);
} else {
  console.log('Not a number');
}
