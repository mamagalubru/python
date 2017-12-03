#!C:\Python34\python.exe
# -*- coding: utf-8 -*-


"""
lecture de fichier paramètre csv et rangement des couples clé-valeur
dans un dictionnaire comprenant des clés connues
boucles, luminosite, taille et timing
puis utilisation des valeurs lues grâce à la connaissance des clés
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
        # récupère clé et valeur
        #
        cle = row[0]
        valeur = row[1]
        #
        # peuple le dictionnaire
        #
        dico[cle]=valeur
    #
    # affiche la clé boucles du dictionnaire
    #
    valeur = dico['boucles']
    print("Le dico contient la clé 'boucles' avec la valeur {}.".format(valeur))
    #
    # affiche la clé luminosite du dictionnaire
    #
    valeur = dico['luminosite']
    print("Le dico contient la clé 'luminosite' avec la valeur {}.".format(valeur))
    #
    # affiche la clé taille du dictionnaire
    #
    valeur = dico['taille']
    print("Le dico contient la clé 'taille' avec la valeur {}.".format(valeur))
    #
    # affiche la clé timing du dictionnaire
    #
    valeur = dico['timing']
    print("Le dico contient la clé 'timing' avec la valeur {}.".format(valeur))
		
finally:
    file.close()
