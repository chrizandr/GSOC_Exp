# For demo purposes we can use Sqlite3 as no installation is required

import sqlite3

conn = sqlite3.connect('../database.db')
print("Database created successfully")

conn.execute("CREATE TABLE products (P_id integer primary key autoincrement, description text, price real, name text );")
print("Table created successfully.")

conn.close()
