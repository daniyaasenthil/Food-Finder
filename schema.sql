CREATE DATABASE IF NOT EXISTS food_finder;
USE food_finder;

-- Matches the two columns used by the original Food Finder project.
-- If your existing restaurants table already has these columns, you do not
-- need to recreate it or reinsert your existing data.
CREATE TABLE IF NOT EXISTS restaurants (
    Food VARCHAR(100) NOT NULL,
    Foodchain VARCHAR(150) NOT NULL
);

-- Optional sample rows for a NEW/EMPTY table. Uncomment and edit as needed:
-- INSERT INTO restaurants (Food, Foodchain) VALUES
-- ('Burger', 'Example Burger Cafe'),
-- ('Pizza', 'Example Pizza Place'),
-- ('French Fries', 'Example Snack Corner'),
-- ('Chicken Burger', 'Example Burger Cafe'),
-- ('Pasta', 'Example Italian Kitchen');
