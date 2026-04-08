function makeAllCaps(words) {
    return new Promise((resolve, reject) => {
        // Check if all elements are strings
        const allStrings = words.every(word => typeof word === 'string');
        
        if (allStrings) {
            resolve(words.map(word => word.toUpperCase()));
        } else {
            reject('Error: Not all items are strings');
        }
    });
}

function sortWords(words) {
    return new Promise((resolve, reject) => {
        if (words.length > 4) {
            resolve(words.sort());
        } else {
            reject('Error: Array length is not greater than 4');
        }
    });
}

// Test 1: Rejects (number in array)
makeAllCaps([1, "pear", "banana"])
    .then(arr => sortWords(arr))
    .then(result => console.log(result))
    .catch(error => console.log(error)); // "Error: Not all items are strings"

// Test 2: Rejects (array length <= 4)
makeAllCaps(["apple", "pear", "banana"])
    .then(arr => sortWords(arr))
    .then(result => console.log(result))
    .catch(error => console.log(error)); // "Error: Array length is not greater than 4"

// Test 3: Resolves and sorts
makeAllCaps(["apple", "pear", "banana", "melon", "kiwi"])
    .then(arr => sortWords(arr))
    .then(result => console.log(result)) // ["APPLE", "BANANA", "KIWI", "MELON", "PEAR"]
    .catch(error => console.log(error));