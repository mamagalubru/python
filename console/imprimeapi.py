#! /usr/bin/python
# -*- coding: ISO-8859-1 -*-


"""
affiche quelques propri�t�s d'un type donn� en param�tre
"""


def imprimeapi(element):
    """
    recherche toutes les m�thodes d'un objet Python
    imprime les attributs de chacune de ces m�thodes
    """
    methods = [el for el in dir(element) if not el.startswith('_')]
    for meth in methods:
        print(getattr(element, meth, 'nothing'))


# des m�thodes de entiers
print()
print('liste des m�thodes des objets entiers')
imprimeapi(int)

# des m�thodes de listes
print()
print('liste des m�thodes des objets listes')
imprimeapi([])

# des m�thodes de tuples
print()
print('liste des m�thodes des objets tuples')
imprimeapi(())

# des m�thodes de dicos
print()
print('liste des m�thodes des objets dicos')
imprimeapi({})




