CREATE DATABASE hospital_DB;

USE hospital_DB;

----------------------------------------------------------- PATIENTS table ------------------------------

-- DROP TABLE IF EXISTS patients;
CREATE TABLE IF NOT EXISTS PATIENTS
(
	ID VARCHAR(36) PRIMARY KEY,
	FIRST_NAME VARCHAR(200) NOT NULL,
	LAST_NAME VARCHAR(200) NOT NULL,
	EMAIL VARCHAR(200) NOT NULL,
	PHONE VARCHAR(20) NOT NULL,
	ELECTRONIC_CABINET_ID VARCHAR(36),
    INSURANCE_NUMBER VARCHAR(36),
    WARD_ID INT
--     FOREIGN KEY (ELECTRONIC_CABINET_ID) REFERENCES ELECTRONIC_CABINET(ID),
--     FOREIGN KEY (WARD_ID) REFERENCES WARD(ID)
);

ALTER TABLE PATIENTS
COMMENT = "Table to store PATIENTS' information";

ALTER TABLE PATIENTS
MODIFY COLUMN ID VARCHAR(36) COMMENT 'Unique identifier for each PATIENT',
MODIFY COLUMN FIRST_NAME VARCHAR(200) NOT NULL COMMENT 'First name of the PATIENT',
MODIFY COLUMN LAST_NAME VARCHAR(200) NOT NULL COMMENT 'Last name of the PATIENT',
MODIFY COLUMN EMAIL VARCHAR(200) NOT NULL COMMENT 'Email address of the PATIENT',
MODIFY COLUMN PHONE VARCHAR(20) NOT NULL COMMENT 'Phone number of the PATIENT',
MODIFY COLUMN ELECTRONIC_CABINET_ID VARCHAR(36) COMMENT 'THE NUMBER OF ELECTRONIC CABINET OF A PATIENT',
MODIFY COLUMN INSURANCE_NUMBER VARCHAR(36) COMMENT 'INSURANCE NUMBER OF A PATIENT',
MODIFY COLUMN WARD_ID INT COMMENT 'WARD OF THE PATIENT'


select * from patients;

-- побачити коменти
SELECT column_name, column_comment
FROM information_schema.columns
WHERE table_name = 'PATIENTS';

----------------------------------------------------------- PATIENTS table ------------------------------

----------------------------------------------------------- DOCTORS table ------------------------------

-- DROP TABLE IF EXISTS DOCTORS;
drop table DOCTORS;
CREATE TABLE IF NOT EXISTS DOCTORS
(
	ID VARCHAR(36) PRIMARY KEY,
	FIRST_NAME VARCHAR(200) NOT NULL,
	LAST_NAME VARCHAR(200) NOT NULL,
	EMAIL VARCHAR(200) NOT NULL,
	PHONE VARCHAR(20) NOT NULL,
--	DEPARTMENT_ID VARCHAR(36),
    ROOM_ID VARCHAR(36),
    SPECIALIZATION VARCHAR(200)
  --  FOREIGN KEY (DEPARTMENT_ID) REFERENCES DEPARTMENTS(ID)
--     FOREIGN KEY (ROOM_ID) REFERENCES ROOMS(ID)
);

ALTER TABLE DOCTORS
COMMENT = "Table to store DOCTORS' information";

ALTER TABLE DOCTORS
MODIFY COLUMN ID VARCHAR(36) COMMENT 'Unique identifier for each DOCTOR',
MODIFY COLUMN FIRST_NAME VARCHAR(200) NOT NULL COMMENT 'First name of the DOCTORS',
MODIFY COLUMN LAST_NAME VARCHAR(200) NOT NULL COMMENT 'Last name of the DOCTORS',
MODIFY COLUMN EMAIL VARCHAR(200) NOT NULL COMMENT 'Email address of the DOCTORS',
MODIFY COLUMN PHONE VARCHAR(20) NOT NULL COMMENT 'Phone number of the DOCTORS',
MODIFY COLUMN DEPARTMENT_ID VARCHAR(36) COMMENT 'DOCTOR DEPARTMENT ID',
MODIFY COLUMN ROOM_ID VARCHAR(36) COMMENT 'DOCTOR ROOM ID',
MODIFY COLUMN SPECIALIZATION VARCHAR(200) COMMENT 'DOCTOR SPECIALIZATION'


select * from DOCTORS;

-- побачити коменти
SELECT column_name, column_comment
FROM information_schema.columns
WHERE table_name = 'DOCTORS';

----------------------------------------------------------- DOCTORS table ------------------------------

----------------------------------------------------------- DOCTORS-DEPARTMENTS RELATIONSHIP table ------------------------------

-- проміжна таблиця між лікарями та департаментами, щоб не було взаємопосилань
CREATE TABLE IF NOT EXISTS DOCTOR_DEPARTMENT (
    DOCTOR_ID VARCHAR(36),
    DEPARTMENT_ID VARCHAR(36),
    MAIN_DOCTOR BOOLEAN DEFAULT FALSE,
    PRIMARY KEY (DOCTOR_ID, DEPARTMENT_ID),
    FOREIGN KEY (DOCTOR_ID) REFERENCES DOCTORS(ID),
    FOREIGN KEY (DEPARTMENT_ID) REFERENCES DEPARTMENTS(ID)
);

ALTER TABLE doctor_department
COMMENT = "Table to CREATE RELATIONSHIP BETWEEN DEPARTMENTS AND DOCTORS";

ALTER TABLE doctor_department
MODIFY COLUMN DOCTOR_ID VARCHAR(36) COMMENT 'Unique identifier for each DOCTOR',
MODIFY COLUMN DEPARTMENT_ID VARCHAR(36) COMMENT 'Unique identifier for each department',
MODIFY COLUMN MAIN_DOCTOR BOOLEAN DEFAULT FALSE COMMENT 'SHOWS WHETHER THE DOCTOR IS THE MAIN DOCTOR IN THE DEPARTMENT'

select * from doctor_department;

-- побачити коменти
SELECT column_name, column_comment
FROM information_schema.columns
WHERE table_name = 'doctor_department';

----------------------------------------------------------- DOCTORS-DEPARTMENTS RELATIONSHIP table ------------------------------

----------------------------------------------------------- DEPARTMENTS table ------------------------------

-- DROP TABLE IF EXISTS DEPARTMENTS;
drop table departments;
CREATE TABLE IF NOT EXISTS DEPARTMENTS
(
	ID VARCHAR(36) PRIMARY KEY,
    DEPARTMENT_TYPE VARCHAR(200)
--    MAIN_DOCTOR_ID VARCHAR(36)
   -- FOREIGN KEY (MAIN_DOCTOR_ID) REFERENCES DOCTORS(ID)
);

ALTER TABLE departments
COMMENT = "Table to store departments' information";

ALTER TABLE departments
MODIFY COLUMN ID VARCHAR(36) COMMENT 'Unique identifier for each departments',
MODIFY COLUMN  DEPARTMENT_TYPE VARCHAR(200) COMMENT 'TYPE OF EACH DEPARTMENT'


select * from departments;

-- побачити коменти
SELECT column_name, column_comment
FROM information_schema.columns
WHERE table_name = 'departments';

----------------------------------------------------------- DEPARTMENTS table ------------------------------