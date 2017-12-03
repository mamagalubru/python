#!C:\Python34\python.exe
# -*- coding: utf-8 -*-

import pymysql as mdb
import sys

"""
teste quelques propriétés de base mysql
"""

try:
    # se connecter
    con = mdb.connect('localhost', 'mamagalubru', 'rialto2013', 'projets');
    print('Connexion effectuée')

    # créer un curseur
    cur = con.cursor()
    print('Curseur créé')

    # créer une table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS etudiants(
     id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
     nom VARCHAR(50), prenom VARCHAR(50), mail VARCHAR(100), age INT)
    """)
    con.commit()
    print('Table créée')

    # insérer des données via valeurs
    cur.execute("""
    INSERT INTO etudiants(nom, prenom, mail, age) VALUES('morane', 'bob', 'bm@easyschool.fr', 31)""")
    cur.execute("""
    INSERT INTO etudiants(nom, prenom, mail, age) VALUES('poe', 'edgar', 'ep@easyschool.fr', 40)""")
    con.commit()
    print('Table peuplée de 2 tuples via des valeurs directes')

    # insérer des données via paramètres
    cur.execute("""
    INSERT INTO etudiants (nom, prenom, mail, age) VALUES (%s, %s, %s, %s)""",
                ('léponge', 'bob', 'bl@easyschool.fr', '21'))
    cur.execute("""
    INSERT INTO etudiants (nom, prenom, mail, age) VALUES (%s, %s, %s, %s)""",
                ('sleigh', 'bob', 'bs@easyschool.fr', '11'))
    con.commit()
    print('Table peuplée de 2 tuples via des valeurs paramétrées')

    # insérer des données via dictionnaires
    
    data = {"nom" : "mitchell", "prenom" : "eddy", "mail" : "em@easyschool.fr", "age" : "32"}
    cur.execute("""
    INSERT INTO etudiants(nom, prenom, mail, age) VALUES(%(nom)s, %(prenom)s, %(mail)s, %(age)s)""", data)
    con.commit()
    print('Table peuplée de 1 tuple via un dictionnaire')

except mdb.DataError as e:
    # afficher erreur
    print ("Erreur Data %d: %s" % (e.args[0],e.args[1]))

except mdb.OperationalError as e:
    # afficher erreur
    print ("Erreur Programming %d: %s" % (e.args[0],e.args[1]))

except mdb.InternalError as e:
    # afficher erreur
    print ("Erreur interne %d: %s" % (e.args[0],e.args[1]))

except mdb.ProgrammingError as e:
    # afficher erreur
    print ("Erreur Programming %d: %s" % (e.args[0],e.args[1]))

except mdb.MySQLError as e:
    # afficher erreur
    print ("Erreur MySQL %d: %s" % (e.args[0],e.args[1]))

except mdb.Error as e:
    # afficher erreur
    print ("Erreur diverse %d: %s" % (e.args[0],e.args[1]))

finally:
    con.close()
