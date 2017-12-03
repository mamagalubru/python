#!C:\Python34\python.exe
# -*- coding: utf-8 -*-

import sqlite3
from tkinter import *

"""
teste les remplissages de widgets par des données de base sqlite
"""

# créer la fenêtre
fen1 = Tk()

# se connecter
conn = sqlite3.connect("bts2facile.db")
# créer un curseur
cursor = conn.cursor()
# lire enregistrement par enregistrement
cursor.execute("""SELECT classes.sigle, etudiants.prenom, etudiants.nom FROM classes, etudiants WHERE etudiants.idClasse = classes.id""")
rows = cursor.fetchall()
print("lecture pour debug")
for row in rows:
    print('{0} : {1} - {2}'.format(row[0], row[1], row[2]))

ligne = 1
Label(fen1, text=str("CLASSE"), borderwidth=1, height = 5, width = 20, bg="yellow").grid(row=ligne, column=0)
Label(fen1, text=str("PRENOM"), borderwidth=1, height = 5, width = 20, bg="yellow").grid(row=ligne, column=1)
Label(fen1, text=str("  NOM "), borderwidth=1, height = 5, width = 20, bg="yellow").grid(row=ligne, column=2)
for row in rows:
    ligne = ligne + 1
    for colonne in range(3):
        Button(fen1, text=str(row[colonne]), borderwidth=1, height = 5, width = 20, bg="blue").grid(row=ligne, column=colonne)

# se déconnecter
conn.close()

# boucle principale
fen1.mainloop()
