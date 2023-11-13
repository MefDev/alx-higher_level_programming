#!/usr/bin/node

const c = 'C is fun';

let [firstArg] = process.argv.slice(2);
firstArg = Number(firstArg);
if (isNaN(firstArg) || firstArg === undefined) {
  console.log('Missing number of occurrences');
} else {
  while (firstArg > 0) {
    console.log(c);
    firstArg--;
  }
}
