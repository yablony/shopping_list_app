from db.db import sql
import bcrypt

def create_new_user(name, email, password):
    password_digest = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    sql("INSERT INTO users(name, email, password_digest) VALUES(%s, %s, %s) RETURNING *", [name, email, password_digest])