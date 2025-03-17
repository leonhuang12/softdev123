import sqlite3
from flask_login import UserMixin
from flask import g

DATABASE = 'site.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def query_db(query, args=(), one=False):
    cursor = get_db().execute(query, args)
    rv = cursor.fetchall()
    cursor.close()
    return (rv[0] if rv else None) if one else rv

def init_db():
    with sqlite3.connect(DATABASE) as conn:
        with open('schema.sql') as f:
            conn.executescript(f.read())

def user_loader(user_id):
    user = query_db('SELECT * FROM user WHERE id = ?', [user_id], one=True)
    if user:
        return User(id=user[0], username=user[1], email=user[2], password=user[3])
    return None

class User(UserMixin):
    def __init__(self, id, username, email, password):
        self.id = id
        self.username = username
        self.email = email
        self.password = password