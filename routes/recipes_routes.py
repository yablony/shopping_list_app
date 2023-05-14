from flask import Blueprint
from controllers.recipes_controllers import search_recipes_in_api, view_recipe_info_in_api

recipes_routes = Blueprint('recipes_routes', __name__)

recipes_routes.route('/search')(search_recipes_in_api)
recipes_routes.route('/<id>')(view_recipe_info_in_api)