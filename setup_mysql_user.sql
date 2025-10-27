-- MySQL User Setup Script for Django Project
-- Run this script after connecting to MySQL as an admin user (root)

-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS custom_drone;

-- Create the user if it doesn't exist (MySQL 8.0+ syntax)
CREATE USER IF NOT EXISTS 'ddeveloper72'@'localhost' IDENTIFIED BY 'MlDnaa@5036089';

-- Grant all privileges on the custom_drone database to the user
GRANT ALL PRIVILEGES ON custom_drone.* TO 'ddeveloper72'@'localhost';

-- Flush privileges to ensure changes take effect
FLUSH PRIVILEGES;

-- Verify the user and database setup
SELECT User, Host FROM mysql.user WHERE User = 'ddeveloper72';
SHOW DATABASES LIKE 'custom_drone';
SHOW GRANTS FOR 'ddeveloper72'@'localhost';

-- Test connection (you can run this manually)
-- mysql -u ddeveloper72 -p custom_drone