-- Create Trigger for email validation
DELIMITER $ ;
CREATE
DEFINER=`root`@`localhost`
TRIGGER reset_valid_email
AFTER UPDATE ON users
FOR EACH ROW
BEGIN
  IF NEW.email <> OLD.email THEN
    UPDATE users SET valid_email = 0 WHERE user_id = NEW.user_id;
  END IF;
END;
$
