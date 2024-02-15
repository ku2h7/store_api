from flask import Blueprint, jsonify, request
from app.utils.database import db
from app.models.customers import Customers

customers_blueprint = Blueprint('customers_endpoint', __name__)

@customers_blueprint.route("/", methods=["GET"])
def get_list_customers():
  try:
    customers = Customers.query.all()
    return [customer.as_dict() for customer in customers], 200
  except Exception as e:
    return e, 500

@customers_blueprint.route("/", methods=["POST"])
def create_customer():
  try:
    data = request.json

    customer = Customers()
    customer.name = data["name"]
    customer.email = data["email"]
    customer.phone = data["phone"]
    db.session.add(customer)
    db.session.commit()
    return 'berhasil', 200
  except Exception as e:
    return e, 500