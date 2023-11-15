#!/usr/bin/node

const fs = require('fs');

const [, , fileA, fileB, fileC] = process.argv;

try {
  const contentA = fs.readFileSync(fileA, 'utf8');
  const contentB = fs.readFileSync(fileB, 'utf8');

  const content = `${contentA}\n${contentB}`;

  fs.writeFileSync(fileC, content, 'utf8');
} catch (err) {
  console.error('An error occurred:', err.message);
}
