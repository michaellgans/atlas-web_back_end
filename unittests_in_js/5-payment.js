// Task 5 - Hooks

const Utils = require('./utils');

function sendPaymentRequestToApi(totalAmount, totalShipping) {
  // Usis utils to add totalAmount and totalShipping
  const sum = Utils.calculateNumber('SUM', totalAmount, totalShipping);
  console.log(`The total is: ${sum}`);
}

module.exports = sendPaymentRequestToApi;
