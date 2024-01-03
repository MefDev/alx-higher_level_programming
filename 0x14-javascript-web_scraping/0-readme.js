#!/usr/bin/node

const fs = require("fs");
const { argv } = require("process");
const file = argv[2];

fs.readFileSync(file, "utf-8", (err, data) => {
    if (err) {
        console.log(err);
    }
    console.log(data);
    
});
