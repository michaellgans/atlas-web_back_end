// Task 6 - Create a small HTTP server using Express

const express = require('express');

// Names express as app and sets port
const app = express();
const port = 1245;

// Message to send once route is reached
app.get('/', (req, res) => {
  res.send('Hello Atlas School');
});

// Message to send if server is running
app.listen(port, () => {
  console.log('It\'s running!');
});
