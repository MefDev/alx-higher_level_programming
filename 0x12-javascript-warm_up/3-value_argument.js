#!/usr/local/bin/node

const [firstArg] = process.argv.slice(2);
firstArg
  ? process.argv.slice(2).forEach((val) => console.log(val))
  : console.log('No argument');
