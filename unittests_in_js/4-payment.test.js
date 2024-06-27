// Task 3 - Tests 4-payment.js

const { expect } = require('chai');
const sinon = require('sinon');
const sendPaymentRequestToApi = require('./4-payment.js');
const Utils = require('./utils');

describe('sendPaymentRequestToApi', function() {
  it('calls Utils.calculateNumber to calculate the SUM', function() {
    // Create stub
    const calculateNumberStub = sinon.stub(Utils, 'calculateNumber').returns(10);
    
    // Create spy
    const consoleSpy = sinon.spy(console, 'log');

    // Call function to spy on
    sendPaymentRequestToApi(100, 20);

    // What do you expect the outcome to be?
    expect(calculateNumberStub.calledOnceWithExactly('SUM', 100, 20)).to.be.true;
    expect(consoleSpy.calledOnceWithExactly('The total is: 10')).to.be.true;

    // Remove spy and stub
    calculateNumberStub.restore();
    consoleSpy.restore();
  });
});
