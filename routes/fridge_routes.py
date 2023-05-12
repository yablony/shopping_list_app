from flask import Blueprint
from controllers.fridge_controllers import update, new

fridge_routes = Blueprint('fridge_routes', __name__)

fridge_routes.route('/new', methods=['POST'])(new)
fridge_routes.route('/update')(update)