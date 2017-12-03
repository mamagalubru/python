#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Ce fichier définit une communication avec un arduino via le port série 
Le programme récupère toute écriture sur porte série
Puis l'écrit dans un fichier toutes les 10 secondes (ceci 10 fois)
'''

import time
import serial
from serial import Serial

# ouvrir le port série Com3 avec taux de transfert de 9600 bits par seconde
serial_port = Serial(port='Com3', baudrate=9600)
# ouvrir un fichier dans le répertoire courant (éventuellement avec création)
fichier = open('arduinoecriretout.txt', 'w')

i = 0
while (i < 10):
   ligne = serial_port.readline()
   print(ligne)
   fichier.write(str(ligne))
   time.sleep(10)
   i = i + 1
fichier.close()   
