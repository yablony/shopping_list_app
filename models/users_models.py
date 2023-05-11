from db.db import sql
import bcrypt

def create_new_user(name, email, password):
    password_digest = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    sql("INSERT INTO users(name, email, password_digest) VALUES(%s, %s, %s) RETURNING *", [name, email, password_digest])

def find_user_by_email(email):
    users = sql('SELECT * FROM users WHERE email = %s', [email])

    if len(users) > 0:
        return users[0]
    else:
        return None

def find_user_by_id(id):
    users = sql('SELECT * FROM users WHERE id = %s', [id])
    return users[0]