import { people } from './data.js';

function averageAge(arr) {
  const total = arr.reduce((sum, person) => sum + person.age, 0);
  const avg = total / arr.length;
  console.log("Average age:", avg);
}

averageAge(people);