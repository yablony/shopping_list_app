from flask import Blueprint
from controllers.shopping_list_controllers import index, new

shopping_list_routes = Blueprint('shopping_list_routes', __name__)

shopping_list_routes.route('/')(index)
shopping_list_routes.route('/new', methods=["POST"])(new)