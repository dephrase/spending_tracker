DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS merchants;
DROP TABLE IF EXISTS tags;
DROP TABLE IF EXISTS users;

CREATE TABLE tags (
    id SERIAL PRIMARY KEY,
    tag_name VARCHAR(255),
    tag_description VARCHAR(255)
);

CREATE TABLE merchants (
    id SERIAL PRIMARY KEY,
    merchant_name VARCHAR(255),
    merchant_description VARCHAR(255)
);

CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    transaction_name VARCHAR(255),
    tag_id SERIAL REFERENCES tags(id),
    merchant_id SERIAL REFERENCES merchants(id),
    amount_spent INT
);

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    user_name VARCHAR(255),
    budget INT
);