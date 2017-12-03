# -*- coding: ISO-8859-1 -*-

# Ce fichier d�finit des fonctions utiles pour le pendu On utilise les donn�es du programme contenues dans donnees.py

import os
import pickle
from random import choice
from pendudonnees import *

# Gestion des scores
def recup_scores():
    """Cette fonction r�cup�re les scores enregistr�s si le fichier existe.
    Dans tous les cas, on retourne un dictionnaire, soit l'objet d�pickl�,
    soit un dictionnaire vide.
    On s'appuie sur nom_fichier_scores d�finit dans donnees.py.
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
    """Cette fonction se charge d'enregistrer les scores dans le fichier
    nom_fichier_scores . Elle re�oit en param�tre le dictionnaire des scores
    � enregistrer.
    """
    fichier_scores = open(nom_fichier_scores, "wb") # on �crase les anciens scores
    mon_pickler = pickle.Pickler(fichier_scores)
    mon_pickler.dump(scores)
    fichier_scores.close()
    
# Fonction g�rant les entr�es d'utilisateur
def recup_nom_utilisateur():
    # Fonction charg�e de r�cup�rer le nom de l'utilisateur.
    # Le nom de l'utilisateur doit �tre compos� de 4 caract�res minimum,chiffres et lettres exclusivement.
    # Si ce nom n'est pas valide, on appelle r�cursivement la fonction pour en obtenir un nouveau.

    nom_utilisateur = "brunode"
    nom_utilisateur = input("Entrez votre nom: ")
    # On met la premi�re lettre en majuscule et les autres en minuscule
    nom_utilisateur = nom_utilisateur.capitalize()
    if not nom_utilisateur.isalnum() or len(nom_utilisateur)<4:
        print("Ce nom est invalide.")
        # On appelle de nouveau la fonction pour avoir un autre nom
        return recup_nom_utilisateur()
    else:
        return nom_utilisateur

def recup_lettre():
    """Cette fonction est charg�e de r�cup�rer une lettre entr�e par
    l'utilisateur. Si la cha�ne r�cup�r�e n'est pas une lettre,
    on appelle r�cursivement la fonction jusqu'� obtenir une lettre.
    """
    lettre = input("Entrez une lettre: ")
    lettre = lettre.lower()
    if len(lettre)>1 or not lettre.isalpha():
        print("Vous n'avez pas entr� une lettre valide.")
        return recup_lettre()
    else:
        return lettre

# Fonctions du jeu de pendu
def choisir_mot():
    """Cette fonction retourne le mot choisi dans la liste des mots
    liste_mots .
    On utilise la fonction choice du module random (voir l'aide)
    """
    return choice(liste_mots)
    
def recup_mot_masque(mot_complet, lettres_trouvees):
    """Cette fonction retourne un mot masqu� tout ou en partie, en fonction :
    - du mot d'origine (type str)
    - des lettres d�j� trouv�es (type list)
    On retourne le mot d'origine avec des * rempla�ant les lettres que l'on
    n'a pas encore trouv�es.
    """
    mot_masque = ""
    for lettre in mot_complet:
        if lettre in lettres_trouvees:
            mot_masque += lettre
        else:
            mot_masque += "*"
    return mot_masque

