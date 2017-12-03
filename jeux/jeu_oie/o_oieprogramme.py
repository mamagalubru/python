#!/usr/bin/env python
# -*- coding: cp1252 -*-

#import des modules utilisés
from tkinter import *
from o_oiedonnee import *

# Ce fichier définit l'interface graphique (tkinter)
# et la classe Joueur utiles au programme oie

#fonction qui répond au clic sur bouton et lance les dés pour chaque joueur
def aller():
    ljoueurs[Joueur.numerojoueurencours].lancerdes()

#préparation et création fenetre principale du jeu
fenetre = Tk()
fenetre.title("Jeu de l'oie")
fenetre.geometry('1050x700+0+0')

#déclaration des variables de texte partagées avec les contrôles tkinter
TexteDe = StringVar()
TexteJoueur = StringVar()
TexteResultat = StringVar()
TexteBouton = StringVar()
#création afficheur du label affiché au nord de fenêtre
labeljoueur = Label(fenetre , textvariable = TexteJoueur)
labeljoueur.config(font=('courier', 14, 'bold'))
labeljoueur.config(bg='black', fg='white')
labeljoueur.config(height=1, width=110)
labeljoueur.pack(side = TOP,padx = 2 , pady = 2 )
#création afficheur du label affiché au sud de fenêtre
labelresultat = Label(fenetre , textvariable = TexteResultat)
labelresultat.config(font=('courier', 14, 'italic'))
labelresultat.config(bg='black', fg='yellow')
labelresultat.config(height=3, width=110)
labelresultat.pack(side = BOTTOM, padx = 2 , pady = 2 )
#création bouton affiché à l'ouest de fenêtre lancer de dés avec déclenchement de la fonction aller sur click
boutonlancer = Button(fenetre, textvariable = TexteBouton, width=25, height = 4, command=aller)
boutonlancer.config(bg='navy', fg='white', bd=8)
boutonlancer.config(font=('courier', 12, 'bold'))
boutonlancer.pack(side= LEFT, padx = 10 , pady = 10)
TexteBouton.set("Lancer les dés !")
#création afficheur du label affiché à l'ouest de fenêtre
labelde = Label(fenetre , textvariable = TexteDe)
labelde.config(font=('courier', 10, 'bold'))
labelde.config(bg='navy', fg='white')
labelde.config(height=4, width=15)
labelde.pack(side = LEFT, padx =10 , pady = 10 )
#création d'un widget Canvas qui va afficher l'image principale du jeu (zone graphique)
canevas = Canvas(fenetre,width = largeurCanevas, height =hauteurCanevas)
photo = PhotoImage(file="oie.gif")
itemphoto = canevas.create_image(0,0,anchor=NW, image=photo)
print ("Image de fond (itemphoto",itemphoto,")")
canevas.pack()

# création des listes de travail  (on utilisera les éléments 1 à 6, pas l'élément 0)
lpions = [0,1,2,3,4,5,6]
limages = [0,1,2,3,4,5,6]
ljoueurs = [0,1,2,3,4,5,6]
#calcul d'un nombre aléatoire de 2 à 6 joueurs
nombreAleatoireJoueurs = random.randint(2,6)
#création des joueurs et placement initial des pions
for i in range(1,nombreAleatoireJoueurs+1):
    lpions[i] = PhotoImage(file="pion"+str(i)+".gif")
    limages[i]  = canevas.create_image(38-3*i,680+5*i,anchor=NW, image=lpions[i])
    print ("pion numero : "+str(i)+" ==> lien vers image : "+str(limages[i]))
    ljoueurs[i] = Joueur(i,1,3,canevas,limages[i],TexteDe,TexteJoueur,TexteResultat,TexteBouton,boutonlancer)
Joueur.nombreJoueurs = nombreAleatoireJoueurs
print ("NOMBRE DE JOUEURS : "+str(Joueur.nombreJoueurs))

#affichage de la fenêtre principale
fenetre.mainloop()
