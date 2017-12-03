#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
    teste quelques propriétés de conditionnelles
"""

x1 = 1
while int(x1) > 0 :
    x1 = input("Entrez la coordonnée en abscisse du 1er vecteur : ")
    y1 = input("Entrez la coordonnée en ordonnée du 1er vecteur : ")
    x2 = input("Entrez la coordonnée en abscisse du 2ème vecteur : ")
    y2 = input("Entrez la coordonnée en ordonnée du 2ème vecteur : ")

    if int(x1) * int(x2) + int(y1) * int(y2) == 0:
        print("les 2 vecteurs sont orthogonaux")
    else:
        print("les 2 vecteurs ne sont pas orthogonaux")
print("à bientôt !!!")
    
        
