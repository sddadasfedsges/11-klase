import sqlite3
DB = 'noliktava.db'
conn = sqlite3.connect(DB)
cursor = conn.cursor()
dati = []
for i in range(8):
    print(f'\nIevadi {i+1}. ierakstu:')
    nosaukums = input('nosaukums: ')
    skaitlis = input('skaitlis: ')
    svars = int(input('svars: '))
    dati.append((nosaukums, skaitlis, svars))
cursor.executemany('''
    INSERT INTO preces (nosaukums, skaitlis, svars)
    VALUES (?, ?, ?)
''', dati)
conn.commit()
conn.close()
print('Tika pievienoti 8 ieraksti.')
