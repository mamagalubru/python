#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
Ce fichier définit un essai de fenêtre sous TK 
Le programme va afficher quelques widgets dans une fenêtre Tkinter
Mais tout ceci structuré dans une grille
'''

# import du module graphique
from tkinter import *
# création la fenêtre 
fen1 = Tk()
# création de widgets 'Label' et rangement dans la grille
label1 = Label(fen1, text = 'Guitare :').grid(row =1, column =0, sticky =E)
label2 = Label(fen1, text = 'Marque  :').grid(row =0, column =0, sticky =E)
# création de widgets 'Entry' et rangement dans la grille
entr1 = Entry(fen1).grid(row =0, column =1)
entr2 = Entry(fen1).grid(row =1, column =1)
# création de widgets 'Checkbutton' et rangement dans la grille
chek1 = Checkbutton(fen1, text ='Guitare électrique ').grid(row =4, column =0, sticky =W)
chek2 = Checkbutton(fen1, text ='Guitare classique  ').grid(row =5, column =0, sticky =W)
chek3 = Checkbutton(fen1, text ='Guitare folklorique').grid(row =6, column =0, sticky =W)
# création d'un widget 'Canvas' avec une image gif et rangement dans la grille
can1 = Canvas(fen1, width =120, height =160, bg ='white')
photo =PhotoImage(file='C:\\Python34\\tests\\images\\guitare.gif')
can1.create_image(50,75, image =photo)
can1.grid(row =0, column =2, rowspan =4, padx =10, pady =5)
# démarrage de la boucle infinie de la fenêtre
fen1.mainloop()


# autres essais à réaliser
#chek1 = Checkbutton(fen1, text ='Guitare électrique').grid(row = 3, column = 1, columnspan =2)
#chek2 = Checkbutton(fen1, text ='Guitare classique ').grid(row = 4, column = 1, columnspan =2)
#chek3 = Checkbutton(fen1, text ='Guitare folk      ').grid(row = 5, column = 1, columnspan =2)
