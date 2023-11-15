#!/usr/local/bin/node

const fs = require('fs');

const [fileA, fileB, fileC] = process.argv.slice(2);

const fileContentA = fs.readFileSync(fileA, 'utf8');
const fileContentB = fs.readFileSync(fileB, 'utf8');

const data = fileContentA + fileContentB;
fs.writeFile(fileC, data, err => {
  if (err) throw err;
});
