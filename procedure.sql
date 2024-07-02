----------------------------------------------------------- PROCEDURE CountDeathsBeforeAfter2000------------------------------
DELIMITER //

CREATE PROCEDURE CountDeathsBeforeAfter2000(
    OUT num_before_2000 INT,
    OUT num_after_2000 INT
)
BEGIN
    SELECT COUNT(*) INTO num_before_2000
    FROM DEATHS
    WHERE YEAR(TIME_OF_DEATH) < 2000;

    SELECT COUNT(*) INTO num_after_2000
    FROM DEATHS
    WHERE YEAR(TIME_OF_DEATH) >= 2000;
end
//

DELIMITER ;

SHOW PROCEDURE STATUS WHERE db = 'hospital_db';


CALL CountDeathsBeforeAfter2000(@num_before_2000, @num_after_2000);

SELECT @num_before_2000 AS Deaths_Before_2000, @num_after_2000 AS Deaths_After_2000;
----------------------------------------------------------- PROCEDURE CountDeathsBeforeAfter2000------------------------------