// Task 5 - Create more complex HTTP server

const http = require('http');
const fs = require('fs');
const countStudents = require('./3-read_file_async');

const app = async (req, res) => {
  // Creates HTTP Header: status, content type
  res.writeHead(200, { 'Content-Type': 'text/plain' });

  // Different responses for different routes
  if (req.url === '/') {
    res.end('Hello Atlas School!');
  } else if (req.url === '/students') {
    // Grab path from User Input
    const databasePath = process.argv[2];

    // Try to pull list of students from DB
    try{
      const result = await countStudents(databasePath);
      res.end(`This is the list of our students\n${result}`);
    } catch (error) {
      // Internal Server Error 500
      res.writeHead(500, { 'Content-Type': 'text/plain' });
      res.end('Internal Server Error');
      console.error(error);
    }
  } else {
    // Cannot find the page 404
    res.writeHead(404, { 'Content-Type': 'text/plain' });
    res.end('Not Found');
  }
};

// Create Server
const server = http.createServer(app);

// Define port and host
const port = 1245;
const host = 'localhost';

// Listen for specific port
server.listen(port, host, () => {
  // TEST: prints if server is running
  console.log('It\'s running!!');
});

module.exports = app;
