-- Create Trigger for email validation
DELIMITER $ ;
CREATE
DEFINER=`root`@`localhost`
TRIGGER reset_valid_email
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
  IF NEW.email != OLD.email THEN
    SET New.valid_email = 0;
  END IF;
END;
$
