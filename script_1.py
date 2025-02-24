import sqlite3

connection = sqlite3.connect('store_transactions.db')

cursor = connection.cursor()

command1 = """CREATE TABLE IF NOT EXISTS
stores(store_id INTEGER PRIMARY KEY, location TEXT)"""

cursor.execute(command1)

command2 = """CREATE TABLE IF NOT EXISTS
purchases(purchase_id INTEGER PRIMARY KEY, store_id INTEGER, total_cost FLOAT,
FOREIGN KEY(store_id) REFERENCES stores(store_id))"""

cursor.execute(command2)

cursor.execute("INSERT INTO stores VALUES (21, 'Paris, IDF')")
cursor.execute("INSERT INTO stores VALUES (95, 'Toulouse, OCC')")
cursor.execute("INSERT INTO stores VALUES (64, 'Bordeaux, NAQ')")

cursor.execute("INSERT INTO purchases VALUES (54, 21, 15.49)")
cursor.execute("INSERT INTO purchases VALUES (23, 64, 21.12)")

cursor.execute("SELECT * FROM purchases")

results = cursor.fetchall()
print(results)

cursor.execute("UPDATE purchases SET total_cost = 9.78 WHERE purchase_id = 54")
print(results)