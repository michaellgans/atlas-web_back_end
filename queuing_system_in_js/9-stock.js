// Task 9 - Checking Stock

import express from 'express';
import redis from 'redis';
import { promisify } from 'util';

// Initializes Express
const app = express();
const port = 1245;

// List of products that are in stock from a company
const listProducts = [
    {id: 1, name: 'Suitcase 250', price: 50, stock: 4},
    {id: 1, name: 'Suitcase 250', price: 50, stock: 4},
    {id: 1, name: 'Suitcase 250', price: 50, stock: 4},
    {id: 1, name: 'Suitcase 250', price: 50, stock: 4}
];

// Grabs item by the ID number
function getItemByID(id) {
    return listProducts;
}

// Create express Server

// GET route /list_products
app.get('/list_products', (req, res) => {
    res.send('Reached list products page');
});

// What is in stock?
function reserveStockByID(itemID, stock) {
    client.set(item.ITEM_ID, value, (err, reply) => {
        if (err) {
            console.error(`Couldn\'t set ${item.ITEM_ID}:`, err);
        } else {
            // Outputs using redis print instead of console log
            redis.print(`Reply: ${reply}`);
        }
    });
};

// GET route /list_products/:itemId
app.get('/list_products:itemId', (req, res, itemId) => {
    res.send('Reached list products page');
});

// GET route /reserve_products/:itemId
app.get('/reserve_products:itemId', (req, res, itemId) => {
    res.send('Reached list products page');
});