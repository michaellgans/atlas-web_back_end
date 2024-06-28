// Task 4 - Node Redis Advanced Operations

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

client.hset('AtlasSchools', 'Portland', '50', redis.print);
client.hset('AtlasSchools', 'Seattle', '80', redis.print);
client.hset('AtlasSchools', 'New York', '20', redis.print);
client.hset('AtlasSchools', 'Bogota', '20', redis.print);
client.hset('AtlasSchools', 'Cali', '40', redis.print);
client.hset('AtlasSchools', 'Paris', '2', redis.print);

client.hgetall('AtlasSchools', (err, reply) => {
    console.log(reply);
});
