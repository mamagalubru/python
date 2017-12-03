#!C:\Python34\python.exe
# -*- coding: utf-8 -*-


"""
lecture de fichier paramètre csv et rangement des couples clef-valeur dans un dictionnaire
"""


import csv

# lire tout un fichier paramètre csv du répertoire courant
fname = "param.csv"
file = open(fname, "r")
dico = {}
try:
    reader = csv.reader(file)
    for row in reader:
        #
        # affiche la ligne entière lue
        #
        print("Ligne entière : ",row)
        #
        # récupère clé et valeur
        #
        cle = row[0]
        valeur = row[1]
        #
        # peuple le dictionnaire
        #
        dico[cle]=valeur
    #
    # affiche le dictionnaire
    #
    for cle, valeur in dico.items():
        print("La clé {} contient la valeur {}.".format(cle, valeur))
    #
    # affiche les clés du dictionnaire
    #
    for cle in dico.keys():
        print("Le dico contient la clé {}.".format(cle))
    #
    # affiche les valeurs du dictionnaire
    #
    for valeur in dico.values():
        print("Le dico contient la valeur {}.".format(valeur))
		
finally:
    file.close()
