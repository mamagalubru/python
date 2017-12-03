#!C:\Python34\python.exe
# -*- coding: utf-8 -*-

import sqlite3

"""
teste quelques propriétés de base sqlite
"""

# se connecter
conn = sqlite3.connect("bts2facile.db")
print('Connexion effectuée')

# créer un curseur
cursor = conn.cursor()
print('Curseur créé')

# lire et afficher le comptage des enregistrements etudiants
cursor.execute("""SELECT count(*) FROM etudiants""")
nbr = cursor.fetchone()
print("Nombre d'enregistrements de la table etudiants : %s" %nbr)
# lire et afficher enregistrement par enregistrement
cursor.execute("""SELECT id, nom, prenom, mail, age, idClasse FROM etudiants""")
rows = cursor.fetchall()
for row in rows:
    print('Etudiant {0} a pour nom {1} {2}, pour mail {3}, pour age {4}, pour classe {5} '.format(row[0], row[1], row[2] , row[3], row[4], row[5]))

# lire et afficher le comptage des enregistrements classes
cursor.execute("""SELECT count(*) FROM classes""")
nbr = cursor.fetchone()
print("Nombre d'enregistrements de la table classes : %s" %nbr)
# lire et afficher enregistrement par enregistrement
cursor.execute("""SELECT id, sigle FROM classes""")
rows = cursor.fetchall()
for row in rows:
    print('Classe {0} de sigle {1} '.format(row[0], row[1]))

# lire et afficher le comptage des enregistrements classes
cursor.execute("""SELECT count(*) FROM classes, etudiants WHERE etudiants.idClasse = classes.id""")
nbr = cursor.fetchone()
print("Nombre d'enregistrements de la jointure des tables classes et etudiants : %s" %nbr)
# lire et afficher enregistrement par enregistrement
cursor.execute("""SELECT classes.sigle, etudiants.prenom, etudiants.nom FROM classes, etudiants WHERE etudiants.idClasse = classes.id""")
rows = cursor.fetchall()
for row in rows:
    print('Etudiant {1} {2} en classe {0} '.format(row[0], row[1] , row[2]))

# se déconnecter
conn.close()


