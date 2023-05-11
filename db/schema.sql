CREATE DATABASE shopping_list_app;
\c shopping_list_app

CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    name TEXT,
    email TEXT,
    password_digest TEXT
);