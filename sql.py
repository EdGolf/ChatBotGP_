import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id VARCHAR(255),
        lang VARCHAR(255)
    )
''')
               
conn.commit()
conn.close()

print("Таблица создана успешно.")