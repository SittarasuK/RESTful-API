# db_config.py
import MySQLdb

def get_db_connection():
    connection = MySQLdb.connect(
        host="localhost",   # Database host
        user="root",        # Database username
        password="Kcg@1234", # Database password
        database="company_user_db"  # Your database name
    )
    return connection
