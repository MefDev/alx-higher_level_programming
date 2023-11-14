#!/usr/local/bin/node

const dict = require('./101-data').dict;
const list = [89, 90, 91, 92, 93, 94];
const obj = {
  1: [],
  2: [],
  3: []
};
for (let i = 0; i < list.length; i++) {
  if (dict[list[i]] === 1) {
    obj['1'].push(list[i]);
  } else if (dict[list[i]] === 2) {
    obj['2'].push(list[i]);
  } else {
    obj['3'].push(list[i]);
  }
}
