// Task 2 - Node Redis Client & Basic Ops

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

function setNewSchool(schoolName, value) {
    // Sets the value of School Name key
    client.set(schoolName, value, (err, reply) => {
        if (err) {
            console.error(`Couldn\'t set ${schoolName}:`, err);
        } else {
            // Outputs using redis print instead of console log
            redis.print(`Reply: ${reply}`);
        }
    });
}

function displaySchoolValue(schoolName) {
    // Displays the value of the key
    client.get(schoolName, (err, reply) => {
        console.log(reply);
    });
}

// Call functions
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');