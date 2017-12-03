#!C:\Python34\python.exe
# -*- coding: utf-8 -*-

import sqlite3
from tkinter import *
from tkinter.messagebox import *
from tkinter.simpledialog import *

"""
teste les saisies sur widgets pour des données de base sqlite
"""

etudiantEnCours=0

def modifier(etudiantEnCours):
    print(etudiantEnCours)
    if askyesno('Confirmation', 'Êtes-vous sûr de vouloir modifier le prénom de cette ligne ?'):
        nouveauprenom = askstring('Confirmation','Nouveau Prénom')
        print(nouveauprenom)
        chaineSQL = "UPDATE etudiants SET prenom = '" + str(nouveauprenom) + "' WHERE id = " + str(etudiantEnCours)
        print(chaineSQL)
        #cursor.execute("""UPDATE etudiants SET prenom = ? WHERE id = ? """, (nouveauprenom, etudiantEnCours))
        cursor.execute(chaineSQL)
        conn.commit()
    else:
        showinfo('Titre 1', 'Vous avez peur de polluer la base de donnée !')
        showwarning('Titre 2', 'Tant pis, on y va ...')
        showerror("Titre 3", "Aha Aha Aha !!!")

# créer la fenêtre principale
fen1 = Tk()

# se connecter
conn = sqlite3.connect("bts2facile.db")
# créer un curseur
cursor = conn.cursor()
# lire enregistrement par enregistrement
cursor.execute("""SELECT classes.sigle, etudiants.prenom, etudiants.nom, etudiants.id FROM classes, etudiants WHERE etudiants.idClasse = classes.id""")
rows = cursor.fetchall()
ligne = 1
Label(fen1, text=str("CLASSE"), borderwidth=1, height = 5, width = 20, bg="yellow").grid(row=ligne, column=0)
Label(fen1, text=str("PRENOM"), borderwidth=1, height = 5, width = 20, bg="yellow").grid(row=ligne, column=1)
Label(fen1, text=str("  NOM "), borderwidth=1, height = 5, width = 20, bg="yellow").grid(row=ligne, column=2)
for row in rows:
    ligne = ligne + 1
    for colonne in range(3):
        Button(fen1, text=str(row[colonne]), borderwidth=1, height = 5, width = 20, bg="blue", command = lambda x=ligne:modifier(x)).grid(row=ligne, column=colonne)

# se déconnecter
# conn.close()

# boucle principale
fen1.mainloop()
