import sqlite3

connection = sqlite3.connect("gta.db")
cursor = connection.cursor()

cursor.execute("create table if not exists gta (year integer, name text, city text)")

release_list = [
    (2000, "The Dreamers", "New York"),
    (1995, "The Road", "London"),
    (2005, "The Great Adventure", "Paris"),
    (2010, "The Silent Revolution", "Berlin"),
    (2008, "The Forgotten Path", "Tokyo"),
    (2012, "City of Angels", "Los Angeles"),
    (1990, "The Hidden Valley", "Moscow"),
    (2015, "Echoes of the Past", "Sydney")
]

cursor.executemany("insert into gta values (?,?,?)", release_list)

for row in cursor.execute("select * from gta"):
    print(row)

connection.close()
