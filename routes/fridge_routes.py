from flask import Blueprint
from controllers.fridge_controllers import update, new, edit, delete_item, delete_all, new_inside_the_edit_page

fridge_routes = Blueprint('fridge_routes', __name__)

fridge_routes.route('/new', methods=['POST'])(new)
fridge_routes.route('/update')(update)
fridge_routes.route('/<id>', methods=["POST"])(edit)
fridge_routes.route('/<id>/delete', methods=['POST'])(delete_item)
fridge_routes.route('/delete', methods=['POST'])(delete_all)
fridge_routes.route('/new_inside_edit', methods=['POST'])(new_inside_the_edit_page)