#! /usr/bin/python
# -*- coding: ISO-8859-1 -*-

import os

"""
teste quelques propriétés pour forensic scientist : expert en criminalistique
ce programme recherche certaines instructions python
dans une arborescence de fichiers à partir du dossier courant
"""

jeu_instruction = ['for','while','if','in','else']
jeu_fonction = ['str','open','print','close','input']

rootDir = '.'

for chemin, repertoire, fichiers in os.walk(rootDir):
   for fnom in fichiers:
      if ".py" in str(fnom):
         trouvemotcle = 0
         trouvefonction = 0
         lignes = open(fnom).readlines()
         for ligne in lignes:
            mots = ligne.split()
            for mot in mots:
               if mot in jeu_instruction:
                  trouvemotcle = trouvemotcle + 1
               if mot in jeu_fonction:
                  trouvefonction = trouvefonction + 1
         if trouvemotcle > 0:
            print (fnom + " contient sans doute %s instructions PYTHON. " % trouvemotcle)
         else:
            print (fnom + " ne contient sans doute pas d'instructions PYTHON. ")
         if trouvefonction > 0:
            print (fnom + " contient sans doute %s fonctions PYTHON. " % trouvefonction)
         else:
            print (fnom + " ne contient sans doute pas de fonctions PYTHON. ")
