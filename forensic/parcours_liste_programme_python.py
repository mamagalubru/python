#! /usr/bin/python
# -*- coding: ISO-8859-1 -*-
import os
"""
teste quelques propriétés pour forensic scientist
expert en criminalistique, ce programme affiche chemins,
répertoires et fichiers à partir du dossier courant
"""
rootDir = '.'
for chemin, repertoire, fichiers in os.walk(rootDir):
   for fnom in fichiers:
      if ".py" in str(fnom):
         lignes = open(fnom).readlines()
         for ligne in lignes:
            print (" Ligne lue : " + repr(ligne))
