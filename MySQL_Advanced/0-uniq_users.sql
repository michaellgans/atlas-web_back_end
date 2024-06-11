-- Task 0: Creates Users Table
CREATE TABLE users(
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
);
