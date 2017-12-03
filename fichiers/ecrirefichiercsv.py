#!C:\Python34\python.exe
# -*- coding: utf-8 -*-
"""
teste quelques propriétés d'écriture de fichier csv
"""
import csv
# création de la liste à écrire
connaissances = [["ID","First Name","Credit","Density"],
      ["1032","John","2290","1"],
      ["1044","Paul","1240","1.5"],
      ["1050","Georges","5490","1"]]
# ouvrir ou créer un fichier csv du répertoire courant
nomfic = "connaissances.csv"
fichier = open(nomfic, "wt")
try:
    # créer un objet writer csv davec délimiteurs ; et "
    wtr = csv.writer(fichier, delimiter=',', quotechar='"')
    for ligne in connaissances:
        # écrit chaque ligne dans le fichier csv
        wtr.writerow(ligne)
        # affiche la ligne entière écrite
        print("Ligne entière : ",ligne)
finally:
    fichier.close()
