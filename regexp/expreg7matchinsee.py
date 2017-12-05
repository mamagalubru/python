#!C:\Python34\python.exe
#-*- coding: utf-8 -*-

'''
Continuons avec re.match une recherche de numéro INSEE
r"(^([12])(?P<an>[0-9]{2})(?P<mn>0[1-9]|1[0-2])(?P<dp>[0-9]{2})[0-9]{3}[0-9]{3}$)"
'''

# import du module adéquat
import re

# initialisation de la chaine de recherche
regexp = r"(^([12])(?P<an>[0-9]{2})(?P<mn>0[1-9]|1[0-2])(?P<dp>[0-9]{2})[0-9]{3}[0-9]{3}$)"

while 1:
    # récupération de la chaine de saisie
    print("votre regexp %s " % regexp)
    insee = input("entrer votre numéro INSEE : ") 
    # test de correspondance
    mat = re.match(regexp, insee)
    if mat is not None:
        # succès
        print ("Numéro INSEE correct")
        # recherche avec affichage de l'élément trouvé
        print(f"{insee} ==> {mat}")
        print (re.search(regexp, insee).groups(1))
        # recherche avec affichage de tous les l'élément trouvé
        print(f"Année : {mat.group('an')} Mois : {mat.group('mn')} Dépt : {mat.group('dp')}")
        break
    else:
        # échec
        print ("Numéro INSEE incorrect")


