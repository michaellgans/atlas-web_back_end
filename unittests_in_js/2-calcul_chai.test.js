// Task 2 - 2-calcul_chai.js

const { expect } = require('chai');
const calculateNumbers = require('./2-calcul_chai.js');

// Function to be tested
describe('calculateNumbers', function() {
  // Type = SUM
  describe('When type is SUM...', function() {
    it('should round both numbers and add them.', function() {
      expect(calculateNumbers('SUM', 2.2, 3.3)).to.equal(5);
    });
  });

  // Type = SUBTRACT
  describe('When type is SUBTRACT...', function() {
    it('should round both numbers and subtract them.', function() {
      expect(calculateNumbers('SUBTRACT', 5.2, 3.3)).to.equal(2);
    });
  });

  // Type = DIVIDE
  describe('When type is DIVIDE...', function() {
    it('should round both numbers and divide them.', function() {
      expect(calculateNumbers('DIVIDE', 10.3, 2.3)).to.equal(5);
    });

    it('should return Error.', function() {
      expect(calculateNumbers('DIVIDE', 2.2, 0)).to.equal('Error');
    });
  });
});
