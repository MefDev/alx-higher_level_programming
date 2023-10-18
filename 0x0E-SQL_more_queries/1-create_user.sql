-- Create user with  all  privileges
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
GRANT ALL ON *.* TO 'user_0d_1'@'localhost';
ALTER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

