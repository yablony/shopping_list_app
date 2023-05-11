from flask import Blueprint
from controllers.recipes_controllers import index

recipes_routes = Blueprint('recipes_routes', __name__)

recipes_routes.route('/')(index)