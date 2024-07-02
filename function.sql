----------------------------------------------------------- FUNCTION CalculateTotalMedicineQuantity------------------------------
DELIMITER //

CREATE FUNCTION CalculateTotalMedicineQuantity()
RETURNS INT
READS SQL DATA
BEGIN
    DECLARE total_quantity INT;

    SELECT SUM(QUANTITY) INTO total_quantity
    FROM MEDICINE;

    RETURN total_quantity;
END //

DELIMITER ;

SELECT CalculateTotalMedicineQuantity() AS TotalQuantity;
----------------------------------------------------------- FUNCTION CalculateTotalMedicineQuantity------------------------------