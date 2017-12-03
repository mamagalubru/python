#!C:\Python34\python.exe
# -*- coding: utf-8 -*-
"""
teste quelques propriétés de lecture de fichier
"""
# lire tout un fichier du répertoire courant
fichier = open('liretout.txt')
texte = fichier.read()
print(texte)
fichier.close()
# lire ligne par ligne
fichier = open('liretout.txt','r')
for ligne in fichier:
    print("ligne par ligne : "+ligne)
fichier.close()
