----------------------------------------------------------- VIEW  Main_DoctorsView------------------------------
CREATE INDEX idx_main_doctor ON DOCTOR_DEPARTMENT (MAIN_DOCTOR);
CREATE INDEX idx_doctor_id ON DOCTOR_DEPARTMENT (DOCTOR_ID);
CREATE INDEX idx_department_id ON DOCTOR_DEPARTMENT (DEPARTMENT_ID);

CREATE VIEW Main_DoctorsView AS
SELECT
    -- dd.DOCTOR_ID,
    d.first_name AS Doctor_First_Name,
    d.last_name AS Doctor_Last_Name,
    -- d.email AS Doctor_Email,
    d.phone AS Doctor_Phone,
    d.SPECIALIZATION AS Doctor_Specialization,
    -- d.ROOM_ID AS Doctor_Room_ID,
    -- dd.DEPARTMENT_ID,
    dep.DEPARTMENT_TYPE AS Department_Name
FROM DOCTOR_DEPARTMENT dd
JOIN DOCTORS d ON dd.DOCTOR_ID = d.id
JOIN DEPARTMENTS dep ON dd.DEPARTMENT_ID = dep.ID
WHERE dd.MAIN_DOCTOR = TRUE;


select * from Main_DoctorsView;
----------------------------------------------------------- VIEW  Main_DoctorsView------------------------------

----------------------------------------------------------- VIEW  NonExpired_Medicine_View------------------------------
CREATE VIEW NonExpired_Medicine_View AS
SELECT *
FROM MEDICINE
WHERE EXPIRATION_DATE >= '2024-06-20';

select * from NonExpired_Medicine_View;
----------------------------------------------------------- VIEW  NonExpired_Medicine_View------------------------------

----------------------------------------------------------- VIEW  Doctors_WithNoDeaths------------------------------
CREATE VIEW Doctors_WithNoDeaths AS
SELECT d.ID, d.first_name, d.last_name, d.phone, d.SPECIALIZATION
FROM DOCTORS d
LEFT JOIN DEATHS dt ON d.ID = dt.DOCTOR_ID
WHERE dt.ID IS NULL;

select * from Doctors_WithNoDeaths;
----------------------------------------------------------- VIEW  Doctors_WithNoDeaths------------------------------