// Task 8 - Basic Integration Testing

const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send('Welcome to the payment system');
});

// To be displayed when server is connected
app.listen(7865, () => {
  console.log('API available on localhost port 7865')
});

module.exports = app;
