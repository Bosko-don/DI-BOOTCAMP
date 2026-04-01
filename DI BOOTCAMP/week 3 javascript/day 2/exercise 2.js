/*******************************
 🌟 EXERCISE 1: RANDOM NUMBER
*******************************/
let randomNum = Math.floor(Math.random() * 100) + 1;
console.log("Random number:", randomNum);

for (let i = 0; i <= randomNum; i++) {
  if (i % 2 === 0) {
    console.log(i);
  }
}


/*******************************
 🌟 EXERCISE 2: CAPITALIZE LETTERS
*******************************/
function capitalize(str) {
  let even = "";
  let odd = "";

  for (let i = 0; i < str.length; i++) {
    if (i % 2 === 0) {
      even += str[i].toUpperCase();
      odd += str[i];
    } else {
      even += str[i];
      odd += str[i].toUpperCase();
    }
  }

  return [even, odd];
}

console.log(capitalize("abcdef"));


/*******************************
 🌟 EXERCISE 3: PALINDROME
*******************************/
function palindrome(str) {
  let reversed = str.split("").reverse().join("");
  return str === reversed;
}

console.log(palindrome("madam")); // true
console.log(palindrome("hello")); // false


/*******************************
 🌟 EXERCISE 4: BIGGEST NUMBER
*******************************/
function biggestNumberInArray(arrayNumber) {
  let max = -Infinity;

  for (let item of arrayNumber) {
    if (typeof item === "number" && item > max) {
      max = item;
    }
  }

  return max === -Infinity ? 0 : max;
}

console.log(biggestNumberInArray([-1, 0, 3, 100, 99, 2, 99]));
console.log(biggestNumberInArray(["a", 3, 4, 2]));
console.log(biggestNumberInArray([]));


/*******************************
 🌟 EXERCISE 5: UNIQUE ELEMENTS
*******************************/
function uniqueElements(arr) {
  return [...new Set(arr)];
}

console.log(uniqueElements([1, 2, 3, 3, 3, 4, 5]));


/*******************************
 🌟 EXERCISE 6: CALENDAR (DOM)
*******************************/
// ⚠️ Make sure your HTML has:
// <div id="calendar"></div>

function createCalendar(year, month) {
  const container = document.getElementById("calendar");

  let table = document.createElement("table");

  let days = ["MO", "TU", "WE", "TH", "FR", "SA", "SU"];

  let header = document.createElement("tr");
  for (let day of days) {
    let th = document.createElement("th");
    th.textContent = day;
    header.appendChild(th);
  }
  table.appendChild(header);

  let date = new Date(year, month - 1, 1);

  let firstDay = (date.getDay() + 6) % 7; // Monday start fix

  let row = document.createElement("tr");

  for (let i = 0; i < firstDay; i++) {
    let td = document.createElement("td");
    td.textContent = ".";
    row.appendChild(td);
  }

  while (date.getMonth() === month - 1) {
    if (row.children.length === 7) {
      table.appendChild(row);
      row = document.createElement("tr");
    }

    let td = document.createElement("td");
    td.textContent = date.getDate();
    row.appendChild(td);

    date.setDate(date.getDate() + 1);
  }

  while (row.children.length < 7) {
    let td = document.createElement("td");
    td.textContent = ".";
    row.appendChild(td);
  }

  table.appendChild(row);
  container.appendChild(table);
}

// Run calendar example
createCalendar(2012, 9);