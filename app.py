from dotenv import load_dotenv
load_dotenv()

import os

from flask import Flask, redirect
from routes.users_routes import users_routes
from routes.recipes_routes import recipes_routes
from routes.sessions_routes import sessions_routes
from routes.shopping_list_routes import shopping_list_routes
from routes.fridge_routes import fridge_routes

SECRET_KEY = os.environ.get("FLASK_SECRET_KEY", "pretend key for testing only")

app = Flask(__name__)

app.config['SECRET_KEY'] = SECRET_KEY

app.register_blueprint(users_routes, url_prefix = "/users")
app.register_blueprint(recipes_routes, url_prefix="/recipes")
app.register_blueprint(sessions_routes, url_prefix="/sessions")
app.register_blueprint(shopping_list_routes, url_prefix="/shopping_list")
app.register_blueprint(fridge_routes, url_prefix="/fridge")

@app.route('/')
def index():
    return redirect('/shopping_list')