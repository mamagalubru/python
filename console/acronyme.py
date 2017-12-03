#! /usr/bin/python
# -*- coding: ISO-8859-1 -*-


"""
teste quelques propriétés de chaines de caractères
"""

def transformeacronyme(sentence='gnu not unix'):
    """
    force la majuscule de la première lettre de chaque mot d'une phrase
    renvoie l'acronyme majusculisé séparé par des points
    """
    letters = [word[0].upper() for word in sentence.split()]
    return '.'.join(letters)


# des initiales de début
print()
print('bruno enregistre généralement irrationnellement nativement')
print(transformeacronyme('bruno enregistre généralement irrationnellement nativement'))

# des initiales par défaut
print('un acronyme par défaut')
print(transformeacronyme())

# des initiales mathématiques
print()
print('un acronyme par passage de paramètres')
print(transformeacronyme('ce quil fallait démontrer'))

# des initiales de fin
print()
print('françois idéalise noe')
print(transformeacronyme('françois idéalise noe'))



