// Task 7 - More compless HTTP server using Express

const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();
const port = 1245;

app.get('/', (req, res) => {
  res.type('type/plain');
  res.send('Hello Atlas School');
});

app.get('/students')

app.listen(port, () => {
  console.log('It\'s running!');
});
