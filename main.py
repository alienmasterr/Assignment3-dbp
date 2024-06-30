import mysql.connector
from mysql.connector import Error
import uuid
import os
from dotenv import load_dotenv
from faker import Faker
import random
import time

# Load environment variables
load_dotenv()

# Connection settings
HOST = os.getenv('host')
USER = os.getenv('user')
PASSWORD = os.getenv('password')
DATABASE = os.getenv('database')

fake = Faker()


