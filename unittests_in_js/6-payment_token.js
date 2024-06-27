// Task 6 - Async Tests

function getPaymentTokenFromAPI(success) {
  return new Promise((resolve, reject) => {
    if (success) {
      resolve({ data: 'Successful response from the API'});
    }
  });
}

module.exports = getPaymentTokenFromAPI;
