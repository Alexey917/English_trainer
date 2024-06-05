import random
import sqlite3

con = sqlite3.connect("Dictionary.db")
cursor = con.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Dictionary
    (
        Id INTEGER PRIMARY KEY AUTOINCREMENT,
        Word TEXT NOT NULL,
        Translate TEXT NOT NULL
    )""")


end = 30
words = []
list_id = []

for i in range(0, end):
    list_id.append(random.randint(1, 61))

for i in range(0, end):
    pass

print(list_id)
