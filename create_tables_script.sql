CREATE DATABASE hospital_DB;

USE hospital_DB;

-- заповнено
 DROP TABLE IF EXISTS patients;
CREATE TABLE IF NOT EXISTS PATIENTS
(
	ID VARCHAR(36) PRIMARY KEY,
	FIRST_NAME VARCHAR(200) NOT NULL,
	LAST_NAME VARCHAR(200) NOT NULL,
	EMAIL VARCHAR(200) NOT NULL,
	PHONE VARCHAR(20) NOT NULL,
    INSURANCE_NUMBER VARCHAR(36),
    WARD_ID varchar(36),
    FOREIGN KEY (WARD_ID) REFERENCES WARDS(ID)
);

ALTER TABLE PATIENTS
COMMENT = "Table to store PATIENTS' information";

ALTER TABLE PATIENTS
MODIFY COLUMN ID VARCHAR(36) COMMENT 'Unique identifier for each PATIENT',
MODIFY COLUMN FIRST_NAME VARCHAR(200) NOT NULL COMMENT 'First name of the PATIENT',
MODIFY COLUMN LAST_NAME VARCHAR(200) NOT NULL COMMENT 'Last name of the PATIENT',
MODIFY COLUMN EMAIL VARCHAR(200) NOT NULL COMMENT 'Email address of the PATIENT',
MODIFY COLUMN PHONE VARCHAR(20) NOT NULL COMMENT 'Phone number of the PATIENT',
MODIFY COLUMN INSURANCE_NUMBER VARCHAR(36) COMMENT 'INSURANCE NUMBER OF A PATIENT',
MODIFY COLUMN WARD_ID varchar(36) COMMENT 'WARD OF THE PATIENT'


select * from patients;

-- побачити коменти
SELECT column_name, column_comment
FROM information_schema.columns
WHERE table_name = 'PATIENTS';

