#!C:\Python34\python.exe
#-*- coding: utf-8 -*-

'''
Continuons avec [a-z0-9._-]+\.[(com|fr)]+ 
'''

# import du module adéquat
import re

# récupération de la chaine de saisie
adresse = input("entrer une adresse mail de type bruno@mailbidon.com : ") 
# initialisation de la chaine de recherche
regexp = r"(^[a-z0-9._-]+@[a-z0-9._-]+\.[(com|fr)]+)"

# test de correspondance 
if re.match(regexp, adresse) is not None:
    # succès
    print ("Trouvé")
    # recherche avec affichage de l'élément trouvé
    print (re.search(regexp, adresse).groups())
else:
    # échec
    print ("Non Trouvé")


