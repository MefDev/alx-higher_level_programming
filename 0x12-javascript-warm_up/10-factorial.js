#!/usr/bin/node

const factorial = (num) => {
  if (num < 0) return 1;
  if (num === 1 || num === 0) return 1;
  return num * factorial(num - 1);
};

const [firstArg] = process.argv.slice(2);

if (firstArg === undefined) {
  console.log(1);
} else if (isNaN(Number(firstArg))) {
  console.log(1);
} else {
  const value = factorial(Number(firstArg));
  console.log(value);
}
