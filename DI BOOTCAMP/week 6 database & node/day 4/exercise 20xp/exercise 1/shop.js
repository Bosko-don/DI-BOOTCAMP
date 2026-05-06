const products = require('./products');

function findProduct(productName) {
  const product = products.find(p => p.name.toLowerCase() === productName.toLowerCase());

  if (product) {
    console.log("Product found:", product);
  } else {
    console.log("Product not found");
  }
}

// Test
findProduct("Laptop");
findProduct("Shoes");
findProduct("TV");