# models.py
from db_config import get_db_connection


def create_tables():
    connection = get_db_connection()
    cursor = connection.cursor()

    # Create companies table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS companies (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        address VARCHAR(255),
        latitude DOUBLE,
        longitude DOUBLE
    );
    """)

    # Create users table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        first_name VARCHAR(255) NOT NULL,
        last_name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL UNIQUE,
        designation VARCHAR(255),
        date_of_birth DATE,
        active BOOLEAN DEFAULT TRUE,
        company_id INT,
        FOREIGN KEY (company_id) REFERENCES companies(id)
    );
    """)

    connection.commit()
    connection.close()
