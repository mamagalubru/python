#! /usr/bin/python
# -*- coding: utf-8 -*-

# importe la mathématique
from math import *
# importe la tortue
from turtle import *


def traceorigine():
    
    color("red")
    # revenir origine    
    goto(0, 0)
    
    # tracer axe des x
    x = -100
    y = 0
    while x < 100:
        goto(x, y)
        x = x + 1
        
    # revenir origine    
    goto(0, 0)
    
    # tracer axe des y
    y = -100
    x = 0
    while y < 100:
        goto(x, y)
        y = y + 1
        
    # revenir origine    
    goto(0, 0)
   

def tracefonction(origine,pas,fin):
    
    color("blue")
    x = origine
    while x < fin:
        y = sqrt(x)
        goto(x, y)
        x = x + pas


def tracefonctiongen(origine,pas,fin,couleur,fonction):
    
    color(couleur)
    x = origine
    while x < fin:
        # utilisation de la fonction eval => y = eval(cy)
        # avec préparation de la string par formatage => cy = '%s(x)' % fonction
        cy = '%s(x)' % fonction
        y = 5 * eval(cy)
        goto(x, y)
        x = x + pas

# fabrique des axes
reset()
traceorigine()
print ("OK pour ce schéma des axes")

# fabrique une courbe sqrt
tracefonction(0,1,10)
print ("OK pour ce schéma tracefonction sqrt")

# fabrique une courbe cos paramétrée
tracefonctiongen(10,5,100,'yellow','cos')
print ("OK pour ce schéma tracefonctiongen cos")

# fabrique une courbe exp paramétrée
# tracefonctiongen(100,1,5,'pink','exp')
# print ("OK pour ce schéma tracefonctiongen exp")

# fabrique une courbe sin paramétrée
tracefonctiongen(100,5,200,'green','sin')
print ("OK pour ce schéma tracefonctiongen sin")

# fabrique une courbe log paramétrée
tracefonctiongen(200,1,300,'black','log')
print ("OK pour ce schéma tracefonctiongen log")
