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
    print ("Database projets connexion effectuée")

    # créer un curseur
    cur = con.cursor()
    print ("Database projets curseur créé")

    # lire la version mysql
    cur.execute("SELECT VERSION()")
    ver = cur.fetchone()
    print ("Database projets version : %s " % ver)
    # lire le nom de la database 
    cur.execute("SELECT DATABASE()")
    ver = cur.fetchone()
    print ("Database : %s " % ver)
    
except mdb.Error as e:
    # afficher erreur  
    print ("Erreur diverse %d: %s" % (e.args[0],e.args[1]))
    
finally:            
    con.close()
