import mysql.connector
import uuid
from faker import Faker
from dotenv import load_dotenv
import random
import os

# Load environment variables
load_dotenv()

# Connection settings
HOST = os.getenv('HOST')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')
DATABASE = os.getenv('DATABASE')

# Connect to the MySQL database
connection = mysql.connector.connect(
    host=HOST,
    user=USER,
    password=PASSWORD,
    database=DATABASE
)

cursor = connection.cursor()
fake = Faker()


# ----------------------------------- MEDICINE TABLE -------------------------------------------------------------------
# Insert 50000 rows into MEDICINE
print("Inserting into MEDICINE ...")
medicine_insert_query = """
    INSERT INTO MEDICINE (ID, NAME, MEDICINE_TYPE, BATCH_NUMBER, EXPIRATION_DATE, QUANTITY) 
    VALUES (%s, %s, %s, %s, %s, %s)
"""

medicine_data = [
    (str(uuid.uuid4()), fake.word(), fake.word(), fake.random_number(), fake.date(), random.randint(1, 4000))
    for _ in range(50000)
]

cursor.executemany(medicine_insert_query, medicine_data)
connection.commit()
print("Inserted into MEDICINE.")

cursor.execute("SELECT ID FROM MEDICINE")
medicine_ids = [row[0] for row in cursor.fetchall()]

# ----------------------------------- WARDS TABLE -------------------------------------------------------------------

# Insert 45000 rows into WARDS
print("Inserting into WARDS...")
wards_insert_query = """
    INSERT INTO WARDS (ID, BUILDING, FLOOR_NUM, NUM) 
    VALUES (%s, %s, %s, %s)
"""
wards_data = [
    (str(uuid.uuid4()), random.randint(1,100), random.randint(1, 20), random.randint(1, 500))
    for _ in range(45000)
]
cursor.executemany(wards_insert_query, wards_data)
connection.commit()
print("Inserted into WARDS.")

cursor.execute("SELECT ID FROM WARDS")
wards_ids = [row[0] for row in cursor.fetchall()]

# ----------------------------------- EQUIPMENT TABLE -----------------------------------------------------------------

# Insert 30000 rows into EQUIPMENT
print("Inserting into EQUIPMENT...")
equipment_insert_query = """
    INSERT INTO EQUIPMENT (ID, NAME, EQUIPMENT_TYPE, QUANTITY) 
    VALUES (%s, %s, %s, %s)
"""
equipment_data = [
    (str(uuid.uuid4()), fake.word(), fake.word(), random.randint(1,1000))
    for _ in range(30000)
]

cursor.executemany(equipment_insert_query, equipment_data)
connection.commit()
print("Inserted into EQUIPMENT.")

# ----------------------------------- ROOMS TABLE -------------------------------------------------------------------

# Insert 50000 rows into ROOMS
print("Inserting into ROOMS...")
rooms_insert_query = """
    INSERT INTO ROOMS (ID, BUILDING, FLOOR_NUM, NUM) 
    VALUES (%s, %s, %s, %s)
"""
rooms_data = [
    (str(uuid.uuid4()), random.randint(1, 100), random.randint(1, 20), random.randint(1,10000))
    for _ in range(50000)
]
cursor.executemany(rooms_insert_query, rooms_data)
connection.commit()
print("Inserted into ROOMS.")

cursor.execute("SELECT ID FROM ROOMS")
room_ids = [row[0] for row in cursor.fetchall()]

# ----------------------------------- DEPARTMENTS TABLE ----------------------------------------------------------------

# Insert 7000 rows into DEPARTMENTS
print("Inserting into DEPARTMENTS...")
departments_insert_query = """
    INSERT INTO DEPARTMENTS (ID, DEPARTMENT_TYPE) 
    VALUES (%s, %s)
"""
departments_data = [
    (str(uuid.uuid4()), fake.word())
    for _ in range(7000)
]
cursor.executemany(departments_insert_query, departments_data)
connection.commit()
print("Inserted into DEPARTMENTS.")

cursor.execute("SELECT ID FROM DEPARTMENTS")
department_ids = [row[0] for row in cursor.fetchall()]

# ----------------------------------- DOCTORS TABLE -------------------------------------------------------------------

# Insert 1000 rows into DOCTORS
print("Inserting into DOCTORS...")
doctors_insert_query = """
    INSERT INTO DOCTORS (ID, FIRST_NAME, LAST_NAME, EMAIL, PHONE, ROOM_ID, SPECIALIZATION) 
    VALUES (%s, %s, %s, %s, %s, %s, %s)
"""
doctors_data = [
    (str(uuid.uuid4()), fake.first_name(), fake.last_name(), fake.email(), fake.phone_number()[:20], random.choice(room_ids), fake.job())
    for _ in range(1000)
]
cursor.executemany(doctors_insert_query, doctors_data)
connection.commit()
print("Inserted into DOCTORS.")

