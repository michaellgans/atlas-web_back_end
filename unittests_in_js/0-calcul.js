// Task 0 - Basic Tests with Mocha and Node

function calculateNumbers(a, b) {
  // Takes in two numbers, rounds them, sums them
  const numA = Math.round(a);
  const numB = Math.round(b);

  return numA + numB;
}

module.exports = calculateNumbers;
