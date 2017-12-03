# -*- coding: cp1252 -*-
from tkinter import messagebox
from tkinter import *
import random
import time
from oiedonnee import *


#gérer le bouton jouer
def demarrerjeu():
    global nbjoueurs
    nbjoueurs = int(Nbjoueurs.get())
    print (nbjoueurs)
    fenetreintro.destroy()

#fonction de lancer de 2 dés aleatoire + cases speciales
def lancerdes():
    global numcase,numjoueur,compteur

    de1 = random.randint(1,6)
    de2 = random.randint(1,6)
    des = de1 + de2
    pos = numcase[numjoueur]
    TexteDe.set('Joueur  => ' + str(numjoueur) + '\nPos AV = > ' + str(pos) + '\nDé1+Dé2 => ' + str(des) + '\nPos AP  => ' + str(des+pos))
    TexteResultat.set("")

    # on regarde si bloqué dans le puits auparavant pour vérifier la libération
    if numcase[numjoueur] == 31 :
        if de1 == 6 or de2 == 6 :
            TexteResultat.set("Vous avez fait un 6 ! \n Vous pouvez sortir du puits !")
        else :
            TexteResultat.set("Vous n'avez pas fait un 6 ! \n Vous nagez toujours au fond du puits !")
            changerjoueur()
            return

    # on regarde si bloqué en prison auparavant pour vérifier la libération
    if numcase[numjoueur] == 52 :
        compteur[numjoueur] = compteur[numjoueur] - 1
        if compteur[numjoueur] < 1 :
            TexteResultat.set("Vous êtes liberé de prison!")
        else :
            TexteResultat.set("Vous restez encore bloqué en prison !")
            changerjoueur()
            return

    # on effectue le deplacement lié au tirage des dés :de1,de2
    numcase[numjoueur]=numcase[numjoueur] + de1 + de2
    print("Joueur " + str(numjoueur) + " Dés " + str(de1+de2) + " Case " + str(numcase[numjoueur]))

    # case trop haut
    if numcase[numjoueur] > 63 :
        TexteResultat.set('Dommage, vous avez dépassé la cible')
        trop = numcase[numjoueur] - 63
        numcase[numjoueur] = 63 - trop

    # cases bonus
    if numcase[numjoueur]  == 6 :
        TexteResultat.set("Pont : Vous avez pris le pont ! \n Vous passez à la case 12 !")
        numcase[numjoueur] = 12
    elif numcase[numjoueur] == 9 or numcase[numjoueur] ==18 or numcase[numjoueur] ==27 or numcase[numjoueur] ==36 or numcase[numjoueur] ==45 or numcase[numjoueur] ==54 :
         TexteResultat.set("Case Oie : Vous êtes sur une case ''oie''! \n Vous doublez votre lancer de dés !")
         numcase[numjoueur]=numcase[numjoueur] + de1 + de2

    # cases malus
    if numcase[numjoueur] == 31 :
        TexteResultat.set("Vous êtes au puits \n Vous devrez faire un 6 avec un des deux dés pour sortir !")
        numcase[numjoueur] = 31
    elif numcase[numjoueur] == 42 :
        TexteResultat.set("Vous vous êtes perdu dans le labyrinthe ! \n Vous passez à la case 30 !")
        numcase[numjoueur] = 30
    elif numcase[numjoueur] == 52 :
        compteur[numjoueur] = 3
        TexteResultat.set("Vous êtes bloqué pour quelques tours en prison !")
        numcase[numjoueur] = 52
    elif numcase[numjoueur] == 58 :
        TexteResultat.set("Mort : Vous êtes DEAD ! \n Vous retournez au départ !")
        numcase[numjoueur] = 1

    # case gagné
    if numcase[numjoueur] == 63 :
        TexteResultat.set('Bravo, vous avez gagné joueur ' + str(numjoueur))
        Canevas.coords(pionjoueur[numjoueur],415,325)
        Canevas.update()
        print('Bravo, vous avez gagné joueur ' + str(numjoueur))
        time.sleep(10)
        boutonlancer.destroy()
        return

    # déplacer le pion dans tous les cas
    deplacerpion()

    # inventer une phrase
    inventerphrase()

    # passer au joueur suivant
    changerjoueur()
    return

def deplacerpion():
    global numcase,numjoueur,pionjoueur
    # déplacer le pion si possible
    x = casex[numcase[numjoueur]]- 3*numjoueur
    y = casey[numcase[numjoueur]]- 3*numjoueur
    if x < largeurCanevas and y < hauteurCanevas:
        Canevas.coords(pionjoueur[numjoueur],x,y)
        Canevas.update()

def inventerphrase():
    # inventer une petite phrase si rien d'autre n'est affiché
    if len(TexteResultat.get()) == 0:
        phrase = liste_phrases[random.randint(1,20)]
        TexteResultat.set(str(phrase))

