#!C:\Python34\python.exe
#-*- coding: utf-8 -*-

'''Controle sur des objets tkinter '''

# import des modules adéquats
import re
from tkinter import *

# lecture du contenu du widget "reponse"
def repondre():
    # test de correspondance 
    if re.match(regexp, reponse.get()) is not None:
        # succès
        affichage['text'] = reponse.get() + ' valide '
    else:
        # échec
        affichage['text'] = reponse.get() + ' invalide '

# initialisation de la chaine de recherche
regexp = r"(^[A-Z][a-z -]+$)"

# construction du formulaire
fenetre = Tk()
fenetre.title('Controle de saisie')
nom = Label(fenetre, text = 'Votre nom :')
reponse = Entry(fenetre, width=40)
valeur = Button(fenetre, text =' Valider', command=repondre)
affichage = Label(fenetre, width=50)
nom.pack()
reponse.pack()
valeur.pack()
affichage.pack()
fenetre.mainloop()

