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


words = {}
list_id = []

while True:
    number = random.randint(1, 59)
    if number not in list_id:
        list_id.append(number)
    if len(list_id) == 10:
        break

cursor.execute("SELECT * FROM Dictionary")

for i in cursor.fetchall():
    if int(f'{i[0]}') in list_id:
        words[f'{i[1]}'] = f'{i[2]}'


print(list_id)
for key, value in words.items():
    print(f'{key}: {value}')

