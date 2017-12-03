#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Ce fichier définit un essai de fenêtre sous TK 
Le programme va créer une photo dans une fenêtre Tkinter
Puis va remuer par une boucle image et texte
'''

import time
from tkinter import *

# créer une fenêtre
tk = Tk()

# créer un canevas
canvas = Canvas(tk, width=500, height=500)
canvas.pack()

# charger une image et l'afficher avec un texte
mon_image = PhotoImage(file='C:\\Python34\\tests\\images\\guitare.gif')
cv1 = canvas.create_image(0, 0, anchor = NW, image = mon_image)
cv2 = canvas.create_text(200, 300, text = 'images de musique')

# remuer image et texte
for i in range(0,10):
    for j in range(0,40):
        canvas.move(cv1,5,5)
        canvas.move(cv2,5,-5)
        tk.update()
        time.sleep(0.10)
    for j in range(0,40):
        canvas.move(cv1,-5,-5)
        canvas.move(cv2,-5,5)
        tk.update()
        time.sleep(0.10)
