#! /usr/bin/env python

# Exercice utilisant la librairie graphique Tkinter et le module math
from tkinter import *
from math import *

# définition de l'action à effectuer si l'utilisateur actionne
# la touche "enter" alors qu'il édite le champ d'entrée :
def evaluer(event):
   chaine['text'] = "Résultat = " + str(eval(entree.get()))
   print(chaine['text'])

# ----- Programme principal : -----
fenetre = Tk()
entree = Entry(fenetre)
entree.bind("<Return>",evaluer)
chaine = Label(fenetre)
entree.pack()
chaine.pack()
fenetre.mainloop()
