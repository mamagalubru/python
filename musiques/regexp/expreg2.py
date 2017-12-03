#!C:\Python34\python.exe
#-*- coding: utf-8 -*-

'''
Commençons par le début, recherchons XXXXXXXX@
Cela peut se traduire par ^[a-z0-9._-]+@
'''

# import du module adéquat
import re

# initialisation de la chaine de test
string = "brunomailbidon.com" 
# initialisation de la chaine de recherche
regexp = r"(^[a-z0-9._-]+@)"

# test de correspondance 
if re.match(regexp, string) is not None:
    # succès
    print ("Trouvé")
    # recherche avec affichage de l'élément trouvé
    print (re.search(regexp, string).groups())
else:
    # échec
    print ("Non Trouvé")


