-- Create the database if not exists
CREATE DATABASE IF NOT EXISTS workik_db;

-- Use the database
USE workik_db;

-- Create the auth_tokens table
CREATE TABLE IF NOT EXISTS auth_tokens (
    id INT AUTO_INCREMENT PRIMARY KEY,
    server_id BIGINT NOT NULL UNIQUE,
    token VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);