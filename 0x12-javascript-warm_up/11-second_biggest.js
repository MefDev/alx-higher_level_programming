#!/usr/bin/node

let listOfArgs = process.argv.slice(2);
listOfArgs = listOfArgs.map(e => Number(e));
if (listOfArgs.length === 0) {
  console.log(0);
} else if (listOfArgs.length === 1) {
  console.log(0);
} else {
  const max = Math.max(...listOfArgs);
  const index = listOfArgs.indexOf(max);
  const secondMax = Math.max(...listOfArgs.slice(0, index), ...listOfArgs.slice(index + 1));
  console.log(secondMax);
}
