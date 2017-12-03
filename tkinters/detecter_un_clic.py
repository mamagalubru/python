#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Exercice utilisant la librairie graphique Tkinter
from tkinter import *

# définition de l'action à effectuer si l'utilisateur clicke
def pointeur(event):
   chaine['text'] = "Clic détecté en X =" + str(event.x) + ", Y =" + str(event.y)

root = Tk()
fen1 = Frame(root, width =200, height =150, bg="light yellow")
fen1.bind("<Button-1>", pointeur)
fen1.pack()
chaine = Label(root)
chaine.pack()

fen1.mainloop()
