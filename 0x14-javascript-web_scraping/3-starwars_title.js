#!/usr/bin/node

const request = require('request');
const { argv } = require('process');
const ID = argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${ID}`;

request(url, function (error, response, body) {
  const { title } = JSON.parse(body);
  console.log(title);
});
