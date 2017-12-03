#! /usr/bin/python
# -*- coding: ISO-8859-1 -*-


"""
affiche quelques propriétés d'un type donné en paramètre
"""


def imprimeapi(element):
    """
    recherche toutes les méthodes d'un objet Python
    imprime les attributs de chacune de ces méthodes
    """
    methods = [el for el in dir(element) if not el.startswith('_')]
    for meth in methods:
        print(getattr(element, meth, 'nothing'))


# des méthodes de entiers
print()
print('liste des méthodes des objets entiers')
imprimeapi(int)

# des méthodes de listes
print()
print('liste des méthodes des objets listes')
imprimeapi([])

# des méthodes de tuples
print()
print('liste des méthodes des objets tuples')
imprimeapi(())

# des méthodes de dicos
print()
print('liste des méthodes des objets dicos')
imprimeapi({})




