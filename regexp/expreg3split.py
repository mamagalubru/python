#!C:\Python34\python.exe
#-*- coding: utf-8 -*-

'''
Commençons par le début, splitons avec re.split des mots quelconques d'une liste
Cela peut se traduire par \W+
'''

# import du module adéquat
import re

# initialisation de la chaine de test
sentences = ['Lacus a donec, la vitae gravida.',
             'Neque ipsum! rhoncus cras quam.'] 
# initialisation de la chaine de recherche
regexp = r"\W+"

# test de correspondance
[print(re.split(regexp, s)) for s in sentences]
