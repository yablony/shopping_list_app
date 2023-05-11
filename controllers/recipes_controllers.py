from flask import render_template, request, redirect
from services.session_info import current_user

def index():
    return render_template('/recipes/index.html', current_user=current_user())