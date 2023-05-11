from flask import render_template, redirect, request
from models.users_models import create_new_user

def new():
    return render_template('/users/new.html')

def create():
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')
    create_new_user(name, email, password)
    return redirect('/')