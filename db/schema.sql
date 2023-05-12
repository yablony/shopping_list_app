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
    image_url TEXT 
);

CREATE TABLE fridge_items (
    id SERIAL PRIMARY KEY,
    user_id INTEGER,
    item_name TEXT
);

-- table for testing only, will bechanged to an API
CREATE TABLE recipes (
    id SERIAL PRIMARY KEY,
    name TEXT,
    cooking_time INTEGER,
    image_url TEXT, 
    ingredients TEXT,
    cooking_instructions TEXT
);

INSERT INTO recipes(name, cooking_time, image_url, ingredients, cooking_instructions)
VALUES
  ('Tacos', 90, 'https://images.unsplash.com/photo-1551504734-5ee1c4a1479b?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=870&q=80', 'taco shells, chicken, spices, salsa', 'Step 1, step 2, step 3');

INSERT INTO shopping_list(user_id, item_name, image_url)
VALUES
  (1, 'parsley', 'https://images.unsplash.com/photo-1588879460618-9249e7d947d1?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80');