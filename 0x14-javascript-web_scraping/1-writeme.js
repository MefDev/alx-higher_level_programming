#!/usr/bin/node

const fs = require('fs');
const { argv } = require('process');
const fileName = argv[2];
const content = argv[3];

fs.writeFile(fileName, content, 'utf8', (err) => {
  if (err) throw err;
});
