import mysql.connector
from mysql.connector import Error


def create_database():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="rafiu"
        )
        cursor = connection.cursor()

        # Create the hospital_portal database
        cursor.execute("CREATE DATABASE IF NOT EXISTS hospital_portal")
        print("Database 'hospital_portal' created successfully")

    except Error as e:
        print("Error:", e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


def create_tables():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="rafiu",
            database="hospital_portal"
        )
        cursor = connection.cursor()

        # Creating the doctors table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS doctors (
                doctor_id INT AUTO_INCREMENT PRIMARY KEY,
                doctor_name VARCHAR(45) NOT NULL,
                specialization VARCHAR(45) NOT NULL
            )
        """)

        # Creating the patients table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS patients (
                patient_id INT AUTO_INCREMENT PRIMARY KEY,
                patient_name VARCHAR(45) NOT NULL,
                age INT NOT NULL,
                admission_date DATE,
                discharge_date DATE
            )
        """)

        # Creating the appointments table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS appointments (
                appointment_id INT AUTO_INCREMENT PRIMARY KEY,
                patient_id INT NOT NULL,
                doctor_id INT NOT NULL,
                appointment_date DATE NOT NULL,
                appointment_time DECIMAL NOT NULL,
                FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
                FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id)
            )
        """)

        print("Tables created successfully")

    except Error as e:
        print("Error:", e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


def insert_sample_data():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="rafiu",
            database="hospital_portal"
        )
        cursor = connection.cursor()

        # Inserting sample data into the doctors table
        cursor.execute("""
            INSERT INTO doctors (doctor_name, specialization)
            VALUES
                ('Dr. Smith', 'Cardiology'),
                ('Dr. Johnson', 'Orthopedics'),
                ('Dr. Brown', 'Pediatrics')
        """)

        # Inserting sample data into the patients table
        cursor.execute("""
            INSERT INTO patients (patient_name, age, admission_date, discharge_date)
            VALUES
                ('Maria Jozef', 67, '2023-10-01', '2023-10-07'),
                ('John Doe', 45, '2023-09-15', '2023-09-22'),
                ('Alice Smith', 30, '2023-11-05', '2023-11-12')
        """)

        print("Sample data inserted successfully")

    except Error as e:
        print("Error:", e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


# Creating the database
create_database()

# Creating the tables
create_tables()

# Inserting sample data
insert_sample_data()
