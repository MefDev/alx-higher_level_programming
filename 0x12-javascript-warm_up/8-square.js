#!/usr/bin/node

let square = '';

let [firstArg] = process.argv.slice(2);
firstArg = Number(firstArg);
if (isNaN(firstArg) || firstArg === undefined) {
  console.log('Missing size');
} else {
  for (let i = 0; i < firstArg; i++) {
    square += 'X';
  }
  for (let i = 0; i < firstArg; i++) {
    console.log(square);
  }
}
