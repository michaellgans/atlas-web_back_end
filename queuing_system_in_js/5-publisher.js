// Task 5 - Node Redis Publisher & Subscriber

import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
    // Displays a message when connected
    console.log('Redis client connected to the server');
});

client.on('error', (err) => {
    // Displays error message when can't connect
    console.error('Redis client not connected to the server:', err);
});

// Publish messages to channel
function publishMessage(message, time) {
    setTimeout(() => {
        console.log(`About to send ${message}`);
        client.publish('holberton school channel', message);
    }, time);
};

// Run these functions
publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);