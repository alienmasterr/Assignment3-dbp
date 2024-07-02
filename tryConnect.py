import mysql.connector
import uuid

from faker import Faker
from dotenv import load_dotenv
import random
import os
from datetime import timedelta

# Load environment variables
load_dotenv()

# Connection settings
HOST = os.getenv('host')
USER = os.getenv('user')
PASSWORD = os.getenv('password')
DATABASE = os.getenv('database')

# Connect to the MySQL database
connection = mysql.connector.connect(
    host=HOST,
    user=USER,
    password=PASSWORD,
    database=DATABASE
)

cursor = connection.cursor()
fake = Faker()

# -------------------------------------------------- Insert 5000 rows into rooms
print("Inserting into rooms...")
rooms_insert_query = """
        INSERT INTO rooms (id, building, floor_num, num) 
        VALUES (%s, %s, %s, %s)
    """
rooms_data = [
    (str(uuid.uuid4()), random.randint(1, 10), random.randint(1, 5), random.randint(1, 100))
    for _ in range(5000)
]
cursor.executemany(rooms_insert_query, rooms_data)
connection.commit()
print("Inserted into rooms.")
# -------------------------------------------------- Insert 5000 rows into rooms

# -------------------------------------------------- Insert 5000 rows into equipment
print("Inserting into equipment...")
equipment_insert_query = """
        INSERT INTO equipment (id, name, EQUIPMENT_TYPE, quantity) 
        VALUES (%s, %s, %s, %s)
    """
equipment_data = [
    (str(uuid.uuid4()), fake.word(), fake.word(), random.randint(1, 100))
    for _ in range(5000)
]
cursor.executemany(equipment_insert_query, equipment_data)
connection.commit()
print("Inserted into equipment.")
# -------------------------------------------------- Insert 5000 rows into equipment

# -------------------------------------------------- Insert 5000 rows into wards
print("Inserting into wards...")
wards_insert_query = """
        INSERT INTO wards (id, building, floor_num, num) 
        VALUES (%s, %s, %s, %s)
    """
wards_data = [
    (str(uuid.uuid4()), random.randint(1, 10), random.randint(6, 7), random.randint(1, 100))
    for _ in range(5000)
]
cursor.executemany(wards_insert_query, wards_data)
connection.commit()
print("Inserted into wards.")
# -------------------------------------------------- Insert 5000 rows into wards

# -------------------------------------------------- Insert 10000 rows into medicine
print("Inserting into medicine...")
medicine_insert_query = """
        INSERT INTO medicine (id, name, MEDICINE_TYPE, BATCH_NUMBER, EXPIRATION_DATE, QUANTITY) 
        VALUES (%s, %s, %s, %s, %s, %s)
    """
medicine_data = [
    (
    str(uuid.uuid4()), fake.word(), fake.word(), random.randint(100000, 999999), fake.date(), random.randint(100, 1000))
    for _ in range(10000)
]
cursor.executemany(medicine_insert_query, medicine_data)
connection.commit()
print("Inserted into medicine.")
# -------------------------------------------------- Insert 10000 rows into medicine

# -------------------------------------------------- Insert 500 000 rows into patients
print("Inserting into patients...")

uuids = [ward[0] for ward in wards_data]
MAX_PHONE_LENGTH = 20

patients_insert_query = """
        INSERT INTO patients (id, first_name, last_name, email, phone, INSURANCE_NUMBER, WARD_ID) 
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
patients_data = [
    (str(uuid.uuid4()), fake.name(), fake.last_name(), fake.email(), fake.phone_number()[:MAX_PHONE_LENGTH],
     str(uuid.uuid4()), random.choice(uuids))
    for _ in range(5000)
]
cursor.executemany(patients_insert_query, patients_data)
connection.commit()
print("Inserted into patients.")
# -------------------------------------------------- Insert 500 000 rows into patients

# -------------------------------------------------- Insert 50 rows into DEPARTMENTS

print("Inserting into DEPARTMENTS...")
DEPARTMENTS_insert_query = """
        INSERT INTO DEPARTMENTS (ID, DEPARTMENT_TYPE) 
        VALUES (%s, %s)
    """
DEPARTMENTS_data = [
    (str(uuid.uuid4()), fake.word())
    for _ in range(50)
]
cursor.executemany(DEPARTMENTS_insert_query, DEPARTMENTS_data)
connection.commit()
print("Inserted into DEPARTMENTS.")
# -------------------------------------------------- Insert 50 rows into DEPARTMENTS

# -------------------------------------------------- Insert 500000 rows into DOCTORS

print("Inserting into DOCTORS...")

uuidsRooms = [room[0] for room in rooms_data]
MAX_PHONE_LENGTH = 20

length = len(rooms_data)
number_of_doctors = 5000


def chooseId():
    global length
    if length > 0:
        room_id = uuidsRooms[length - 1]
        length -= 1
    else:
        room_id = None
    return room_id


DOCTORS_insert_query = """
        INSERT INTO DOCTORS (id, first_name, last_name, email, phone, ROOM_ID, SPECIALIZATION) 
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
DOCTORS_data = [
    (str(uuid.uuid4()), fake.name(), fake.last_name(), fake.email(), fake.phone_number()[:MAX_PHONE_LENGTH], chooseId(),
     fake.word())
    for _ in range(number_of_doctors)
]
cursor.executemany(DOCTORS_insert_query, DOCTORS_data)
connection.commit()
print("Inserted into DOCTORS.")
# -------------------------------------------------- Insert 500000 rows into DOCTORS

