import mysql.connector
from flask import current_app

def get_db_connection():
    config = current_app.config
    conn = mysql.connector.connect(
        host=config['MYSQL_HOST'],
        user=config['MYSQL_USER'],
        password=config['MYSQL_PASSWORD'],
        database=config['MYSQL_DB']
    )
    return conn

def fetch_employee_data():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    query = """
    SELECT e.employeeNumber, e.lastName, e.firstName, e.extension, e.email, e.officeCode,
           e.jobTitle, o.city, o.phone, e.reportsTo, r.lastName as reportToLastName,
           r.firstName as reportToFirstName
    FROM employees e
    LEFT JOIN offices o ON e.officeCode = o.officeCode
    LEFT JOIN employees r ON e.reportsTo = r.employeeNumber
    """
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result
