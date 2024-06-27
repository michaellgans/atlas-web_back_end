// Task 5 - Tests 5-payment.js

const sinon = require('sinon');
const sendPaymentRequestToApi = require('./5-payment');

describe('sendPaymentRequestToApi', function() {
  let spyConsole;

  beforeEach(function() {
    spyConsole = sinon.spy(console, 'log');
  });

  afterEach(function() {
    spyConsole.restore();
  });

  it('will call sendPaymentRequestToAPI with 100, and 20', function() {
    sendPaymentRequestToApi(100, 20);
    sinon.assert.calledWithExactly(spyConsole, 'The total is: 120');
  });

  it('will call sendPaymentRequestToAPI with 10, and 10', function() {
    sendPaymentRequestToApi(10, 10);
    sinon.assert.calledWithExactly(spyConsole, 'The total is: 20');
  });
});
