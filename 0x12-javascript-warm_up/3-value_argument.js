#!/usr/bin/node

const [firstArg] = process.argv.slice(2);
firstArg
  ? console.log(firstArg)
  : console.log('No argument');
