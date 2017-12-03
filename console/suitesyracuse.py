#! /usr/bin/python
# -*- coding: utf-8 -*-


"""
    teste quelques propriétés de boucle
"""

U0 = input("Entrez la première valeur de la suite : ")
n = input("Entrez le nombre d'itérations désiré : ")

u = int(U0)

for i in range(1,int(n)):
    if u%2 == 0:
        u=u/2
    else:
        u=3*u+1
    print("u%s = %i" % (i,u))
    
        
