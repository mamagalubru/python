#! /usr/bin/python
# -*- coding: utf-8 -*-

# cette version me sert à tester git et github
# chaque modification sur un poste doit être validée via git sur ce poste (commit)
# chaque modification sur un poste doit être poussée via git sur github (push) par exemple sur https://github.com/mamagalubru/essai
# chaque modification peut ensuite être récupérée via git sur un autre poste (pull)

"""
tests de rebonds de balle sur une raquette poussé le 21 mars à 22h
"""

import time
import random
from tkinter import *

"""
la classe balle gère ses mouvements
et ses collisions (contacts) sur les murs
"""
class Balle:
    """
    constructeur de balle avec le canevas et la couleur en paramètres
    """
    def __init__(self, canvas, couleur):
        self.canvas = canvas
        self.id = canvas.create_oval(10,10,25,25, fill = couleur)
        self.canvas.move(self.id, 245, 100)
        departs = [-12, -9, -6, -3, -2, -1, 1, 2, 3, 6, 9, 12]
        random.shuffle(departs)
        self.x = departs[0]
        self.y = -3
        self.hauteur_canevas = self.canvas.winfo_height()
        self.largeur_canevas = self.canvas.winfo_width()

    """
    gestionnaire de dessin de balle
    """
    def dessiner(self,decalage):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.hauteur_canevas:
            self.y = -3 -decalage
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.largeur_canevas:
            self.x = -3 -decalage
        time.sleep(0.01 * decalage)

"""
le programme principal
"""

# créer une fenêtre
tk = Tk()
tk.title("Tests pour jeu rebondir")
tk.resizable(0,0)
#tk.wm_attributes("-topmost",1)

# créer un canevas
canvas = Canvas(tk, width=500, height=400, bd = 0, highlightthickness=0)
canvas.pack()
tk.update()

# créer une ou plusieurs balle
balle1 = Balle(canvas, 'red')
balle2 = Balle(canvas, 'blue')
balle3 = Balle(canvas, 'green')
balle4 = Balle(canvas, 'yellow')
# la ou les faire bouger
while(1):
    balle1.dessiner(0)
    balle2.dessiner(1)
    balle3.dessiner(2)
    balle4.dessiner(4)
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)

