#!/usr/bin/node
// Script that prints command line arguments
const argVar = process.argv;

if (argVar.length === 3) {
  console.log('Argument found');
} else if (argVar.length > 2) {
  console.log('Arguments found');
} else {
  console.log('No argument');
}
