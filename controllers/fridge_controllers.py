from flask import render_template, request, redirect, session
from services.session_info import current_user
from models.fridge import select_all_fridge, create, update_info, delete_fridge_item, delete_fridge

def update():
    fridge = select_all_fridge(session['user_id'])
    return render_template('/fridge/view_and_edit.html', current_user = current_user(), fridge = fridge)

def new():
    item_name = request.form.get('item_name')
    fridge = select_all_fridge(session['user_id'])
    fridge_list = []
    for fridge_item in fridge:
        fridge_list.append(fridge_item['item_name'])
    if item_name != '' and item_name not in fridge_list:
        create(session['user_id'], item_name)
    return redirect('/')

def new_inside_the_edit_page():
    item_name = request.form.get('item_name')
    fridge = select_all_fridge(session['user_id'])
    fridge_list = []
    for fridge_item in fridge:
        fridge_list.append(fridge_item['item_name'])
    if item_name != '' and item_name not in fridge_list:
        create(session['user_id'], item_name)
    return redirect('/fridge/update')

def edit(id):
    item_name = request.form.get('item_name')
    update_info(id, session['user_id'], item_name)
    return redirect('/fridge/update')

def delete_item(id):
    delete_fridge_item(id)
    return redirect('/fridge/update')

def delete_all():
    delete_fridge(session['user_id'])
    return redirect('/fridge/update')