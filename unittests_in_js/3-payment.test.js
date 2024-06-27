// Task 3 - Tests 3-payment.js

const { expect } = require('chai');
const sinon = require('sinon');
const sendPaymentRequestToApi = require('./3-payment.js');
const Utils = require('./utils');

describe('sendPaymentRequestToApi', function() {
  it('calls Utils.calculateNumbers to calculate the SUM', function() {
    // Create spy
    const calculateNumbersSpy = sinon.spy(Utils, 'calculateNumbers');

    // Call function to spy on
    sendPaymentRequestToApi(100, 100);

    // What do you expect the outcome to be?
    expect(calculateNumbersSpy.calledOnceWithExactly('SUM', 100, 100)).to.be.true;

    // Remove spy
    calculateNumbersSpy.restore();
  });
});
