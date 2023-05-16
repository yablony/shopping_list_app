from flask import render_template, request, redirect, session
from services.session_info import current_user
from models.shopping_list import select_all, create, update_info, delete_shopping_item, delete_shopping_list, delete_shopping_item_by_name
from models.fridge import select_all_fridge

def index():
    if session == {}:
        shopping_list = select_all(0)
    else: 
        shopping_list = select_all(session['user_id'])
        fridge = select_all_fridge(session['user_id'])
        fridge_list = []
        for fridge_item in fridge:
            fridge_list.append(fridge_item['item_name'])
        for item in shopping_list:
            if item['item_name'] in fridge_list:
                delete_shopping_item_by_name(item['item_name'])
    return render_template('/shopping_list/index.html', current_user = current_user(), shopping_list = shopping_list)

def new():
    item_name = request.form.get('item_name')
    shopping_list = select_all(session['user_id'])
    fridge = select_all_fridge(session['user_id'])
    list_of_all_shopping_items = []
    fridge_list = []
    for fridge_item in fridge:
        fridge_list.append(fridge_item['item_name'])
    for shopping_item in shopping_list:
        list_of_all_shopping_items.append(shopping_item['item_name'])
    if item_name != '' and item_name not in fridge_list and item_name not in list_of_all_shopping_items:
        create(session['user_id'], item_name)
    return redirect('/')

def update():
    shopping_list = select_all(session['user_id'])
    return render_template('/shopping_list/edit.html', shopping_list = shopping_list)

def edit(id):
    item_name = request.form.get('item_name')
    update_info(id, session['user_id'], item_name)
    return redirect('/')

def delete_item(id):
    delete_shopping_item(id)
    return redirect('/')

def delete_all():
    delete_shopping_list(session['user_id'])
    return redirect('/')

def add_ingredients():
    ingredients = request.form.getlist('ingredients_list')
    shopping_list = select_all(session['user_id'])
    fridge = select_all_fridge(session['user_id'])
    list_of_all_shopping_items = []
    fridge_list = []
    for fridge_item in fridge:
        fridge_list.append(fridge_item['item_name'])
    for shopping_item in shopping_list:
        list_of_all_shopping_items.append(shopping_item['item_name'])
    # ingredients needs to be a list for this to work
    # for every time a <li> is written I want it to be added to this list that will be sent together with the form
    for item_name in ingredients:
        if item_name not in fridge_list and item_name not in list_of_all_shopping_items: # checks if the item exists in the fridge or in the shopping list already
            create(session['user_id'], item_name)
    return redirect('/')