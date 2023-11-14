#!/usr/bin/node

const square = require('./5-square');

class Square extends square {
  constructor (size) {
    super(size, size);
  }

  charPrint (char) {
    let square = '';
    for (let i = 0; i < this.width; i++) {
      (char) ? square += char : square += 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(square);
    }
  }
}
module.exports = Square;
