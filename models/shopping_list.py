from db.db import sql

def select_all(user_id):
    return sql('SELECT * FROM shopping_list WHERE user_id=%s ORDER BY id DESC', [user_id])

def create(user_id, item_name, image_url):
    sql('INSERT INTO shopping_list(user_id, item_name, image_url) VALUES(%s, %s, %s) RETURNING *', [user_id, item_name, image_url])

def update_info(id, user_id, item_name, image_url):
    sql('UPDATE shopping_list SET user_id=%s, item_name=%s, image_url=%s WHERE id=%s RETURNING *', [user_id, item_name, image_url, id])

def delete_shopping_item(id):
    sql('DELETE FROM shopping_list WHERE id=%s RETURNING *', [id])

def delete_shopping_list(user_id):
    sql('DELETE FROM shopping_list WHERE user_id=%s RETURNING *', [user_id])