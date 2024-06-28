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

client.subscribe('holberton school channel');

client.on('message', (channel, message) => {
    if (message === 'KILL_SERVER') {
        client.unsubscribe('holberton school channel');
        client.quit();
    } else {
        console.log(message);
    }
});