// Promise that resolves with value 3
const resolvePromise = Promise.resolve(3);
resolvePromise.then(value => console.log(value)); // 3

// Promise that rejects with "Boo!"
const rejectPromise = Promise.reject("Boo!");
rejectPromise.catch(error => console.log(error)); // "Boo!"