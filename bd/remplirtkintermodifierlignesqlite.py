#!C:\Python34\python.exe
# -*- coding: utf-8 -*-

import sqlite3
from tkinter import *
from tkinter.messagebox import *
from tkinter.simpledialog import *

"""
teste les saisies sur widgets pour des données de base sqlite
"""

#etudiantEnCours=0
#colonneEnCours=0

def afficherEtudiants():
    # lire enregistrement par enregistrement
    cursor.execute("""SELECT classes.sigle, etudiants.prenom, etudiants.nom, etudiants.id FROM classes, etudiants WHERE etudiants.idClasse = classes.id""")
    rows = cursor.fetchall()
    ligne = 1
    for row in rows:
        ligne = ligne + 1
        for colonne in range(3):
            Button(fen1, text=str(row[colonne]), borderwidth=1, height = 5, width = 20, bg="blue", command = lambda x=ligne-1,y=colonne:modifier(x,y)).grid(row=ligne, column=colonne)

def modifier(etudiantEnCours,colonneEnCours):
    if colonneEnCours == 2:
        # saisie du nouveau nom
        nouveaunom = askstring('Confirmation','Nouveau Nom')
        chaineSQL = "UPDATE etudiants SET nom = '" + str(nouveaunom) + "' WHERE id = " + str(etudiantEnCours)
        cursor.execute(chaineSQL)
        conn.commit()
    elif colonneEnCours == 1:
        # saisie du nouveau prénom
        nouveauprenom = askstring('Confirmation','Nouveau Prénom')
        cursor.execute("""UPDATE etudiants SET prenom = ? WHERE id = ? """, (nouveauprenom, etudiantEnCours))
        conn.commit()
    else :
        # saisie de la nouvelle classe
        nouvelleclasse = askstring('Confirmation','Nouvelle Classe (SIO15==> 1 ou SIO16==> 2')
        if (nouvelleclasse == '1' or nouvelleclasse == '2'):
            cursor.execute("""UPDATE etudiants SET idClasse = ? WHERE id = ? """, (nouvelleclasse, etudiantEnCours))
            conn.commit()
    # afficher les lignes lues
    afficherEtudiants()

#### programme peincipal
# créer la fenêtre principale
fen1 = Tk()
# se connecter à la base de données
conn = sqlite3.connect("bts2facile.db")
# créer un curseur
cursor = conn.cursor()
# afficher une première ligne
Label(fen1, text=str("CLASSE"), borderwidth=1, height = 5, width = 20, bg="yellow").grid(row=1, column=0)
Label(fen1, text=str("PRENOM"), borderwidth=1, height = 5, width = 20, bg="yellow").grid(row=1, column=1)
Label(fen1, text=str("  NOM "), borderwidth=1, height = 5, width = 20, bg="yellow").grid(row=1, column=2)
# afficher les lignes lues
afficherEtudiants()

# plus tard si demande user se déconnecter
# conn.close()

# boucle principale
fen1.mainloop()
