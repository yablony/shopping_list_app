from flask import render_template, request, redirect, session
from services.session_info import current_user
from models.shopping_list import select_all, create, update_info, delete_shopping_item, delete_shopping_list

def index():
    if session == {}:
        shopping_list = select_all(0)
    else: 
        shopping_list = select_all(session['user_id'])
    return render_template('/shopping_list/index.html', current_user = current_user(), shopping_list = shopping_list)

def new():
    item_name = request.form.get('item_name')
    image_url = request.form.get('image_url')
    create(session['user_id'], item_name, image_url)
    return redirect('/')

def update():
    shopping_list = select_all()
    return render_template('/shopping_list/edit.html', shopping_list = shopping_list)

def edit(id):
    item_name = request.form.get('item_name')
    image_url = request.form.get('image_url')
    update_info(id, session['user_id'], item_name, image_url)
    return redirect('/')

def delete_item(id):
    delete_shopping_item(id)
    return redirect('/')

def delete_all():
    delete_shopping_list(session['user_id'])
    return redirect('/')