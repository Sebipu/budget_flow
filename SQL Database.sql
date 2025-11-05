--Creating DATABASE--
CREATE DATABASE IF NOT EXISTS budget_flow;
USE budget_flow;

CREATE TABLE users
(
    id INT auto_increment PRIMARY KEY,
    username VARCHAR(60) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE expenses
(
    id          INT auto_increment PRIMARY KEY,
    category    VARCHAR(255) NOT NULL,
    amount      DECIMAL(10, 2),
    description VARCHAR(255) NOT NULL,
    month       INT NOT NULL,
    year        INT NOT NULL,
    user_id     INT NOT NULL,

    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Adding user --
USE budget_flow;
INSERT INTO users (username, password) VALUES
('admin', 'admin')
SELECT * FROM users
