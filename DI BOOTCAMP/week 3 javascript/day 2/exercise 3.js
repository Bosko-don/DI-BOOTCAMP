// ============================================
// JAVASCRIPT EXERCISES - COMPLETE SOLUTION
// Variables, Conditionals, Loops, Functions, DOM
// ============================================

// ============================================
// EXERCISE 1: is_Blank
// Check whether a string is blank or not
// ============================================

function isBlank(str) {
    // A string is blank if it's empty or contains only whitespace
    return str === null || str === undefined || str.trim() === '';
}

// Test Exercise 1
console.log("=== Exercise 1: isBlank ===");
console.log(isBlank(''));        // true
console.log(isBlank('abc'));     // false
console.log(isBlank('   '));     // true (whitespace only)
console.log("");

// ============================================
// EXERCISE 2: Abbrev_name
// Convert a string into abbreviated form
// ============================================

function abbrevName(name) {
    // Split the name by spaces
    const parts = name.split(' ');
    
    // If there's only one name, return it as is
    if (parts.length === 1) {
        return name;
    }
    
    // Get the first name
    const firstName = parts[0];
    
    // Get the first letter of the last name and add a dot
    const lastInitial = parts[parts.length - 1][0] + '.';
    
    return firstName + ' ' + lastInitial;
}

// Test Exercise 2
console.log("=== Exercise 2: abbrevName ===");
console.log(abbrevName("Robin Singh"));      // "Robin S."
console.log(abbrevName("John Doe Smith"));   // "John S."
console.log(abbrevName("Madonna"));          // "Madonna"
console.log("");

// ============================================
// EXERCISE 3: SwapCase
// Swap the case of each character in a string
// ============================================

function swapCase(str) {
    let result = '';
    
    for (let i = 0; i < str.length; i++) {
        const char = str[i];
        
        // Check if character is uppercase
        if (char === char.toUpperCase()) {
            // Convert to lowercase
            result += char.toLowerCase();
        } else {
            // Convert to uppercase
            result += char.toUpperCase();
        }
    }
    
    return result;
}

// Test Exercise 3
console.log("=== Exercise 3: swapCase ===");
console.log(swapCase('The Quick Brown Fox')); 
// Output: 'tHE qUICK bROWN fOX'
console.log(swapCase('Hello World'));          
// Output: 'hELLO wORLD'
console.log("");

// ============================================
// EXERCISE 4: Omnipresent value
// Check if a value exists in every subarray
// ============================================

function isOmnipresent(arr, value) {
    // Use every() to check if the value exists in ALL subarrays
    return arr.every(subArray => subArray.includes(value));
}

// Alternative solution using a loop:
function isOmnipresentLoop(arr, value) {
    for (let i = 0; i < arr.length; i++) {
        // If the value is NOT in this subarray, return false
        if (!arr[i].includes(value)) {
            return false;
        }
    }
    // If we made it through all subarrays, return true
    return true;
}

// Test Exercise 4
console.log("=== Exercise 4: isOmnipresent ===");
console.log(isOmnipresent([[1, 1], [1, 3], [5, 1], [6, 1]], 1));  // true
console.log(isOmnipresent([[1, 1], [1, 3], [5, 1], [6, 1]], 6));  // false
console.log(isOmnipresent([[3, 4], [8, 3, 2], [3], [9, 3], [5, 3], [4, 3]], 3)); // true
console.log("");

// ============================================
// EXERCISE 5: Red Table (DOM Manipulation)
// Color all diagonal table cells in red
// ============================================

/*
HTML STRUCTURE TO USE WITH EXERCISE 5:

<!DOCTYPE HTML>
<html>
<head>
  <style>
    table {
      border-collapse: collapse;
    }
    td {
      border: 1px solid black;
      padding: 3px 5px;
    }
    .red {
      background-color: red;
      color: white;
    }
  </style>
</head>

<body>
  <table>
    <tr>
      <td>1:1</td>
      <td>2:1</td>
      <td>3:1</td>
      <td>4:1</td>
      <td>5:1</td>
    </tr>
    <tr>
      <td>1:2</td>
      <td>2:2</td>
      <td>3:2</td>
      <td>4:2</td>
      <td>5:2</td>
    </tr>
    <tr>
      <td>1:3</td>
      <td>2:3</td>
      <td>3:3</td>
      <td>4:3</td>
      <td>5:3</td>
    </tr>
    <tr>
      <td>1:4</td>
      <td>2:4</td>
      <td>3:4</td>
      <td>4:4</td>
      <td>5:4</td>
    </tr>
    <tr>
      <td>1:5</td>
      <td>2:5</td>
      <td>3:5</td>
      <td>4:5</td>
      <td>5:5</td>
    </tr>
  </table>
  <script src="exercises.js"></script>
</body>
</html>

*/

