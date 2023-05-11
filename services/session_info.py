from flask import session
from models.users_models import find_user_by_id

def current_user():
    if session.get('user_id'):
        return find_user_by_id(session['user_id'])
    else:
        return None