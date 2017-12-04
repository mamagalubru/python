#!C:\Python34\python.exe
#-*- coding: utf-8 -*-

'''
Commençons par le début, recherchons des mots et rangeons 
le résultat dans des cases (groupes nommés)
Cela peut se traduire par r"(?P<nom>\w+) (?P<alias>\w+)"
'''

# import du module adéquat
import re

# initialisation de la chaine de test
sentences = ['alex aidant',
             'lamine dor',
             'vera dent']
# initialisation de la chaine de recherche
#regexp = r"\w+ (?P<alias>\w+) \w+ \w+\W"
regexp = r"(?P<nom>\w+) (?P<alias>\w+)"

# test de correspondance
for s in sentences:
    mat = re.match(regexp, s)
    print(f"{s} ==> {mat}")
    print(f"NOM : {mat.group('nom')} ALIAS : {mat.group('alias')}")
