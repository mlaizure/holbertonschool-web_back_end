-- SQL script that creates a trigger to decrease quantity of item after
-- a new order is added
CREATE TRIGGER dec_amt AFTER INSERT ON orders FOR EACH ROW UPDATE items
SET quantity = quantity - NEW.number WHERE items.name = NEW.item_name;
