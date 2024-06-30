import mysql.connector
import uuid
from faker import Faker
from dotenv import load_dotenv
import random
import os

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

#-------------------------------------------------- Insert 5000 rows into rooms
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
#-------------------------------------------------- Insert 5000 rows into rooms

#-------------------------------------------------- Insert 5000 rows into equipment
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
#-------------------------------------------------- Insert 5000 rows into equipment

#-------------------------------------------------- Insert 5000 rows into wards
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
#-------------------------------------------------- Insert 5000 rows into wards

#-------------------------------------------------- Insert 10000 rows into medicine
print("Inserting into medicine...")
medicine_insert_query = """
        INSERT INTO medicine (id, name, MEDICINE_TYPE, BATCH_NUMBER, EXPIRATION_DATE, QUANTITY) 
        VALUES (%s, %s, %s, %s, %s, %s)
    """
medicine_data = [
    (str(uuid.uuid4()), fake.word(), fake.word(), random.randint(100000, 999999), fake.date(), random.randint(100, 1000))
    for _ in range(10000)
]
cursor.executemany(medicine_insert_query, medicine_data)
connection.commit()
print("Inserted into medicine.")
#-------------------------------------------------- Insert 10000 rows into medicine

#-------------------------------------------------- Insert 500 000 rows into patients
print("Inserting into patients...")

uuids = [ward[0] for ward in wards_data]
MAX_PHONE_LENGTH = 20

patients_insert_query = """
        INSERT INTO patients (id, first_name, last_name, email, phone, INSURANCE_NUMBER, WARD_ID) 
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
patients_data = [
    (str(uuid.uuid4()), fake.name(), fake.last_name(), fake.email(), fake.phone_number()[:MAX_PHONE_LENGTH], str(uuid.uuid4()), random.choice(uuids))
    for _ in range(5000)
]
cursor.executemany(patients_insert_query, patients_data)
connection.commit()
print("Inserted into patients.")
#-------------------------------------------------- Insert 500 000 rows into patients

cursor.close()
connection.close()
