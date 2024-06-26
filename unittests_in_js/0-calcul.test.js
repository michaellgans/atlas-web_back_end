// Task 0 - Tests 0-calcul.js

const assert = require('assert');
const calculateNumbers = require('./0-calcul');

describe('calculateNumbers', function() {
  it('should take in two numbers, round them, and return the sum', function() {
    assert.strictEqual(calculateNumbers(2.2, 3.3), 5);
  });
});
