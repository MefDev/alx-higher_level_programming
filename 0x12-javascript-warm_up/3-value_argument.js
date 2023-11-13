#!/usr/bin/node

const isArrayEmpty = (arr) => {
  return Array.isArray(arr) && arr.every(() => false);
};

const argvList = process.argv.slice(2);
!isArrayEmpty(argvList)
  ? argvList.forEach((val) => console.log(val))
  : console.log('No argument');
