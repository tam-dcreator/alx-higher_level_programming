#!/usr/bin/node
// Script that prints specific text depending on number of command line
// arguments passed.
const argVar = process.argv;
if (argVar.length === 3) {
  console.log('Argument found');
} else if (argVar.length > 2) {
  console.log('Arguments found');
} else {
  console.log('No argument');
}
