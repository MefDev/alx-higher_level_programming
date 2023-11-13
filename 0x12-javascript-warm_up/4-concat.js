#!/usr/bin/node

const listOfArgs = process.argv.slice(2);

if (listOfArgs.length === 0) {
  console.log(listOfArgs[0] + ' is ' + listOfArgs[1]);
} else if (listOfArgs.length < 2) {
  console.log(listOfArgs[0] + ' is ' + listOfArgs[1]);
} else {
  console.log(`${listOfArgs[0]} is ${listOfArgs[1]}`);
}
