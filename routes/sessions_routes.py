from flask import Blueprint
from controllers.sessions_controllers import new_session, check_user, delete, guest_login

sessions_routes = Blueprint('sessions_routes', __name__)

sessions_routes.route('/new')(new_session)
sessions_routes.route('', methods=['POST'])(check_user)
sessions_routes.route('/delete', methods=['POST'])(delete)
sessions_routes.route('/guest')(guest_login)