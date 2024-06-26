// Task 7 - More compless HTTP server using Express

const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();
const port = 1245;

// Sets route's type to plain text and sends a message
app.get('/', (req, res) => {
  res.type('type/plain');
  res.send('Hello Atlas School');
});

// Sets route's type to plain text and sends Task 3 output
app.get('/students', async (req, res) => {
  try {
    // Grabs the CSV file from user input
    const databasePath = process.argv[2];
    const result = await countStudents(databasePath);

    // Sends Task 3 output
    res.type('type/plain');
    res.status(200).send(`This is the list of students\n${result}`);
  } catch (error) {
    // Catches Status 500
    console.log(error);
    res.status(500).send('Internal Server Error');
  }
});

app.listen(port, () => {
  // Message displayed when server is running
  console.log('It\'s running!');
});
