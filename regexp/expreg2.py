#!C:\Python34\python.exe
#-*- coding: utf-8 -*-

'''
Commençons par le début, recherchons des mots se terminant par a ou m
Cela peut se traduire par \w*[am]\W
'''

# import du module adéquat
import re

# initialisation de la chaine de test
sentences = ['Lacus a donec, la vitae gravida.',
             'Neque ipsum! rhoncus cras quam.'] 
# initialisation de la chaine de recherche
regexp = r"\w*[am]\W"

# test de correspondance
for s in sentences:
    print(re.findall(regexp, s))


