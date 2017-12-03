#! /usr/bin/python
# -*- coding: ISO-8859-1 -*-


"""
teste quelques propri�t�s de chaines de caract�res
"""

def transformeacronyme(sentence='gnu not unix'):
    """
    force la majuscule de la premi�re lettre de chaque mot d'une phrase
    renvoie l'acronyme majusculis� s�par� par des points
    """
    letters = [word[0].upper() for word in sentence.split()]
    return '.'.join(letters)


# des initiales de d�but
print()
print('bruno enregistre g�n�ralement irrationnellement nativement')
print(transformeacronyme('bruno enregistre g�n�ralement irrationnellement nativement'))

# des initiales par d�faut
print('un acronyme par d�faut')
print(transformeacronyme())

# des initiales math�matiques
print()
print('un acronyme par passage de param�tres')
print(transformeacronyme('ce quil fallait d�montrer'))

# des initiales de fin
print()
print('fran�ois id�alise noe')
print(transformeacronyme('fran�ois id�alise noe'))



