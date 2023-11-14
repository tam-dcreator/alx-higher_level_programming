#!/usr/bin/node
// Script that prints the value of one argument if present
const { argv } = require('node:process');
if (argv[2] == null) {
  console.log('No argument');
} else {
  console.log(argv[2]);
}
