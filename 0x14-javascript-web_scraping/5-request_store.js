#!/usr/bin/node

const request = require('request');
const { argv } = require('process');
const fs = require('fs');
const url = argv[2];
const file = argv[3];

const writeData = (body) => {
  fs.writeFile(file, body, 'utf-8', (err) => {
    if (err) throw err;
  });
};
request(url, (error, response, body) => {
  if (error) throw error;
  writeData(body);
});
