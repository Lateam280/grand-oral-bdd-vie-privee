import sqlite3
from faker import Faker

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

fake = Faker(locale="fr_FR")
liste_id = []
for user in range(50):
    nom = fake.last_name()
    prenom = fake.first_name()
    email = fake.email()
    mot_de_passe = fake.password()
    date_inscription = str(fake.date_this_decade())
    
    cursor.execute("INSERT INTO utilisateurs (nom,prenom,email,mot_de_passe,date_inscription) VALUES (?,?,?,?,?)", (nom,prenom,email,mot_de_passe,date_inscription))

    id = cursor.lastrowid
    liste_id.append(id)

conn.commit()

    


