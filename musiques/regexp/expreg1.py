#!C:\Python34\python.exe
#-*- coding: utf-8 -*-

''' il faut toujours commencer petit, construire brique par brique '''

# import du module adéquat
import re

# initialisation de la chaine de test
string = "TEfdsST Test TEdSTtest TEST" 
# initialisation de la chaine de recherche
regexp = "(TEST)"

# test de correspondance 
if re.match(regexp, string) is not None:
    # succès
    print ("Trouvé")
    # recherche avec affichage de l'élément trouvé
    print (re.search(regexp, string).groups())
else:
    # échec
    print ("Non Trouvé")
    

