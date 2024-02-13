#!/usr/bin/node
// Script that prints command line arguments
const { argv } = require('node:process');

if (argv.length === 3) {
  console.log('Argument found');
} else if (argv.length > 3) {
  console.log('Arguments found');
} else {
  console.log('No argument');
}
