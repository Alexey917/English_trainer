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
right_answers = {}

while True:
    number = random.randint(1, 374)
    if number not in list_id:
        list_id.append(number)
    if len(list_id) == 30:
        break

cursor.execute("SELECT * FROM Dictionary")

for i in cursor.fetchall():
    if int(f'{i[0]}') in list_id:
        words[f'{i[1]}'] = f'{i[2]}'


def check_knowledge():
    result = 0
    for key, value in words.items():
        print(f'{key}')
        translate = input("Переведите:\n->")
        if value == translate:
            result += 1
        else:
            right_answers[key] = value
    print(f'Ваш результат: {result/len(list_id)*100}%\n')


def mistakes():
    for key, value in right_answers.items():
        print(f'{key}: {value}')


check_knowledge()
mistakes()
