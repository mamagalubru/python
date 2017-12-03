# -*- coding: ISO-8859-1 -*-

# Ce fichier d�finit des fonctions utiles pour le pendu On utilise les donn�es du programme contenues dans donnees.py

import os
import pickle
from random import choice
from pendudonneestk import *

# Gestion des scores
def recup_scores():
   """
   Cette fonction r�cup�re les scores enregistr�s si le fichier existe
   Dans tous les cas, on retourne un dictionnaire, soit l'objet d�pickl�,
   soit un dictionnaire vide (nom_fichier_scores d�fini dans pendudonneestk.py)
   """
   if os.path.exists(nom_fichier_scores): # le fichier existe
      # On le r�cup�re
      fichier_scores = open(nom_fichier_scores, "rb")
      mon_depickler = pickle.Unpickler(fichier_scores)
      scores = mon_depickler.load ()
      fichier_scores.close()
   else: # le fichier n'existe pas
      scores = {}
   return scores

def enregistrer_scores(scores):
   """
   Cette fonction se charge d'enregistrer les scores dans le fichier
   nom_fichier_scores. Elle re�oit en param�tre le dictionnaire des scores
   � enregistrer.
   """
   fichier_scores = open(nom_fichier_scores, "wb") # on �crase les anciens scores
   mon_pickler = pickle.Pickler(fichier_scores)
   mon_pickler.dump(scores)
   fichier_scores.close()

# Fonctions du jeu de pendu
def choisir_mot():
   """
   Cette fonction retourne le mot masqu� dans la liste des mots
   liste_mots, on utilise la fonction choice du module random
   """
   mm = choice(liste_mots)
   print("Bonjour mot choisi !!! " + mm) # pour debug 
   return mm

# Fonctions g�rant les entr�es d'utilisateur
def verif_nom_utilisateur(joueur):
   """
   Fonction charg�e de v�rifier le nom de l'utilisateur,
   si ce nom n'est pas valide, on retourne le nom inconnu
   """
   joueur = joueur.capitalize() # On change la premi�re lettre en majuscule
   if not joueur.isalnum() or len(joueur)<4:
      joueur = "Linconnu"
   else:
      joueur = joueur
   # pour debug print("Bonjour " + joueur)
   return joueur

def verif_lettre(l,lts,mat):
   """
   Cette fonction est charg�e de v�rifier et tester une lettre entr�e par
   un utilisateur, si cette lettre n'est pas amphanum�rique on ne fait rien,
   si cette lettre est dans le mot � trouver pas de penalite, sinon penalite
   """
   l = l.lower()
   penalite = 0
   if len(l)==1 and l.isalpha():
      # validation de lettre saisie
      if l in lts: # la lettre a d�j� �t� entr�e
         # pour debug print("... vous avez d�j� trouv� cette lettre ...") # pour debug
         penalite = 2
      elif l in mat: # la lettre est dans le mot � trouver
         lts.append (l)
         # pour debug print('Bien jou� : ' + str(lts)) # pour debug
         penalite = 0
      else: # la lettre n'est pas dans le mot � trouver
         # pour debug print("... cette lettre ne se trouve pas dans le mot ...") # pour debug
         penalite = 1
   return penalite
   
def recup_mot_masque(mat, lts):
   """
   Cette fonction retourne un mot masqu� tout ou en partie, en fonction :
   du mot � trouver (type str) et des lettres d�j� trouv�es (type list)
   On retourne le mot masqu� avec des * rempla�ant les lettres que l'on
   n'a pas encore trouv�es.
   """
   mot_masque = ""
   for l in mat:
      if l in lts:
         mot_masque += l
      else:
         mot_masque += "*"
   print('mot masqu� : ' + mot_masque) # pour debug
   return mot_masque

