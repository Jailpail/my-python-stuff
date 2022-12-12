import sqlite3
connection = sqlite3.connect("temperature.sl3", 5)
cur = connection.cursor()
cur.execute("CREATE TABLE first_table (temperature TEXT time TEXT);")
connection.commit()
connection.close()