# -------------------------------------------------- Insert 500000 rows into DOCTOR_DEPARTMENT

print("Inserting into DOCTOR_DEPARTMENT...")

doctor_ids = [doctor_id[0] for doctor_id in DOCTORS_data]
department_ids = [department_id[0] for department_id in DEPARTMENTS_data]

random.shuffle(doctor_ids)

DOCTOR_DEPARTMENT_insert_query = """
        INSERT INTO DOCTOR_DEPARTMENT (DOCTOR_ID, DEPARTMENT_ID, MAIN_DOCTOR) 
        VALUES (%s, %s, %s)
    """

DOCTOR_DEPARTMENT_data = []

# Призначити головних лікарів для кожного департаменту
for department_id in department_ids:
    if doctor_ids:
        main_doctor_id = doctor_ids.pop()
        DOCTOR_DEPARTMENT_data.append((main_doctor_id, department_id, True))

# Розподілити інших лікарів по департаментах
while doctor_ids:
    for department_id in department_ids:
        if doctor_ids:
            doctor_id = doctor_ids.pop()
            DOCTOR_DEPARTMENT_data.append((doctor_id, department_id, False))

valid_department_ids = set(department_ids)
for record in DOCTOR_DEPARTMENT_data:
    if record[1] not in valid_department_ids:
        print(f"Invalid DEPARTMENT_ID found: {record[1]}")

cursor.executemany(DOCTOR_DEPARTMENT_insert_query, DOCTOR_DEPARTMENT_data)
connection.commit()
print("Inserted into DOCTOR_DEPARTMENT.")
# -------------------------------------------------- Insert 500000 rows into DOCTOR_DEPARTMENT

# -------------------------------------------------- Insert 500 rows into DEATHS
print("Inserting into DEATHS...")
doctor_ids = [doctor_id[0] for doctor_id in DOCTORS_data]

# MAX_PHONE_LENGTH = 20

DEATHS_insert_query = """
        INSERT INTO DEATHS (id, name, surname, TIME_OF_DEATH, FAMILY_PHONE_NUMBER, CAUSE_OF_DEATH, DOCTOR_ID) 
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
DEATHS_data = [
    (str(uuid.uuid4()), fake.name(), fake.last_name(), fake.date_time(), fake.phone_number()[:MAX_PHONE_LENGTH],
     fake.word(), random.choice(doctor_ids))
    for _ in range(500)
]
cursor.executemany(DEATHS_insert_query, DEATHS_data)
connection.commit()
print("Inserted into DEATHS.")
# -------------------------------------------------- Insert 500 rows into DEATHS

# -------------------------------------------------- Insert 10000 rows into APPOINTMENTS
print("Inserting into APPOINTMENTS...")
doctor_ids = [doctor_id[0] for doctor_id in DOCTORS_data]
uuidsRooms = [room[0] for room in rooms_data]
patient_ids = [patient_id[0] for patient_id in patients_data]

APPOINTMENTS_insert_query = """
        INSERT INTO APPOINTMENTS (id, APPOINTMENT_START_TIME, APPOINTMENT_END_TIME, ROOM_ID, DOCTOR_ID, PATIENT_ID) 
        VALUES (%s, %s, %s, %s, %s, %s)
    """
APPOINTMENTS_data = [
    (str(uuid.uuid4()), start_time := fake.date_time(),
     start_time + timedelta(minutes=30), random.choice(uuidsRooms), random.choice(doctor_ids),
     random.choice(patient_ids))
    for _ in range(10000)
]
cursor.executemany(APPOINTMENTS_insert_query, APPOINTMENTS_data)
connection.commit()
print("Inserted into APPOINTMENTS.")
# -------------------------------------------------- Insert 10000 rows into APPOINTMENTS

cursor.close()
connection.close()
