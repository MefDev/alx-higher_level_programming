#!/usr/bin/node

const [firstArg] = process.argv.slice(2);
if (firstArg) {
  const num = Math.floor(Number(firstArg));
  (!isNaN(num)) ? console.log(`My number: ${num}`) : console.log('Not a number');
} else {
  console.log('Not a number');
}
