-- SQL script that creates a users table with id, email, name, and country
-- if table already exists script should not fail
CREATE TABLE IF NOT EXISTS users (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
email VARCHAR(255) NOT NULL UNIQUE, name VARCHAR(255),
country ENUM('US', 'CO', 'TN') NOT NULL);
