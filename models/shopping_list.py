from db.db import sql

def select_all():
    return sql('SELECT * FROM shopping_list ORDER BY id')

def create(user_id, item_name, image_url):
    sql('INSERT INTO shopping_list(user_id, item_name, image_url) VALUES(%s, %s, %s) RETURNING *', [user_id, item_name, image_url])