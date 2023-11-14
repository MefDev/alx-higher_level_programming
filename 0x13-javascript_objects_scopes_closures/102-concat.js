#!/usr/bin/node

const fs = require('fs');
const path = require('path');
const readline = require('readline');

const [fileA, fileB, fileC] = process.argv.slice(2);

const currentPath = process.cwd();

const filePathA = path.join(currentPath, fileA);
const filePathB = path.join(currentPath, fileB);
const filePathC = path.join(currentPath, fileC);

const readerA = readline.createInterface({
  input: fs.createReadStream(filePathA),
  output: process.stdout,
  terminal: false
});

readerA.on('line', line => {
  fs.appendFileSync(filePathC, `${line}\n`, 'utf8');
});

readerA.on('close', () => {
  const readerB = readline.createInterface({
    input: fs.createReadStream(filePathB),
    output: process.stdout,
    terminal: false
  });
  readerB.on('line', line => {
    fs.appendFileSync(filePathC, `${line}`, 'utf8');
  });

  readerB.on('close', () => {

  });
});