def changerjoueur():
    global numjoueur
    # passer au joueur suivant
    if numjoueur<nbjoueurs:
        numjoueur=numjoueur+1
        TexteJoueur.set('Au joueur ' + str(numjoueur) + ' de lancer les dés !')
    else:
        numjoueur=1
        TexteJoueur.set('Au joueur ' + str(numjoueur) + ' de lancer les dés !')



#creation fenetre intro
fenetreintro = Tk()
fenetreintro.title("Jeu de l'oie")
fenetreintro.geometry('380x140+500+400')
choixnb = StringVar()
choixnb.set('Choisissez le nombre de joueurs pour commencer')
choixnbjoueur = Label(fenetreintro , textvariable = choixnb , fg = 'red' , bg = 'white')
choixnbjoueur.pack(side= TOP , padx = 10 , pady = 10)
boutonjouer = Button(fenetreintro, text ='Jouer', command= demarrerjeu)
boutonjouer.pack(side= LEFT , padx = 10 , pady = 10)
Nbjoueurs = StringVar()
Nbjoueurs.set(nbjoueurs)
boutonnbjoueurs = Scale(fenetreintro, from_=1, to=6 , variable = Nbjoueurs , orient=HORIZONTAL )
boutonnbjoueurs.pack(side= LEFT ,padx = 100 , pady = 10)
print ("Nombre de joueurs : " + str(Nbjoueurs.get()))
fenetreintro.mainloop()


#creation fenetre principale du jeu
fenetre = Tk()
fenetre.title("Jeu de l'oie")
fenetre.geometry('1280x900+0+0')
#creation bouton lancé de dés
boutonlancer = Button(fenetre, text ='Lancer les dés' , command= lancerdes)
boutonlancer.pack(side= LEFT , padx = 10 , pady = 10)
#creation afficheur des labels d'affichage
TexteDe = StringVar()
TexteJoueur = StringVar()
TexteResultat = StringVar()
labelde = Label(fenetre , textvariable = TexteDe , fg = 'blue' , bg = 'white')
labelde.config(font=('courier', 16, 'bold'))
labelde.config(bg='blue', fg='yellow')
labelde.config(height=4, width=15)
labelde.pack(side = RIGHT , padx =2 , pady = 2 )
labeljoueur = Label(fenetre , textvariable = TexteJoueur ,fg = 'black' , bg = 'white')
labeljoueur.config(font=('courier', 16, 'bold'))
labeljoueur.config(bg='black', fg='yellow')
labeljoueur.config(height=1, width=80)
labeljoueur.pack(side = TOP,padx = 2 , pady = 2 )
labelresultat = Label(fenetre , textvariable = TexteResultat ,fg = 'red' , bg = 'white')
labelresultat.config(font=('courier', 16, 'italic'))
labelresultat.config(bg='red', fg='yellow')
labelresultat.config(height=3, width=80)
labelresultat.pack(side = BOTTOM,padx = 2 , pady = 2 )
# Création d'un widget Canvas (zone graphique)
Canevas = Canvas(fenetre,width = largeurCanevas, height =hauteurCanevas)
photo = PhotoImage(file="oie.gif")
itemphoto = Canevas.create_image(0,0,anchor=NW, image=photo)
print ("Image de fond (itemphoto",itemphoto,")")
Canevas.pack()
# placement pions
##1
if nbjoueurs > 0:
    pion1 = PhotoImage(file="pion 1.gif")
    item1 = Canevas.create_image(35,715,anchor=NW, image=pion1)
    print ("pion1 (item1",item1,")")
##2
if nbjoueurs > 1:
    pion2 = PhotoImage(file="pion 2.gif")
    item2 = Canevas.create_image(32,720,anchor=NW, image=pion2)
    print ("pion2 (item2",item2,")")
##3
if nbjoueurs > 2:
    pion3 = PhotoImage(file="pion 3.gif")
    item3 = Canevas.create_image(42,720,anchor=NW, image=pion3)
    print ("pion3 (item3",item3,")")
##4
if nbjoueurs > 3:
    pion4 = PhotoImage(file="pion 4.gif")
    item4 = Canevas.create_image(40,725,anchor=NW, image=pion4)
    print ("pion4 (item4",item4,")")
##5
if nbjoueurs > 4:
    pion5 = PhotoImage(file="pion 5.gif")
    item5 = Canevas.create_image(50,720,anchor=NW, image=pion5)
    print ("pion5 (item5",item5,")")
##6
if nbjoueurs > 5:
    pion6 = PhotoImage(file="pion 6.gif")
    item6 = Canevas.create_image(25,730,anchor=NW, image=pion6)
    print ("pion6 (item6",item6,")")
#afficher fenetre
fenetre.mainloop()



