#!/usr/bin/node

const fs = require('fs');

const [fileA, fileB, fileC] = process.argv.slice(2);

const contentA = fs.readFileSync(fileA, 'utf8');
const contentB = fs.readFileSync(fileB, 'utf8');

const content = `${contentA}\n${contentB}`;
fs.writeFileSync(fileC, content, 'utf8');
