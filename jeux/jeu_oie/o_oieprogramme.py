#!/usr/bin/env python
# -*- coding: cp1252 -*-

#import des modules utilis�s
from tkinter import *
from o_oiedonnee import *

# Ce fichier d�finit l'interface graphique (tkinter)
# et la classe Joueur utiles au programme oie

#fonction qui r�pond au clic sur bouton et lance les d�s pour chaque joueur
def aller():
    ljoueurs[Joueur.numerojoueurencours].lancerdes()

#pr�paration et cr�ation fenetre principale du jeu
fenetre = Tk()
fenetre.title("Jeu de l'oie")
fenetre.geometry('1050x700+0+0')

#d�claration des variables de texte partag�es avec les contr�les tkinter
TexteDe = StringVar()
TexteJoueur = StringVar()
TexteResultat = StringVar()
TexteBouton = StringVar()
#cr�ation afficheur du label affich� au nord de fen�tre
labeljoueur = Label(fenetre , textvariable = TexteJoueur)
labeljoueur.config(font=('courier', 14, 'bold'))
labeljoueur.config(bg='black', fg='white')
labeljoueur.config(height=1, width=110)
labeljoueur.pack(side = TOP,padx = 2 , pady = 2 )
#cr�ation afficheur du label affich� au sud de fen�tre
labelresultat = Label(fenetre , textvariable = TexteResultat)
labelresultat.config(font=('courier', 14, 'italic'))
labelresultat.config(bg='black', fg='yellow')
labelresultat.config(height=3, width=110)
labelresultat.pack(side = BOTTOM, padx = 2 , pady = 2 )
#cr�ation bouton affich� � l'ouest de fen�tre lancer de d�s avec d�clenchement de la fonction aller sur click
boutonlancer = Button(fenetre, textvariable = TexteBouton, width=25, height = 4, command=aller)
boutonlancer.config(bg='navy', fg='white', bd=8)
boutonlancer.config(font=('courier', 12, 'bold'))
boutonlancer.pack(side= LEFT, padx = 10 , pady = 10)
TexteBouton.set("Lancer les d�s !")
#cr�ation afficheur du label affich� � l'ouest de fen�tre
labelde = Label(fenetre , textvariable = TexteDe)
labelde.config(font=('courier', 10, 'bold'))
labelde.config(bg='navy', fg='white')
labelde.config(height=4, width=15)
labelde.pack(side = LEFT, padx =10 , pady = 10 )
#cr�ation d'un widget Canvas qui va afficher l'image principale du jeu (zone graphique)
canevas = Canvas(fenetre,width = largeurCanevas, height =hauteurCanevas)
photo = PhotoImage(file="oie.gif")
itemphoto = canevas.create_image(0,0,anchor=NW, image=photo)
print ("Image de fond (itemphoto",itemphoto,")")
canevas.pack()

# cr�ation des listes de travail  (on utilisera les �l�ments 1 � 6, pas l'�l�ment 0)
lpions = [0,1,2,3,4,5,6]
limages = [0,1,2,3,4,5,6]
ljoueurs = [0,1,2,3,4,5,6]
#calcul d'un nombre al�atoire de 2 � 6 joueurs
nombreAleatoireJoueurs = random.randint(2,6)
#cr�ation des joueurs et placement initial des pions
for i in range(1,nombreAleatoireJoueurs+1):
    lpions[i] = PhotoImage(file="pion"+str(i)+".gif")
    limages[i]  = canevas.create_image(38-3*i,680+5*i,anchor=NW, image=lpions[i])
    print ("pion numero : "+str(i)+" ==> lien vers image : "+str(limages[i]))
    ljoueurs[i] = Joueur(i,1,3,canevas,limages[i],TexteDe,TexteJoueur,TexteResultat,TexteBouton,boutonlancer)
Joueur.nombreJoueurs = nombreAleatoireJoueurs
print ("NOMBRE DE JOUEURS : "+str(Joueur.nombreJoueurs))

#affichage de la fen�tre principale
fenetre.mainloop()
