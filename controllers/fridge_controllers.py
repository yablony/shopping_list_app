from flask import render_template, request, redirect, session
from services.session_info import current_user
from models.fridge import select_all, create

def update():
    fridge = select_all()
    return render_template('/fridge/view_and_edit.html', current_user = current_user(), fridge = fridge)

def new():
    item_name = request.form.get('item_name')
    create(session['user_id'], item_name)
    return redirect('/')
