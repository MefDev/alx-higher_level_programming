#!/usr/bin/node

const fs = require('fs');
const path = require('node:path');

const [, , fileA, fileB, fileC] = process.argv;

const currentPath = process.cwd();

const filePathA = path.join(currentPath, fileA);
const filePathB = path.join(currentPath, fileB);
const filePathC = path.join(currentPath, fileC);

fs.readFile(filePathA, 'utf8', (err, data) => {
  if (err) console.log(err);
  fs.writeFile(filePathC, `${data}\n`, err => {
    if (err) {
      console.error(err);
    }
  });
});

fs.readFile(filePathB, 'utf8', (err, data) => {
  if (err) console.log(err);
  fs.appendFile(filePathC, data, err => {
    if (err) {
      console.error(err);
    }
  });
});
