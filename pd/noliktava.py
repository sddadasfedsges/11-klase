import sqlite3
DB = 'noliktava.db'
conn = sqlite3.connect(DB)
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS preces (
               id INTEGER PRIMARY KEY  AUTOINCREMENT,
               nosaukums TEXT NOT NULL,
               skaitlis TEXT NOT NULL,
               svars INTEGER NOT NULL
               )
''')
conn.commit()
conn.close()
print('Tabula Rezultāti norada')