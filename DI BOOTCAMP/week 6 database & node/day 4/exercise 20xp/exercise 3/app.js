const { readFile, writeFile } = require('./fileManager');

readFile('Hello World.txt');
writeFile('Bye World.txt', 'Writing to the file');