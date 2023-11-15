#!/usr/bin/node

const dict = require('./101-data').dict;
const obj = {
};
for (count in dict){
    const occurrences = dict[count];
    if (!obj[occurrences]){
        obj[occurrences] = []
    }
    obj[occurrences].push(count)
}
console.log(obj)
   
