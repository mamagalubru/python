#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
Ce fichier définit un essai de fenêtre sous TK 
Le programme va afficher une image dans une fenêtre Tkinter
'''

from tkinter import *

# créer une fenêtre
tk = Tk()

# créer un canevas
canvas = Canvas(tk, width=100, height=200)
canvas.pack()
print(''' je dessine une image sur le canevas ''')
mon_image = PhotoImage(file='C:\\Python34\\tests\\images\\guitare.gif')
canvas.create_image(0, 0, anchor = NW, image = mon_image)
print(''' je dessine un texte sur le canevas ''')
canvas.create_text(50, 160, text = 'image de musique')

tk.mainloop()
