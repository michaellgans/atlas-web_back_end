// Task 3 - Tests 3-payment.js

const { expect } = require('chai');
const sinon = require('sinon');
const sendPaymentRequestToApi = require('./3-payment.js');
const Utils = require('./utils');

describe('sendPaymentRequestToApi', function() {
  it('calls Utils.calculateNumber to calculate the SUM', function() {
    // Create spy
    const calculateNumberSpy = sinon.spy(Utils, 'calculateNumber');

    // Call function to spy on
    sendPaymentRequestToApi(100, 100);

    // What do you expect the outcome to be?
    expect(calculateNumberSpy.calledOnceWithExactly('SUM', 100, 100)).to.be.true;

    // Remove spy
    calculateNumberSpy.restore();
  });
});
