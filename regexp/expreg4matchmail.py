#!C:\Python34\python.exe
#-*- coding: utf-8 -*-

'''
Continuons avec re.match une recherche d'adresse mail com ou fr
[(^[a-z0-9._-]+@[a-z0-9_-]+\.(com|fr){1}) 
'''

# import du module adéquat
import re

# initialisation de la chaine de recherche
regexp = r"(^[a-z0-9._-]+@[a-z0-9_-]+\.(com|fr){1})"

while 1:
    # récupération de la chaine de saisie
    print("votre regexp %s " % regexp)
    adresse = input("entrer une adresse mail de type bruno@mailbidon.com : ") 
    # test de correspondance 
    if re.match(regexp, adresse) is not None:
        # succès
        print ("Adresse mail correcte")
        # recherche avec affichage de l'élément trouvé
        print (re.search(regexp, adresse).groups(1))
        # recherche avec affichage de tous les l'élément trouvé
        print (re.findall(regexp, adresse))
        break
    else:
        # échec
        print ("Adresse mail incorrecte")


