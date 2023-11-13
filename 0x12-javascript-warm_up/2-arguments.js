#!/usr/bin/node

const { argv } = require('node:process');
(argv.length === 2)
  ? console.log('No argument')
  : (argv.length === 3)
      ? console.log('Argument found')
      : console.log('Arguments found');
