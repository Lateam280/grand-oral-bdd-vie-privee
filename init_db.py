import sqlite3
connexion = sqlite3.connect('database.db')
cursor = connexion.cursor()

with open('schema.sql', 'r') as f:
    schema = f.read()

cursor.executescript(schema)

