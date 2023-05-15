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
    item_name TEXT,
);

CREATE TABLE fridge_items (
    id SERIAL PRIMARY KEY,
    user_id INTEGER,
    item_name TEXT
);

INSERT INTO shopping_list(user_id, item_name, image_url)
VALUES
  (1, 'parsley', 'https://images.unsplash.com/photo-1588879460618-9249e7d947d1?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80');