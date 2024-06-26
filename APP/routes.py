from flask import Blueprint, jsonify
from .models import fetch_employee_data

api = Blueprint('api', __name__)

@api.route('/employees', methods=['GET'])
def get_employees():
    data = fetch_employee_data()
    return jsonify({"data": data})