----------------------------------------------------------- DOCTORS table ------------------------------
-- заповнено
-- DROP TABLE IF EXISTS DOCTORS;
drop table DOCTORS;
CREATE TABLE IF NOT EXISTS DOCTORS
(
	ID VARCHAR(36) PRIMARY KEY,
	FIRST_NAME VARCHAR(200) NOT NULL,
	LAST_NAME VARCHAR(200) NOT NULL,
	EMAIL VARCHAR(200) NOT NULL,
	PHONE VARCHAR(20) NOT NULL,
    ROOM_ID VARCHAR(36),
    SPECIALIZATION VARCHAR(200),
    foreign key (ROOM_ID) references ROOMS(ID)
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

----------------------------------------------------------- DOCTORS table end------------------------------

----------------------------------------------------------- DOCTORS-DEPARTMENTS RELATIONSHIP table start------------------------------
-- заповнено

-- проміжна таблиця між лікарями та департаментами, щоб не було взаємопосилань
drop table doctor_department ;
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

----------------------------------------------------------- DOCTORS-DEPARTMENTS RELATIONSHIP table end------------------------------

----------------------------------------------------------- DEPARTMENTS table start------------------------------
-- заповнено
-- DROP TABLE IF EXISTS DEPARTMENTS;
drop table departments;
CREATE TABLE IF NOT EXISTS DEPARTMENTS
(
	ID VARCHAR(36) PRIMARY KEY,
    DEPARTMENT_TYPE VARCHAR(200)

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

----------------------------------------------------------- DEPARTMENTS table end------------------------------

----------------------------------------------------------- ROOMS table start------------------------------
-- заповнено

-- DROP TABLE IF EXISTS ROOMS;

CREATE TABLE IF NOT EXISTS ROOMS
(
	ID VARCHAR(36) PRIMARY KEY,
	BUILDING INT,
	FLOOR_NUM INT,
	NUM INT
);

-- ALTER TABLE ROOMS
-- RENAME COLUMN FLOOR TO FLOOR_NUM;

ALTER TABLE ROOMS
COMMENT = "Table to store ROOMS' information";

ALTER TABLE ROOMS
MODIFY COLUMN ID VARCHAR(36) COMMENT 'Unique identifier for each ROOM',
MODIFY COLUMN  BUILDING INT COMMENT 'NUMBER OF A BUILDING',
MODIFY COLUMN  FLOOR_NUM INT COMMENT 'NUMBER OF A FLOOR',
MODIFY COLUMN  NUM INT COMMENT 'NUMBER OF A ROOM'

select * from ROOMS;

-- побачити коменти
SELECT column_name, column_comment
FROM information_schema.columns
WHERE table_name = 'ROOMS';

----------------------------------------------------------- ROOMS table end------------------------------

----------------------------------------------------------- APPOINTMENTS table start------------------------------

 DROP TABLE IF EXISTS APPOINTMENTS;
-- заповнено
CREATE TABLE IF NOT EXISTS APPOINTMENTS
(
	ID VARCHAR(36) PRIMARY KEY,
	APPOINTMENT_START_TIME DATETIME,
	APPOINTMENT_END_TIME DATETIME,
	ROOM_ID VARCHAR(36),
	DOCTOR_ID VARCHAR(36),
	PATIENT_ID VARCHAR(36),
	foreign key (ROOM_ID) references ROOMS(ID),
	foreign key (DOCTOR_ID) references DOCTORS(ID),
	foreign key (PATIENT_ID) references PATIENTS(ID)
);

select * from appointments;

ALTER TABLE APPOINTMENTS
COMMENT = "Table to store APPOINTMENTS' information";

-- FK - FOREIGN KEY
ALTER TABLE APPOINTMENTS
MODIFY COLUMN ID VARCHAR(36) COMMENT 'Unique identifier for each APPOINTMENT',
MODIFY COLUMN APPOINTMENT_START_TIME DATETIME COMMENT 'START TIME for each APPOINTMENT',
MODIFY COLUMN APPOINTMENT_END_TIME DATETIME COMMENT 'END TIME for each APPOINTMENT',
MODIFY COLUMN ROOM_ID VARCHAR(36) COMMENT 'Unique identifier for each ROOM FK',
MODIFY COLUMN DOCTOR_ID VARCHAR(36) COMMENT 'Unique identifier for each DOCTOR FK',
MODIFY COLUMN PATIENT_ID VARCHAR(36) COMMENT 'Unique identifier for each PATIENT FK'

-- побачити коменти
SELECT column_name, column_comment
FROM information_schema.columns
WHERE table_name = 'APPOINTMENTS';

----------------------------------------------------------- APPOINTMENTS table ------------------------------

----------------------------------------------------------- DEATHS table ------------------------------

-- DROP TABLE IF EXISTS DEATHS;
-- заповнено
CREATE TABLE IF NOT EXISTS DEATHS
(
	ID VARCHAR(36) PRIMARY KEY,
	NAME VARCHAR(200),
	SURNAME VARCHAR(200),
	TIME_OF_DEATH DATETIME,
	FAMILY_PHONE_NUMBER VARCHAR(36),
	CAUSE_OF_DEATH VARCHAR(200),
	DOCTOR_ID VARCHAR(36),
	foreign key (DOCTOR_ID) references DOCTORS(ID)
);

select * from DEATHS;

ALTER TABLE DEATHS
COMMENT = "Table to store APPOINTMENTS' information";

-- FK - FOREIGN KEY
ALTER TABLE DEATHS
MODIFY COLUMN ID VARCHAR(36) COMMENT 'Unique identifier for each DEATH',
MODIFY COLUMN TIME_OF_DEATH DATETIME COMMENT 'START TIME for each DEATH',
MODIFY COLUMN NAME VARCHAR(200) COMMENT 'THE NAME OF EACH DEAD',
MODIFY COLUMN SURNAME VARCHAR(200) COMMENT 'THE SURNAME OF EACH DEAD',
MODIFY COLUMN DOCTOR_ID VARCHAR(36) COMMENT 'Unique identifier for each DOCTOR FK',
MODIFY COLUMN FAMILY_PHONE_NUMBER VARCHAR(36) COMMENT 'EACH FAMILY PHONE NUMBER',
MODIFY COLUMN CAUSE_OF_DEATH VARCHAR(200) COMMENT 'CAUSE OF DEATH'


-- побачити коменти
SELECT column_name, column_comment
FROM information_schema.columns
WHERE table_name = 'DEATHS';

----------------------------------------------------------- DEATHS table ------------------------------

----------------------------------------------------------- EQUIPMENT table ------------------------------
-- заповнено

-- DROP TABLE IF EXISTS EQUIPMENT;

CREATE TABLE IF NOT EXISTS EQUIPMENT
(
	ID VARCHAR(36) PRIMARY KEY,
	NAME VARCHAR(200),
	EQUIPMENT_TYPE VARCHAR(200),
	QUANTITY INT
);

select * from EQUIPMENT;

ALTER TABLE EQUIPMENT
COMMENT = "Table to store EQUIPMENT information";

ALTER TABLE EQUIPMENT
MODIFY COLUMN ID VARCHAR(36) COMMENT 'Unique identifier for EQUIPMENT',
MODIFY COLUMN NAME VARCHAR(200) COMMENT 'THE NAME OF EACH EQUIPMENT',
MODIFY COLUMN EQUIPMENT_TYPE VARCHAR(200) COMMENT 'THE TYPE OF EACH EQUIPMENT',
MODIFY COLUMN QUANTITY INT COMMENT 'QUANTITY OF EQUIPMENT'


-- побачити коменти
SELECT column_name, column_comment
FROM information_schema.columns
WHERE table_name = 'EQUIPMENT';

----------------------------------------------------------- EQUIPMENT table ------------------------------

----------------------------------------------------------- WARDS table ------------------------------
-- заповнено

-- DROP TABLE IF EXISTS WARDS;

CREATE TABLE IF NOT EXISTS WARDS
(
	ID VARCHAR(36) PRIMARY KEY,
	BUILDING INT,
	FLOOR_NUM INT,
	NUM INT
);

select * from WARDS;

ALTER TABLE WARDS
COMMENT = "Table to store WARDS information";

ALTER TABLE WARDS
MODIFY COLUMN ID VARCHAR(36) COMMENT 'Unique identifier for WARDS',
MODIFY COLUMN  BUILDING INT COMMENT 'NUMBER OF A BUILDING',
MODIFY COLUMN  FLOOR_NUM INT COMMENT 'NUMBER OF A FLOOR',
MODIFY COLUMN  NUM INT COMMENT 'NUMBER OF A ROOM'

-- побачити коменти
SELECT column_name, column_comment
FROM information_schema.columns
WHERE table_name = 'WARDS';

----------------------------------------------------------- WARDS table ------------------------------

----------------------------------------------------------- DIAGNOSES table ------------------------------

-- DROP TABLE IF EXISTS DIAGNOSES;

CREATE TABLE IF NOT EXISTS DIAGNOSES
(
    id varchar(36) primary key,
	PATIENT_ID VARCHAR(36),
	DIAGNOSES_NAME VARCHAR(200),
	START_DATE DATE,
	END_DATE DATE,
	MEDICINE_ID VARCHAR(200),
	foreign key (PATIENT_ID) references PATIENTS(ID),
	foreign key (MEDICINE_ID) references MEDICINE(ID)
);

select * from DIAGNOSES;

ALTER TABLE DIAGNOSES
COMMENT = "Table to store DIAGNOSES information";

-- ALTER TABLE DIAGNOSES
-- RENAME COLUMN MEDICINE TO MEDICINE_ID;

ALTER TABLE DIAGNOSES
MODIFY COLUMN PATIENT_ID VARCHAR(36) COMMENT 'Unique identifier for PATIENTS',
MODIFY COLUMN DIAGNOSES_NAME VARCHAR(200) COMMENT 'DIAGNOSES NAME',
MODIFY COLUMN START_DATE DATE COMMENT 'START DATE OF ILLNESS',
MODIFY COLUMN END_DATE DATE COMMENT 'END DATE OF ILLNESS',
MODIFY COLUMN MEDICINE_ID VARCHAR(200) COMMENT 'MEDICINE TAKEN FROM ILLNESS'

-- побачити коменти
SELECT column_name, column_comment
FROM information_schema.columns
WHERE table_name = 'DIAGNOSES';

----------------------------------------------------------- DIAGNOSES table ------------------------------

----------------------------------------------------------- MEDICINE table ------------------------------
-- заповнено

CREATE TABLE IF NOT EXISTS MEDICINE
(
	ID VARCHAR(36) PRIMARY KEY,
	NAME VARCHAR(200),
	MEDICINE_TYPE VARCHAR(200),
	BATCH_NUMBER INT,
	EXPIRATION_DATE DATE,
	QUANTITY INT
);

select * from MEDICINE;

ALTER TABLE MEDICINE
COMMENT = "Table to store MEDICINE information";

ALTER TABLE MEDICINE
MODIFY COLUMN ID VARCHAR(36) COMMENT 'Unique identifier for MEDICINE',
MODIFY COLUMN NAME VARCHAR(200) COMMENT 'MEDICINE NAME',
MODIFY COLUMN MEDICINE_TYPE VARCHAR(200) COMMENT 'TYPE OF MEDICINE',
MODIFY COLUMN BATCH_NUMBER INT COMMENT 'BATCH NUMBER OF MEDICINE',
MODIFY COLUMN EXPIRATION_DATE DATE COMMENT 'EXPIRATION DATE OF THE MEDICINE',
MODIFY COLUMN QUANTITY INT COMMENT 'QUANTITY OF MEDICINE'

-- побачити коменти
SELECT column_name, column_comment
FROM information_schema.columns
WHERE table_name = 'MEDICINE';

----------------------------------------------------------- MEDICINE table ------------------------------

