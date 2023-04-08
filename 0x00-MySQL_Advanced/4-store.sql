-- Create Trigger to decrease quantity
DELIMITER $ ;
CREATE
DEFINER=`root`@`localhost`
TRIGGER decrease_qty
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
  UPDATE items SET quantity = quantity - NEW.number
  WHERE NEW.item_name = name;
END;
$
