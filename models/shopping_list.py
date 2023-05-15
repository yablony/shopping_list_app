from db.db import sql

def select_all(user_id):
    return sql('SELECT * FROM shopping_list WHERE user_id=%s ORDER BY id DESC', [user_id])

def create(user_id, item_name):
    sql('INSERT INTO shopping_list(user_id, item_name) VALUES(%s, %s) RETURNING *', [user_id, item_name])

def update_info(id, user_id, item_name):
    sql('UPDATE shopping_list SET user_id=%s, item_name=%s WHERE id=%s RETURNING *', [user_id, item_name, id])

def delete_shopping_item(id):
    sql('DELETE FROM shopping_list WHERE id=%s RETURNING *', [id])

def delete_shopping_list(user_id):
    sql('DELETE FROM shopping_list WHERE user_id=%s RETURNING *', [user_id])

def delete_shopping_item_by_name(item_name):
    sql('DELETE FROM shopping_list WHERE item_name=%s RETURNING *', [item_name])