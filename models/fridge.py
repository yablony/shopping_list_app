from db.db import sql

def select_all():
    return sql('SELECT * FROM fridge_items ORDER BY item_name')

def create(user_id, item_name):
    sql('INSERT INTO fridge_items(user_id, item_name) VALUES(%s, %s) RETURNING *', [user_id, item_name])

def update_info(id, user_id, item_name):
    sql('UPDATE fridge_items SET user_id=%s, item_name=%s WHERE id=%s RETURNING *', [user_id, item_name, id])

def delete_fridge_item(id):
    sql('DELETE FROM fridge_items WHERE id=%s RETURNING *', [id])

def delete_fridge(user_id):
    sql('DELETE FROM fridge_items WHERE user_id=%s RETURNING *', [user_id])