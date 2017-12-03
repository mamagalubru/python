#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
    teste quelques manipulations de dictionnaires
"""

sports_favoris = {"pattes d'araignée" : "football",
                  'orteil de crapaud' : 'natation',
                  'oreille de taureau' : 'ski',
                  'ongle de chauve-souris' : 'natation',
                  "omoplate d'anaconda" : 'handball',
                  'oeil de triton' : 'tir'}

# imprime le dico
print("*" * 10)
print(sports_favoris)

# imprime le dico de clé oeil de triton
print("*" * 10)
print(sports_favoris['oeil de triton'])

# modifie le dico de clé oreille de taureau et imprime le dico
sports_favoris['oreille de taureau'] = 'saut'
print("*" * 10)
print(sports_favoris)

# détruit le dico de clé orteil de crapaud et imprime le dico
del sports_favoris['orteil de crapaud']
print("*" * 10)
print(sports_favoris)

# imprime le dico en le formattant
print("*" * 10)
largeurcle = 0
largeursport = 0
for (cle, sport) in sports_favoris.items():
    if len(cle) > largeurcle:
        largeurcle = len(cle)
    if len(sport) > largeursport:
        largeursport = len(sport)
patron = "{{0: <{largeurcle}}} : {{1: <{largeursport}}}".format(**locals())
for (cle, sport) in sports_favoris.items():
    print(patron.format(cle, sport))

# imprime le dico sans l'ordonner
print("*" * 10)
for (cle, sport) in sports_favoris.items():
    print(cle, sport)

# imprime le dico en l'ordonnant par sport
print("*" * 10)
for (cle, sport) in sorted(sports_favoris.items(), key=lambda item: (item[1], item[0])):
    print(sport, cle)
