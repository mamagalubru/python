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

    # créer un curseur
    cur = con.cursor()

    # lire et afficher le comptage des enregistrements
    cur.execute("""SELECT count(*) FROM etudiants""")
    nbr = cur.fetchone()
    print("Nombre d'enregistrements de la table : %s" %nbr)

    # lire et afficher enregistrement par enregistrement
    cur.execute("""SELECT id, nom, prenom, mail, age FROM etudiants""")
    rows = cur.fetchall()
    for row in rows:
        print('{0} => {1} - {2} : {3} - {4} '.format(row[0], row[1], row[2] , row[3], row[4]))

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
