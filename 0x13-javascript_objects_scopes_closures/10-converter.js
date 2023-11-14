#!/usr/bin/node

exports.converter = function (base) {
  const convert = (num) => {
    return num.toString(base);
  };
  return convert;
};
