// Task 8.5 - Server for Express

import express from 'express';

// Import the routes used for the server
const routes = require('./routes/index');
// Initializes express
const app = express();

// Uses routes defined
app.use(routes);

// Listens on port 1245
app.listen(1245);

// Exports so that it can be used in other files
export default app;
