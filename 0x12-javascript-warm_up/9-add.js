#!/usr/bin/node

let [firstNum, lastNum] = process.argv.slice(2);

const add = (a, b) => console.log(a + b);
firstNum = Number(firstNum);
lastNum = Number(lastNum);
add(firstNum, lastNum);
