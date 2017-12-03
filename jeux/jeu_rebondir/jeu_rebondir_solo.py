#! /usr/bin/python
# -*- coding: utf-8 -*-

# cette version me sert aussi à tester git et github
# chaque modification sur un poste doit être validée via git sur ce poste (commit)
# chaque modification sur un poste doit être poussée via git sur github (push) par exemple sur https://github.com/mamagalubru/essai
# chaque modification peut ensuite être récupérée via git sur un autre poste (pull)

"""
le jeu de rebonds de balle sur une raquette poussé le 21 mars 2017 à 22h
"""

import time
import random
from tkinter import *
import winsound

"""
la classe balle gère ses mouvements
et ses collisions (contacts) sur les murs ou sur la raquette
"""
class Balle:
    """
    constructeur de balle avec le canevas la raquette et la couleur en paramètres
    """
    def __init__(self, canvas, raquette1, couleur):
        self.canvas = canvas
        self.raquette1 = raquette1
        # créer le cercle de la balle
        self.id = canvas.create_oval(10,10,25,25, fill = couleur)
        # positionner la balle dans le canvas
        self.canvas.move(self.id, 245, 100)
        # préparer aléatoirement les futurs déplacements en x
        departs = [-3, -2, -1, 1, 2, 3]
        random.shuffle(departs)
        self.x = departs[0]
        # programmer le futur déplacement en y
        self.y = -3
        # gérer les bornes (hauteur, largeur, bas)
        self.hauteur_canevas = self.canvas.winfo_height()
        self.largeur_canevas = self.canvas.winfo_width()
        self.touche_bas = False

    """
    gestionnaire de collision balle et raquette
    """
    def heurter_raquette(self, raquette, pos):
        global coups
        # récupération des 4 coordonnées de la raquette (haut-gauche, bas-droit)
        pos_raquette = self.canvas.coords(raquette.id)
        # comparaison avec les 4 coordonnées de la balle
        if pos[2] >= pos_raquette[0] and pos[0] <= pos_raquette[2]:
            if pos[3] >= pos_raquette[1] and pos[3] <= pos_raquette[3]:
                # si oui il y a collision
                coups = coups + 1
                return True
            return False


    """
    gestionnaire de dessin de balle
    """
    def dessiner(self):
        # redessiner la balle en fonction de ses déplacements programmés (en x et y)
        self.canvas.move(self.id, self.x, self.y)
        # recalculer ses nouvelles coordonnées
        pos = self.canvas.coords(self.id)
        # tout en haut il faut redescendre
        if pos[1] <= 0:
            self.y = 3
            # jouer une musique de mur au plafond sous windows
            winsound.PlaySound('C:\\Python34\\tests\\sons\\pong_plafond.wav',winsound.SND_FILENAME|winsound.SND_ASYNC)
        # tout en bas le jeu est fini on a perdu
        if pos[3] >= self.hauteur_canevas:
            self.touche_bas = True
            # jouer une musique de fin de jeu sous windows
            winsound.PlaySound('C:\\Python34\\tests\\sons\\pong_perdu.wav',winsound.SND_FILENAME|winsound.SND_ASYNC)
        # teste le contact avec la raquette 1 (si oui remonte)
        if self.heurter_raquette(self.raquette1,pos) == True:
            self.y = -3
            # jouer une musique de raquette sous windows
            winsound.PlaySound('C:\\Python34\\tests\\sons\\pong_raquette.wav',winsound.SND_FILENAME|winsound.SND_ASYNC)
        # tout à gauche il faut retourner vers la droite
        if pos[0] <= 0:
            self.x = 3
            # jouer une musique de mur gauche sous windows
            winsound.PlaySound('C:\\Python34\\tests\\sons\\pong_mur_gauche.wav',winsound.SND_FILENAME|winsound.SND_ASYNC)
        # tout à droite il faut retourner vers la gauche
        if pos[2] >= self.largeur_canevas:
            self.x = -3
            # jouer une musique de mur droit sous windows
            winsound.PlaySound('C:\\Python34\\tests\\sons\\pong_mur_droit.wav',winsound.SND_FILENAME|winsound.SND_ASYNC)

"""
la classe raquette gère ses mouvements et ses collisions avec la balle
"""
class Raquette:
    """
    constructeur de raquette avec canevas et couleur en paramètre
    """
    def __init__(self, canvas, couleur):
        self.canvas = canvas
        # créer le rectangle de la raquette
        self.id = canvas.create_rectangle(0,0,100,10, fill = couleur)
        # commencer par un déplacement horizontal nul
        self.x = 0
        # récupérer une largeur
        self.largeur_canevas = self.canvas.winfo_width()
        # positionner la raquette dans le canvas et lier les touches de contrôles
        self.canvas.move(self.id, 200, 300)
        self.canvas.bind_all('<KeyPress-Left>',self.vers_gauche)
        self.canvas.bind_all('<KeyPress-Right>',self.vers_droite)
        self.canvas.bind_all('<KeyPress-Up>',self.stationnaire)
        self.canvas.bind_all('<KeyPress-Down>',self.stationnaire)

    def vers_gauche(self,evt):
        self.x = -2

    def vers_droite(self,evt):
        self.x = 2

    def stationnaire(self,evt):
        self.x = 0

    """
    fonction de déplacement de raquette
    """
    def dessiner(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.largeur_canevas:
            self.x = 0

"""
le programme principal
"""

# créer une fenêtre
tk = Tk()
tk.title("Jeu Rebondir")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)

# créer un canevas
canvas = Canvas(tk, width=500, height=400, bd = 0, highlightthickness=0)
canvas.pack()
tk.update()

# créer une (ou plusieurs) raquette
raquette1 = Raquette(canvas, 'blue')

# créer une (ou plusieurs) balle
balle = Balle(canvas, raquette1, 'red')

# choisir un niveau de jeu
passage = 0
niveau = 1

# compter les coups de raquettes
coups = 0

# faire bouger balle(s) et raquette(s)
while(1):
    if balle.touche_bas == False:
        if niveau > 1 or (niveau == 1 and passage % 2 == 0):
            balle.dessiner()
        raquette1.dessiner()
        tk.update_idletasks()
        tk.update()
        time.sleep(0.01)
        passage = passage + 1
    else:
        messageFin = 'Partie terminée après ' + str(coups) + ' échanges !!!'
        canvas.create_text(200,100, text=messageFin, font=('Helvetica',14))
        canvas.pack()
        tk.update()
        time.sleep(2)
        break

# fermer la fenêtre en sortant
tk.destroy()
