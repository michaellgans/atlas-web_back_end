// Task 3 - Node Redis Client & Basic Ops but Async

import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();

client.on('connect', () => {
    // Displays a message when connected
    console.log('Redis client connected to the server');
});

client.on('error', (err) => {
    // Displays error message when can't connect
    console.error('Redis client not connected to the server:', err);
});

// Promise setup
const getAsync = promisify(client.get).bind(client);

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

// Async Function
async function displaySchoolValue(schoolName) {
    // Displays the value of the key
    try {
        const reply = await getAsync(schoolName);
        console.log(reply);
    } catch (err) {
        console.err(`Couldn\'t get ${schoolName}`)
    }
}

// Call functions
(async () => {
    displaySchoolValue('Holberton');
    setNewSchool('HolbertonSanFrancisco', '100');
    displaySchoolValue('HolbertonSanFrancisco');
})();