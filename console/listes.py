#! /usr/bin/python
# -*- coding: utf-8 -*-


"""
    teste quelques propriétés de listes
"""

liste_sorcier = "pattes d'araignée, orteil de crapaud, oeil de triton"
print("*" * 10)
print(liste_sorcier)
liste_sorcier = ["pattes d'araignée", 'orteil de crapaud', 'oeil de triton',
                 'aile de chauve-souris', 'beurre de limace', 'écailles de serpent']
print("*" * 10)
print(liste_sorcier)
print(liste_sorcier[0])
print(liste_sorcier[2])
print(liste_sorcier[5])

liste_sorcier[2] = "langue d'escargot"
print("*" * 10)
print(liste_sorcier)

liste_sorcier.append('coeur de mandragore')
liste_sorcier.append('extrait de cigüe')
liste_sorcier.append('gaz des marais')
liste_sorcier.append("langue d'iguane")
print("*" * 10)
print(liste_sorcier)
print(liste_sorcier[7:9])

del liste_sorcier[8]
print("*" * 10)
print(liste_sorcier[7:9])

l1 = liste_sorcier[0:4]
print("*" * 10)
print(l1)
l2 = liste_sorcier[4:9]
print("*" * 10)
print(l2)

l3 = l1 + l2
print("*" * 10)
print(liste_sorcier)
print("*" * 10)
print(l3)
