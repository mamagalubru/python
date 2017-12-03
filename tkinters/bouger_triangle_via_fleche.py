#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Ce fichier définit un essai de fenêtre sous TK 
Le programme va créer un triangle dans une fenêtre Tkinter
Puis va permettre à l'utilisateur de déplacer ce triangle
'''

from tkinter import *

def bouger_triangle(evenement):
    if evenement.keysym == 'Right':
        canvas.move(1,3,0)
    elif evenement.keysym == 'Left':
        canvas.move(1,-3,0)
    elif evenement.keysym == 'Up':
        canvas.move(1,0,-3)
    elif evenement.keysym == 'Down':
        canvas.move(1,0,3)
    else:
        canvas.move(0,0,0)
    
# création de l'objet fenêtre
tk = Tk()
# personnalisation éventuelle
# tk.title = 'Coucou'
# tk.iconbitmap("questhead")

# création de l'objet canevas dans la fenêtre
canvas = Canvas(tk, width = 400, height = 400)
canvas.pack()

# création du triangle dans l'objet canevas
canvas.create_polygon(10, 10, 10, 60, 50, 35)
print(''' j'ai créé un triangle ''')
# création des liens antre les touches de fonctions (flèches) et la fonction de mouvement
canvas.bind_all('<KeyPress-Right>',bouger_triangle)
canvas.bind_all('<KeyPress-Left>',bouger_triangle)
canvas.bind_all('<KeyPress-Up>',bouger_triangle)
canvas.bind_all('<KeyPress-Down>',bouger_triangle)
print(''' je peux maintenant bouger le triangle au Nord via Up''')
print(''' je peux maintenant bouger le triangle au Sud via Down''')
print(''' je peux maintenant bouger le triangle à l'Ouest via Right''')
print(''' je peux maintenant bouger le triangle à l'Est via Left''')

# boucle infinie
tk.mainloop()
