from flask import Flask, render_template, request
from sqlalchemy import create_engine, text 
import os
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

app = Flask(__name__)

@app.route('/')
def index():
    # Establish a database connection
    with engine.connect() as connection:
        # Execute an SQL query to fetch data (replace this with your query)
        query1 = text('SELECT * FROM patients')
        query2 = text('SELECT * FROM doctors')

        result1 = connection.execute(query1)
        result2 = connection.execute(query2)

        # Fetch all rows of data
        db_data1 = result1.fetchall()
        db_data2 = result2.fetchall()

    return render_template('index.html', data1=db_data1, data2 = db_data2)


if __name__ == '__main__':
    app.run(debug=True)