/*******************************
 🌟 EXERCISE 1
*******************************/
function displayNumbersDivisible(divisor = 23) {
  let sum = 0;

  for (let i = 0; i <= 500; i++) {
    if (i % divisor === 0) {
      console.log(i);
      sum += i;
    }
  }

  console.log("Sum:", sum);
}

displayNumbersDivisible();


/*******************************
 🌟 EXERCISE 2
*******************************/
const stock = {
  banana: 6,
  apple: 0,
  pear: 12,
  orange: 32,
  blueberry: 1
};

const prices = {
  banana: 4,
  apple: 2,
  pear: 1,
  orange: 1.5,
  blueberry: 10
};

const shoppingList = ["banana", "orange", "apple"];

function myBill() {
  let total = 0;

  for (let item of shoppingList) {
    if (item in stock && stock[item] > 0) {
      total += prices[item];
      stock[item]--;
    }
  }

  return total;
}

console.log(myBill());


/*******************************
 🌟 EXERCISE 3
*******************************/
function changeEnough(itemPrice, amountOfChange) {
  let [quarters, dimes, nickels, pennies] = amountOfChange;

  let total =
    quarters * 0.25 +
    dimes * 0.1 +
    nickels * 0.05 +
    pennies * 0.01;

  return total >= itemPrice;
}

console.log(changeEnough(4.25, [25, 20, 5, 0]));
console.log(changeEnough(14.11, [2, 100, 0, 0]));


/*******************************
 🌟 EXERCISE 4
*******************************/
function hotelCost() {
  let nights = Number(prompt("How many nights?"));

  while (isNaN(nights) || nights <= 0) {
    nights = Number(prompt("Enter valid nights"));
  }

  return nights * 140;
}

function planeRideCost() {
  let destination = prompt("Where to?");

  while (!destination || !isNaN(destination)) {
    destination = prompt("Enter valid destination");
  }

  destination = destination.toLowerCase();

  if (destination === "london") return 183;
  if (destination === "paris") return 220;
  return 300;
}

function rentalCarCost() {
  let days = Number(prompt("How many days?"));

  while (isNaN(days) || days <= 0) {
    days = Number(prompt("Enter valid days"));
  }

  let cost = days * 40;

  if (days > 10) {
    cost *= 0.95;
  }

  return cost;
}

function totalVacationCost() {
  let hotel = hotelCost();
  let plane = planeRideCost();
  let car = rentalCarCost();

  console.log("Hotel:", hotel);
  console.log("Plane:", plane);
  console.log("Car:", car);

  console.log("Total:", hotel + plane + car);
}

totalVacationCost();


/*******************************
 🌟 EXERCISE 5 (DOM USERS)
*******************************/
const div = document.getElementById("container");
console.log(div);

let lists = document.querySelectorAll(".list");

// change Pete → Richard
lists[0].children[1].textContent = "Richard";

// delete second li of second ul
lists[1].children[1].remove();

// change first li of each ul
for (let ul of lists) {
  ul.firstElementChild.textContent = "Samuel";
}

// add classes
lists.forEach(ul => ul.classList.add("student_list"));
lists[0].classList.add("university", "attendance");

// style div
div.style.backgroundColor = "lightblue";
div.style.padding = "10px";

// hide Dan
lists[0].lastElementChild.style.display = "none";

// border Richard
lists[1].children[0].style.border = "1px solid black";

// font size
document.body.style.fontSize = "20px";

// bonus
if (div.style.backgroundColor === "lightblue") {
  alert("Hello Samuel and Samuel");
}


/*******************************
 🌟 EXERCISE 6 (NAVBAR)
*******************************/
let navBar = document.getElementById("navBar");

// change id
navBar.setAttribute("id", "socialNetworkNavigation");

// create new li
let newLi = document.createElement("li");
newLi.appendChild(document.createTextNode("Logout"));

// add to ul
navBar.firstElementChild.appendChild(newLi);

// first and last li
let ul = navBar.querySelector("ul");

console.log(ul.firstElementChild.textContent);
console.log(ul.lastElementChild.textContent);


/*******************************
 🌟 EXERCISE 7 (BOOK LIST)
*******************************/
const allBooks = [
  {
    title: "Harry Potter",
    author: "J.K. Rowling",
    image: "https://covers.openlibrary.org/b/id/7984916-L.jpg",
    alreadyRead: true
  },
  {
    title: "Atomic Habits",
    author: "James Clear",
    image: "https://covers.openlibrary.org/b/id/11153264-L.jpg",
    alreadyRead: false
  }
];

const section = document.querySelector(".listBooks");

for (let book of allBooks) {
  let div = document.createElement("div");

  div.textContent = `${book.title} written by ${book.author}`;

  let img = document.createElement("img");
  img.src = book.image;
  img.style.width = "100px";

  div.appendChild(document.createElement("br"));
  div.appendChild(img);

  if (book.alreadyRead) {
    div.style.color = "red";
  }

  section.appendChild(div);
}