// Function to color diagonal cells red
function colorDiagonalRed() {
    // Get the table (first element in body)
    let table = document.body.firstElementChild;
    
    // Get all rows in the table
    let rows = table.rows;
    
    // Loop through each row
    for (let i = 0; i < rows.length; i++) {
        // Get the cells in the diagonal position (i-th cell in i-th row)
        // Diagonal cells are where row index equals cell index
        let diagonalCell = rows[i].cells[i];
        
        // Color the diagonal cell red
        diagonalCell.style.backgroundColor = 'red';
        diagonalCell.style.color = 'white';
    }
}

// Alternative: More flexible version that works with any table size
function colorDiagonalRedAlternative() {
    let table = document.body.firstElementChild;
    let rows = table.rows;
    
    // Loop through rows
    for (let rowIndex = 0; rowIndex < rows.length; rowIndex++) {
        let cells = rows[rowIndex].cells;
        
        // Loop through cells in this row
        for (let cellIndex = 0; cellIndex < cells.length; cellIndex++) {
            // If row index equals cell index, it's a diagonal cell
            if (rowIndex === cellIndex) {
                cells[cellIndex].style.backgroundColor = 'red';
                cells[cellIndex].style.color = 'white';
            }
        }
    }
}

// Run the diagonal coloring when the page loads
// Uncomment the line below when using with HTML:
// colorDiagonalRed();

// ============================================
// COMPLETE HTML FILE FOR EXERCISE 5
// Save this as index.html and open in browser
// ============================================

/*
<!DOCTYPE HTML>
<html>
<head>
  <meta charset="UTF-8">
  <title>Red Diagonal Table</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      display: flex;
      justify-content: center;
      align-items: center;
      min-height: 100vh;
      margin: 0;
      background-color: #f0f0f0;
    }
    
    table {
      border-collapse: collapse;
      background-color: white;
      box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    td {
      border: 1px solid #333;
      padding: 15px 20px;
      text-align: center;
      font-weight: bold;
      transition: all 0.3s ease;
    }
    
    td:hover {
      transform: scale(1.1);
    }
  </style>
</head>

<body>
  <table>
    <tr>
      <td>1:1</td>
      <td>2:1</td>
      <td>3:1</td>
      <td>4:1</td>
      <td>5:1</td>
    </tr>
    <tr>
      <td>1:2</td>
      <td>2:2</td>
      <td>3:2</td>
      <td>4:2</td>
      <td>5:2</td>
    </tr>
    <tr>
      <td>1:3</td>
      <td>2:3</td>
      <td>3:3</td>
      <td>4:3</td>
      <td>5:3</td>
    </tr>
    <tr>
      <td>1:4</td>
      <td>2:4</td>
      <td>3:4</td>
      <td>4:4</td>
      <td>5:4</td>
    </tr>
    <tr>
      <td>1:5</td>
      <td>2:5</td>
      <td>3:5</td>
      <td>4:5</td>
      <td>5:5</td>
    </tr>
  </table>
  
  <script>
    // EXERCISE 5 SOLUTION - Color diagonal cells red
    let table = document.body.firstElementChild;
    let rows = table.rows;
    
    for (let i = 0; i < rows.length; i++) {
      // Color the diagonal cell (where row index = column index)
      let diagonalCell = rows[i].cells[i];
      diagonalCell.style.backgroundColor = 'red';
      diagonalCell.style.color = 'white';
      diagonalCell.style.fontSize = '1.2em';
    }
    
    // Log success message
    console.log("Diagonal cells colored red successfully!");
  </script>
</body>
</html>
*/

// ============================================
// BONUS: All exercises in interactive version
// Run this in browser console or Node.js
// ============================================

console.log(" All exercises loaded successfully!");
console.log("Test them by calling the functions:");
console.log("- isBlank('')");
console.log("- abbrevName('Your Name')");
console.log("- swapCase('Hello World')");
console.log("- isOmnipresent([[1,2],[1,3]], 1)");