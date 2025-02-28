import sqlite3

connection = sqlite3.connect("gta.db")
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS gta (year INTEGER, name TEXT, city TEXT)")

release_list = [
    (2000, "The Dreamers", "Paris"),
    (1995, "The Road", "London"),
    (2005, "The Great Adventure", "Paris"),
    (2010, "The Silent Revolution", "Berlin"),
    (2008, "The Forgotten Path", "Tokyo"),
    (2012, "City of Angels", "Paris"),
    (1990, "The Hidden Valley", "Moscow"),
    (2015, "Echoes of the Past", "Sydney")
]

cursor.executemany("INSERT INTO gta VALUES (?,?,?)", release_list)

for row in cursor.execute("SELECT * FROM gta"):
    print(row)

print("****************************")
cursor.execute("SELECT * FROM gta WHERE city=:c", {"c": "Paris"})
gta_search = cursor.fetchall()
print(gta_search)

cursor.execute("CREATE TABLE IF NOT EXISTS cities (gta_city TEXT, real_city TEXT)")
cursor.execute("INSERT INTO cities VALUES (?,?)", ("Paris", "Paris, IDF"))
cursor.execute("SELECT * FROM cities WHERE real_city=:c", {"c": "Paris, IDF"})
cities_search = cursor.fetchall()
print(cities_search)

print("****************************")
for i in gta_search:
    adjusted = [cities_search[0][1] if value==cities_search[0][0] else value for value in i]
    print(adjusted)

connection.close()
