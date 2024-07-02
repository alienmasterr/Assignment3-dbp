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

# Global variables
fake = Faker()
MAX_PHONE_LENGTH = 20

def connect_to_database():
    return mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

def insert_rooms(cursor, connection):
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
    return rooms_data

def insert_equipment(cursor, connection):
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
    return equipment_data

def insert_wards(cursor, connection):
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
    return wards_data

def insert_medicine(cursor, connection):
    print("Inserting into medicine...")
    medicine_insert_query = """
            INSERT INTO medicine (id, name, MEDICINE_TYPE, BATCH_NUMBER, EXPIRATION_DATE, QUANTITY) 
            VALUES (%s, %s, %s, %s, %s, %s)
        """
    medicine_data = [
        (
            str(uuid.uuid4()), fake.word(), fake.word(), random.randint(100000, 999999), fake.date(), random.randint(100, 1000)
        )
        for _ in range(10000)
    ]
    cursor.executemany(medicine_insert_query, medicine_data)
    connection.commit()
    print("Inserted into medicine.")
    return medicine_data

def insert_patients(cursor, connection, wards_data):
    print("Inserting into patients...")
    uuids = [ward[0] for ward in wards_data]

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
    return patients_data

def insert_departments(cursor, connection):
    print("Inserting into DEPARTMENTS...")
    departments_insert_query = """
            INSERT INTO DEPARTMENTS (ID, DEPARTMENT_TYPE) 
            VALUES (%s, %s)
        """
    departments_data = [
        (str(uuid.uuid4()), fake.word())
        for _ in range(50)
    ]
    cursor.executemany(departments_insert_query, departments_data)
    connection.commit()
    print("Inserted into DEPARTMENTS.")
    return departments_data

def insert_doctors(cursor, connection, rooms_data):
    print("Inserting into DOCTORS...")

    uuids_rooms = [room[0] for room in rooms_data]
    length = len(rooms_data)
    number_of_doctors = 5000

    def choose_id():
        nonlocal length
        if length > 0:
            room_id = uuids_rooms[length - 1]
            length -= 1
        else:
            room_id = None
        return room_id

    doctors_insert_query = """
            INSERT INTO DOCTORS (id, first_name, last_name, email, phone, ROOM_ID, SPECIALIZATION) 
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
    doctors_data = [
        (str(uuid.uuid4()), fake.name(), fake.last_name(), fake.email(), fake.phone_number()[:MAX_PHONE_LENGTH], choose_id(),
         fake.word())
        for _ in range(number_of_doctors)
    ]
    cursor.executemany(doctors_insert_query, doctors_data)
    connection.commit()
    print("Inserted into DOCTORS.")
    return doctors_data

def insert_doctor_department(cursor, connection, doctors_data, departments_data):
    print("Inserting into DOCTOR_DEPARTMENT...")

    doctor_ids = [doctor_id[0] for doctor_id in doctors_data]
    department_ids = [department_id[0] for department_id in departments_data]

    random.shuffle(doctor_ids)

    doctor_department_insert_query = """
            INSERT INTO DOCTOR_DEPARTMENT (DOCTOR_ID, DEPARTMENT_ID, MAIN_DOCTOR) 
            VALUES (%s, %s, %s)
        """

    doctor_department_data = []

    # Призначити головних лікарів для кожного департаменту
    for department_id in department_ids:
        if doctor_ids:
            main_doctor_id = doctor_ids.pop()
            doctor_department_data.append((main_doctor_id, department_id, True))

    # Розподілити інших лікарів по департаментах
    while doctor_ids:
        for department_id in department_ids:
            if doctor_ids:
                doctor_id = doctor_ids.pop()
                doctor_department_data.append((doctor_id, department_id, False))

    cursor.executemany(doctor_department_insert_query, doctor_department_data)
    connection.commit()
    print("Inserted into DOCTOR_DEPARTMENT.")
    return doctor_department_data

def insert_deaths(cursor, connection, doctors_data):
    print("Inserting into DEATHS...")

    doctor_ids = [doctor_id[0] for doctor_id in doctors_data]

    deaths_insert_query = """
            INSERT INTO DEATHS (id, name, surname, TIME_OF_DEATH, FAMILY_PHONE_NUMBER, CAUSE_OF_DEATH, DOCTOR_ID) 
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
    deaths_data = [
        (str(uuid.uuid4()), fake.name(), fake.last_name(), fake.date_time(), fake.phone_number()[:MAX_PHONE_LENGTH],
         fake.word(), random.choice(doctor_ids))
        for _ in range(500)
    ]
    cursor.executemany(deaths_insert_query, deaths_data)
    connection.commit()
    print("Inserted into DEATHS.")
    return deaths_data

def insert_appointments(cursor, connection, doctors_data, rooms_data, patients_data):
    print("Inserting into APPOINTMENTS...")

    doctor_ids = [doctor_id[0] for doctor_id in doctors_data]
    uuids_rooms = [room[0] for room in rooms_data]
    patient_ids = [patient_id[0] for patient_id in patients_data]

    appointments_insert_query = """
            INSERT INTO APPOINTMENTS (id, APPOINTMENT_START_TIME, APPOINTMENT_END_TIME, ROOM_ID, DOCTOR_ID, PATIENT_ID) 
            VALUES (%s, %s, %s, %s, %s, %s)
        """
    appointments_data = [
        (str(uuid.uuid4()), start_time := fake.date_time(),
         start_time + timedelta(minutes=30), random.choice(uuids_rooms), random.choice(doctor_ids),
         random.choice(patient_ids))
        for _ in range(10000)
    ]
    cursor.executemany(appointments_insert_query, appointments_data)
    connection.commit()
    print("Inserted into APPOINTMENTS.")
    return appointments_data

def main():
    connection = connect_to_database()
    cursor = connection.cursor()

    rooms_data = insert_rooms(cursor, connection)
    equipment_data = insert_equipment(cursor, connection)
    wards_data = insert_wards(cursor, connection)
    medicine_data = insert_medicine(cursor, connection)
    patients_data = insert_patients(cursor, connection, wards_data)
    departments_data = insert_departments(cursor, connection)
    doctors_data = insert_doctors(cursor, connection, rooms_data)
    doctor_department_data = insert_doctor_department(cursor, connection, doctors_data, departments_data)
    deaths_data = insert_deaths(cursor, connection, doctors_data)
    appointments_data = insert_appointments(cursor, connection, doctors_data, rooms_data, patients_data)

    cursor.close()
    connection.close()

if __name__ == "__main__":
    main()