cursor.execute("SELECT ID FROM DOCTORS")
doctor_ids = [row[0] for row in cursor.fetchall()]

# ----------------------------------- DOCTOR DEPARTMENT TABLE ----------------------------------------------------------

# Insert 6000 rows into DOCTOR_DEPARTMENT
print("Inserting into DOCTOR_DEPARTMENT...")
doctor_department_insert_query = """
    INSERT INTO DOCTOR_DEPARTMENT (DOCTOR_ID, DEPARTMENT_ID, MAIN_DOCTOR) 
    VALUES (%s, %s, %s)
"""

doctor_department_data = [
    (random.choice(doctor_ids), random.choice(department_ids), random.randint(0, 1))
    for _ in range(6000)
]
cursor.executemany(doctor_department_insert_query, doctor_department_data)
connection.commit()
print("Inserted into DOCTOR DEPARTMENT.")


# ----------------------------------- PATIENTS TABLE -------------------------------------------------------------------

# Insert 500000 rows into PATIENTS
print("Inserting into PATIENTS...")
patients_insert_query = """
    INSERT INTO PATIENTS (ID, FIRST_NAME, LAST_NAME, EMAIL, PHONE, INSURANCE_NUMBER, WARD_ID) 
    VALUES (%s, %s, %s, %s, %s, %s, %s)
"""

batch_size = 100000  # Define the batch size
for i in range(0, 500000, batch_size):
    batch_data = [
        (str(uuid.uuid4()), fake.first_name(), fake.last_name(), fake.email(), fake.phone_number()[:20], str(uuid.uuid4()), random.choice(wards_ids))
        for _ in range(batch_size)
    ]
    cursor.executemany(patients_insert_query, batch_data)
    connection.commit()
    print(f"Inserted batch {i // batch_size + 1} of {500000 // batch_size}")

# Fetch all patient IDs after inserts
cursor.execute("SELECT ID FROM PATIENTS")
patients_ids = [row[0] for row in cursor.fetchall()]

print("Inserted into PATIENTS.")


# ----------------------------------- DIAGNOSES TABLE -------------------------------------------------------------------

# Insert 5000 rows into DIAGNOSES
print("Inserting into DIAGNOSES...")
diagnoses_insert_query = """
    INSERT INTO DIAGNOSES (DIAGNOSES_ID, PATIENT_ID, DIAGNOSES_NAME, START_DATE, END_DATE, MEDICINE_ID) 
    VALUES (%s, %s, %s, %s, %s, %s)
"""
diagnoses_data = [
    (str(uuid.uuid4()), random.choice(patients_ids), fake.word(), fake.date_time(), fake.date_time_between(start_date='now', end_date='+30d'), random.choice(medicine_ids))
    for _ in range(5000)
]
cursor.executemany(diagnoses_insert_query, diagnoses_data)
connection.commit()
print("Inserted into DIAGNOSES.")

# ----------------------------------- DEATHS TABLE -------------------------------------------------------------------

# Insert 38000 rows into DEATHS
print("Inserting into DEATHS...")
deaths_insert_query = """
    INSERT INTO DEATHS (ID, NAME, SURNAME, TIME_OF_DEATH, FAMILY_PHONE_NUMBER, CAUSE_OF_DEATH, DOCTOR_ID) 
    VALUES (%s, %s, %s, %s, %s, %s, %s)
"""
deaths_data = [
    (str(uuid.uuid4()), fake.first_name(), fake.last_name(), fake.date_time(), fake.phone_number(), fake.sentence(), random.choice(doctor_ids))
    for _ in range(38000)
]
cursor.executemany(deaths_insert_query, deaths_data)
connection.commit()
print("Inserted into DEATHS.")

# ----------------------------------- APPOINTMENTS TABLE ---------------------------------------------------------------

# Insert 20000 rows into APPOINTMENTS
print("Inserting into APPOINTMENTS...")
appointments_insert_query = """
    INSERT INTO APPOINTMENTS (ID, APPOINTMENT_START_TIME, APPOINTMENT_END_TIME, ROOM_ID, DOCTOR_ID, PATIENT_ID) 
    VALUES (%s, %s, %s, %s, %s, %s)
"""
appointments_data = [
    (str(uuid.uuid4()), fake.date_time_between(start_date='-1y', end_date='now'), fake.date_time_between(start_date='now', end_date='+1y'), random.choice(room_ids), random.choice(doctor_ids), random.choice(patients_ids))
    for _ in range(20000)
]
cursor.executemany(appointments_insert_query, appointments_data)
connection.commit()
print("Inserted into APPOINTMENTS.")

# Close the cursor and connection
cursor.close()
connection.close()

