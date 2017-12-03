#! /usr/bin/python
# -*- coding: ISO-8859-1 -*-

import os
import base64

"""
teste quelques propriétés pour forensic scientist : expert en criminalistique
ce programme crypte les programmes python
dans une arborescence de fichiers à partir du dossier courant
"""

rootDir = '.'

for chemin, repertoire, fichiers in os.walk(rootDir):
   for fnom in fichiers:
      if ".py" in str(fnom):
         lignes = open(fnom).readlines()
         for ligne in lignes:
            print (" Ligne lue : " + repr(ligne))
            chout = base64.b64encode(bytes(ligne, 'utf-8'))
            print (" Ligne cryptée : " + repr(chout))
            chinitiale = base64.b64decode(chout)
            print (" Ligne décryptée : " + repr(chinitiale))
