CREATE DATABASE shopping_list_app;
\c shopping_list_app

CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    name TEXT,
    email TEXT,
    password_digest TEXT
);

CREATE TABLE shopping_list (
    id SERIAL PRIMARY KEY,
    user_id INTEGER,
    item_name TEXT
);

CREATE TABLE fridge_items (
    id SERIAL PRIMARY KEY,
    user_id INTEGER,
    item_name TEXT
);