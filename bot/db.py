
import sqlite3
import os
from datetime import datetime

os.makedirs("database", exist_ok=True)
conn = sqlite3.connect("database/users.db", check_same_thread=False)

def get_all_users():
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id TEXT PRIMARY KEY, name TEXT, banned INTEGER, date TEXT)")
    return cursor.fetchall()

def mark_user_banned(user_id):
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET banned = 1 WHERE id = ?", (user_id,))
    conn.commit()
    
def add_user_if_not_exists(user_id, username):
    c = conn.cursor()
    c.execute("SELECT id FROM users WHERE id = ?", (user_id,))
    if c.fetchone() is None:
        c.execute("INSERT INTO users (id, name, banned) VALUES (?, ?, 0)", (user_id, username))
        conn.commit()
