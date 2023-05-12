from db.db import sql

def select_all():
    print('meow')
    print (sql('SELECT * FROM fridge_items ORDER BY id'))
    return sql('SELECT * FROM fridge_items ORDER BY id')

def create(user_id, item_name):
    sql('INSERT INTO fridge_items(user_id, item_name) VALUES(%s, %s) RETURNING *', [user_id, item_name])