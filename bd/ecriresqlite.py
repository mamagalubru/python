#!C:\Python34\python.exe
# -*- coding: utf-8 -*-

import sqlite3

"""
teste quelques propriétés de création de base sqlite
"""

# se connecter
conn = sqlite3.connect("bts2facile.db")
print('Connexion effectuée')

# créer un curseur
cursor = conn.cursor()
print('Curseur créé')

# créer une table etudiants
cursor.execute("""
CREATE TABLE IF NOT EXISTS etudiants(
     id INTEGER PRIMARY KEY UNIQUE, nom TEXT, prenom TEXT, mail TEXT, age INTEGER, idClasse INTEGER)
""")
conn.commit()
print('Table etudiants créée')
# insérer des données des etudiants via paramètres
cursor.execute("""
INSERT INTO etudiants(id, nom, prenom, mail, age, idClasse) VALUES(?, ?, ?, ?, ?, ?)""", (1, "morane", "bob", "bm@easy.fr", 31, 1))
cursor.execute("""
INSERT INTO etudiants(id, nom, prenom, mail, age, idClasse) VALUES(?, ?, ?, ?, ?, ?)""", (2, "poe", "edgar", "ep@easy.fr", 40, 2))
conn.commit()
print('Table etudiants peuplée de 2 tuples via passage de paramètres')
# insérer des données des etudiants via dictionnaires
data = [{"id" : 3,"nom" : "mitch", "prenom" : "eddy", "mail" : "em@easy.fr", "age" : 32, "idClasse" : 1},{"id" : 4,"nom" : "coch", "prenom" : "eddy", "mail" : "ec@easy.fr", "age" : 65, "idClasse" : 1}]
cursor.executemany("""
INSERT INTO etudiants(id, nom, prenom, mail, age, idClasse) VALUES(:id, :nom, :prenom, :mail, :age, :idClasse)""", data)
conn.commit()
print('Table etudiants peuplée de 2 tuples via un dictionnaire')

# créer une table classe
cursor.execute("""
CREATE TABLE IF NOT EXISTS classes(
     id INTEGER PRIMARY KEY UNIQUE, sigle TEXT)
""")
conn.commit()
print('Table classes créée')
# insérer des données via paramètres
cursor.execute("""
INSERT INTO classes(id, sigle) VALUES(?, ?)""", ("1", "SIO15"))
cursor.execute("""
INSERT INTO classes(id, sigle) VALUES(?, ?)""", ("2", "SIO16"))
conn.commit()
print('Table classes peuplée de 2 tuples via des passage de paramètres')

# se déconnecter
conn.close()

