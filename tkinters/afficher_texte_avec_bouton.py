#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Ce fichier définit un premier essai de fenêtre sous TK
le programme va aller créer une première fenêtre Tkinter
'''

from tkinter import *

def bonjour():
    print("Bonjour te voici !!!")

def bonsoir():
    print("Au revoir et merci !!!")
    tk.destroy()
    
# création de la fenêtre, vous pouvez choisir le nom que vous voulez pour votre fenêtre
tk = Tk()
# création du label contenant le texte "Hello Word!" de couleur noire
etiquette = Label(tk, text='hello world!')
# insère le texte dans la fenêtre
etiquette.pack()
# création du bouton, associé à l'action .destroy*
boutonbonjour= Button(tk, text="saluer", command=bonjour)
# création du bouton, associé à l'action .destroy*
boutonquitter= Button(tk, text="quitter", command=bonsoir)
# insère les boutons dans la fenêtre
boutonbonjour.pack()
boutonquitter.pack()
# lance la boucle principale
tk.mainloop()
