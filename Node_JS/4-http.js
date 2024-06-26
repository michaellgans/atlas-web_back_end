// Task 4 - Create small HTTP server

const http = require('http');

const app = (req, res) => {
  // Creates HTTP Header: status, content type
  res.writeHead(200, { 'Content-Type': 'text/plain' });

  // Response once connection is made
  res.end('Hello Atlas School!');
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
