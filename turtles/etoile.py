# -*- coding: ISO-8859-1 -*-

# importe la tortue
from turtle import *

# fabrique une �toile � 12 branches 
reset()
a = 0
aa = 0
while a <12:
    a = a + 1
    forward(150)
    left(150)

# fabrique une figure � n branches
n = 1
while n != 0:  
    reset()
    print ("entrer un nombre de pas entre 1 et 12")
    pas = input()
    nn = int(pas)
    print ("entrer une distance de d�placement entre 50 et 60")
    b = input()
    print ("entrer un angle de d�placement vers la gauche entre 50 et 75")
    c = input()
    pas = 0
    while pas < nn:
        pas = pas+1
        forward(int(b))
        left(int(c))
    print ("OK pour ce sch�ma, entrer 0 pour sortir ")
    n = input()
    if int(n)  == 0: break

