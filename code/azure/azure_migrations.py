"""

pip install sqlalchemy alembic mysql-connector-python
pip install pysql   ---> required for azure connection 

"""

## Part 1 - Define SQLAlchemy models for patients and their medical records:
### this file below could always be called db_schema.py or something similar

from sqlalchemy import create_engine, inspect, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

databaseURL = os.getenv("DB_URL")

Base = declarative_base()

class Doctor(Base):
    __tablename__ = 'doctors'

    doctor_id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    department = Column(String(50), nullable=False)
    phone_number = Column(String(15))

    doctors = relationship('Patient', back_populates='patients')

class Patient(Base):
    __tablename__ = 'patients'

    patient_id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50))
    date_of_birth = Column(Date, nullable=False)
    primary_doctor_id = Column(Integer, ForeignKey('doctors.doctor_id'), nullable=False)

    patients = relationship('Doctor', back_populates='doctors')


### Part 2 - initial sqlalchemy-engine to connect to db:

#DATABASE_URL = "mysql+mysqlconnector://root:password@35.184.8.172/susan"
#engine = create_engine(DATABASE_URL)               This can work with gcp
engine = create_engine("mysql+pymysql://susan:hhA5041314520@504migrations.mysql.database.azure.com/susan",
                         connect_args={'ssl': {'ssl-mode': 'preferred'}},
                         )

## Test connection

inspector = inspect(engine)
inspector.get_table_names()


### Part 3 - create the tables using sqlalchemy models, with no raw SQL required:

Base.metadata.create_all(engine)

### Running migrations 
""" these steps are then performed in the terminal, outside of your python code

1. alembic init migrations
` alembic init migrations `

2. edit alembic.ini to point to your database
` sqlalchemy.url = mysql+mysqlconnector://username:password@host/database_name `

3. edit env.py to point to your models
`from db_schema-name import Base`
`target_metadata = Base.metadata `

4. create a migration
` alembic revision --autogenerate -m "create tables" `

5. run the migration
` alembic upgrade head `

in addition, you can run ` alembic history ` to see the history of migrations
or you can run with the --sql flag to see the raw SQL that will be executed

so it could be like:
` alembic upgrade head --sql `

or if you then want to save it:
` alembic upgrade head --sql > migration.sql `

6. check the database

7. roll back: To roll back a migration in Alembic, you can use the downgrade command. 
The downgrade command allows you to revert the database schema to a previous 
migration version. Here's how you can use it:

`alembic downgrade <target_revision>` 

or if you want to roll back to the previous version, you can use the -1 flag:
`alembic downgrade -1`
 

"""