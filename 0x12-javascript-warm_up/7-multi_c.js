#!/usr/bin/node

const c = 'C is fun';

let [firstArg] = process.argv.slice(2);
if (firstArg){
    firstArg = Number(firstArg)
    if (isNaN(firstArg)){
        console.log('Missing number of occurrences')
    }
    else {
        while (firstArg > 0){
            console.log(c)
            firstArg--;
        }
    }
}
else{
    console.log('Missing number of occurrences')
}