# -*- coding: ISO-8859-1 -*-

# importe la mathématique
from math import *
# importe la tortue
from turtle import *


def tracetortue(nombre,fonction):
    
    # utilisation de la fonction eval => y = eval(cy)
    # avec préparation de la string par formatage => cy = '%s(x)' % fonction
    cy = 't.%s' % fonction + '(%s)' % nombre
    #print(cy)
    eval(cy)

def carresanscoins():
    
    # utilisation de l'objet tortue
    t.up()
    tracetortue(10,'forward')
    t.down()
    tracetortue(80,'forward')
    t.up()
    tracetortue(10,'forward')
    t.down()
    tracetortue(90,'left')
    
# fabrique un carré
t = Pen()
t.color('red', 'green')
tracetortue(100,'forward')
tracetortue(90,'left')
tracetortue(100,'forward')
tracetortue(90,'left')
tracetortue(100,'forward')
tracetortue(90,'left')
tracetortue(100,'forward')
print ("OK pour ce schéma tracetortue carré")

# fabrique un rectangle
# t.reset()
t.color('blue', 'yellow')
tracetortue(200,'forward')
tracetortue(90,'left')
tracetortue(100,'forward')
tracetortue(90,'left')
tracetortue(200,'forward')
tracetortue(90,'left')
tracetortue(100,'forward')
print ("OK pour ce schéma tracetortue rectangle")

# fabrique un triangle
# t.reset()
t.color('black', 'brown')
tracetortue(40,'forward')
tracetortue(90,'left')
tracetortue(30,'forward')
tracetortue(125,'left')
tracetortue(50,'forward')
print ("OK pour ce schéma tracetortue triangle")

# fabrique un carré sans coins
#t.reset()
t.color('green', 'orange')
for i in range (1,5):
    carresanscoins()
print ("OK pour ce schéma tracetortue carré sans coins")
