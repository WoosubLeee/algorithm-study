var fs = require('fs');
var input = fs.readFileSync('1001/input.txt').toString().split(' ');
var a = parseInt(input[0]);
var b = parseInt(input[1]);
console.log(a-b);