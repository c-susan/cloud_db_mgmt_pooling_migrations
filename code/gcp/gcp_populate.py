from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from faker import Faker
from gcp_create_tables import Doctor, Patient
import os
import random 
from dotenv import load_dotenv

load_dotenv()

## Database credentials 
DB_HOST = os.getenv("DB_HOST")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = int(os.getenv("DB_PORT", 3306))
DB_CHARSET = os.getenv("DB_CHARSET", "utf8mb4")

# Connection string and creating the engine 
connect_args={'ssl':{'fake_flag_to_enable_tls': True}}
connection_string = (f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}'
                    f"?charset={DB_CHARSET}")
engine = create_engine(
        connection_string,
        connect_args=connect_args)

# Creating a session to populate the data
Session = sessionmaker(bind=engine)
session = Session()

fake = Faker()

# Adding 10 records to the doctor table

# Creating a function to return a correct format for the phone number 
def phone_number():
    # Generate random numbers for each part of the phone number
    p1 = str(random.randint(1, 999)).zfill(3)
    p2 = str(random.randint(0, 999)).zfill(3)
    p3 = str(random.randint(0, 9999)).zfill(4)

    # Format the phone number as "000-000-0000"
    format = f"{p1}-{p2}-{p3}"
    return format

for _ in range(10):
    doctor = Doctor(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        department=fake.random_element(elements=("Cardiology", "Orthopedics", "Pediatrics","Internal Medicine","Urology","Psychiatry")),
        phone_number=phone_number()
    )
    session.add(doctor)

for _ in range(20):
    patient = Patient(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        date_of_birth=fake.date_of_birth(minimum_age=18, maximum_age=65),
        primary_doctor_id=session.query(Doctor).order_by(func.rand()).first().doctor_id
    )
    session.add(patient)

# Commit the changes to the database
session.commit()

# Close the session
session.close()
