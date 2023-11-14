#!/usr/bin/node
// Script that prints the value of one argument if present
const argVar = process.argv;
if (argVar[2] == null || argVar[3] == null) {
  console.log('No argument');
} else {
  console.log(argVar[2] + ' is ' + argVar[3]);
}
