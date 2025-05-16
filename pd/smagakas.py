import sqlite3
DB = 'noliktava.db'
conn = sqlite3.connect(DB)
cursor = conn.cursor()
cursor.execute('''
    SELECT id, nosaukums, skaitlis, svars FROM preces
    ORDER BY svars DESC LIMIT 4 
''')
smagakas_preces = cursor.fetchall()
conn.commit()
conn.close()
print("4 smagākās preces:")
for prece in smagakas_preces:
    print(prece)