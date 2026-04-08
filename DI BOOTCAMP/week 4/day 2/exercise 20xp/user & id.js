const users = { user1: 18273, user2: 92833, user3: 90315 };

// Part 1: Turn into array of arrays
const usersArray = Object.entries(users);
console.log(usersArray);
// [ [ 'user1', 18273 ], [ 'user2', 92833 ], [ 'user3', 90315 ] ]

// Part 2: Multiply IDs by 2
const doubledUsersArray = usersArray.map(([user, id]) => [user, id * 2]);
console.log(doubledUsersArray);
// [ [ 'user1', 36546 ], [ 'user2', 185666 ], [ 'user3', 180630 ] ]