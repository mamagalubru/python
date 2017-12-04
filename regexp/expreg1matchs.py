#!C:\Python34\python.exe
#-*- coding: utf-8 -*-

''' 
il faut toujours commencer petit, construire brique par brique 
recherchons dans 2 chaines avec re.match 2 mots spécifiques
'''

# import du module adéquat
import re

# initialisation de la chaine de test
chaine1 = "zzzTESTTEfdsST Test TEdSTtest TEST" 
chaine2 = "TEfdsST (TEST) TEdSTtest TEST" 
# initialisation de la chaine de recherche
regexp1 = "TEST (.)*"
regexp2 = "(.)*TEST(.)*"

# test 1 de non correspondance 
mat = re.match(regexp1, chaine1)
print (f"{chaine1} ==> {mat}")
print (f"{regexp1} Trouvé dans {chaine1}")

# test 2 de correspondance 
mat = re.match(regexp2, chaine2)
print (f"{chaine2} ==> {mat}")
print (f"{regexp2} Trouvé dans {chaine2}")
