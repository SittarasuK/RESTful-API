# app.py
from flask import Flask, request, jsonify
from models import create_tables
from db_config import get_db_connection

app = Flask(__name__)

# Create tables if not already created
create_tables()


# Endpoint to list all companies
@app.route('/companies', methods=['GET'])
def list_companies():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM companies")
    companies = cursor.fetchall()
    connection.close()

    return jsonify(companies)


# Endpoint to create a company
@app.route('/companies', methods=['POST'])
def create_company():
    data = request.get_json()
    name = data['name']
    address = data['address']
    latitude = data['latitude']
    longitude = data['longitude']

    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO companies (name, address, latitude, longitude) VALUES (%s, %s, %s, %s)",
                   (name, address, latitude, longitude))
    connection.commit()
    connection.close()

    return jsonify({"message": "Company created successfully"}), 201


# Endpoint to get a specific company by ID
@app.route('/companies/<int:id>', methods=['GET'])
def get_company(id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM companies WHERE id = %s", (id,))
    company = cursor.fetchone()
    connection.close()

    if company:
        return jsonify(company)
    return jsonify({"message": "Company not found"}), 404


# Endpoint to update a company
@app.route('/companies/<int:id>', methods=['PUT'])
def update_company(id):
    data = request.get_json()
    name = data['name']
    address = data['address']
    latitude = data['latitude']
    longitude = data['longitude']

    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("""
    UPDATE companies SET name = %s, address = %s, latitude = %s, longitude = %s WHERE id = %s
    """, (name, address, latitude, longitude, id))
    connection.commit()
    connection.close()

    return jsonify({"message": "Company updated successfully"})


# Endpoint to delete a company
@app.route('/companies/<int:id>', methods=['DELETE'])
def delete_company(id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM companies WHERE id = %s", (id,))
    connection.commit()
    connection.close()

    return jsonify({"message": "Company deleted successfully"})


# Endpoint to list all users
@app.route('/users', methods=['GET'])
def list_users():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    connection.close()

    return jsonify(users)


# Endpoint to create a user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    first_name = data['first_name']
    last_name = data['last_name']
    email = data['email']
    designation = data['designation']
    date_of_birth = data['date_of_birth']
    company_id = data['company_id']

    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("""
    INSERT INTO users (first_name, last_name, email, designation, date_of_birth, company_id) 
    VALUES (%s, %s, %s, %s, %s, %s)
    """, (first_name, last_name, email, designation, date_of_birth, company_id))
    connection.commit()
    connection.close()

    return jsonify({"message": "User created successfully"}), 201


# Endpoint to deactivate a user
@app.route('/users/<int:id>/deactivate', methods=['PUT'])
def deactivate_user(id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE users SET active = FALSE WHERE id = %s", (id,))
    connection.commit()
    connection.close()

    return jsonify({"message": "User deactivated successfully"})


if __name__ == '__main__':
    app.run(debug=True)
