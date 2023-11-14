#!/usr/bin/node
// Script that prints specific text depending on number of command line
// arguments passed.
const { argv } = require('node:process');
if (argv.length === 3) {
  console.log('Argument found');
} else if (argv.length > 2) {
  console.log('Arguments found');
} else {
  console.log('No argument');
}
