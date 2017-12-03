#!C:\Python34\python.exe
# -*- coding: utf-8 -*-

"""
Programme de gestion de tables de la BD
3 tables dont les descriptions sont déclarées en globales
plusieurs actions
"""

import sys
import pymysql as mdb
import re as expreg


class Glob:
   """
   Espace de noms pour les variables et fonctions <pseudo-globales>
   Les variables de connexions
   Les caractéristiques de tables
   """

   # Connexion à la base de données.  Variables :
   # nom de la base de données
   # propriétaire ou utilisateur
   # mot de passe d'accès
   # nom ou adresse IP du serveur ou autre host = "192.168.0.235"
   dbName = "projets"
   user = "mamagalubru"
   passwd = "rialto2013"
   host = "localhost"

   # Structure de la base de données.Dictionnaire des tables & champs :
   dicoT = {"personnes":[('id', "k", "clé primaire"), ('nom', 30, "nom"),
                         ('prenom', 30, "prénom"), ('tauxHoraire', "i", "Taux horaire")],
            "taches":[('id', "k", "clé primaire"), ('code', 5, "code de la tache"),
                      ('description', 80, "description de la tache"), ('duree', "i", "durée (en minutes)")],
            "rendezvous":[('id', "k", "clé primaire"), ('idPersonne', "i", "clé personne"),
                          ('idTache', "i", "clé tache"), ('dateRendezVous', "d", "date du RV"),
                          ('lieuRendezVous', 80, "lieu du RV")]}

   def afficher_parametres_connexion(self):
      """ affiche les paramètres """
      pass

   def afficher_parametres_tables(self):
      """ affiche les paramètres """
      pass

class Enregistreur:
   """
   classe pour gérer l'insertion d'enregistrements divers venus de la saisie
   pour chaque champ, on teste simplement des exemples d'expressions régulières
   d'autres plus conséquents sont à ajouter
   par exemple numérique avec distinction positif, décimal,...
   par exemple un vrai k de date à ajouter, ...
   """

   def __init__(self, database, table):
      """ Constructeur de table """
      self.database = database                           # lien sur BD
      self.table = table                                 # nom de la table
      self.descriptif = Glob.dicoT[table]                # descriptif des champs

   def entrer(self):
      """ procédure d'entrée d'un enregistrement entier """
      fmtdate = "%d/%m/%Y"                               # format de date accepté pour BD
      erentier = r"[0-9]+"                               # expression régulière acceptée pour un entier positif
      erdate = r"[0-3][0-9]\/[0-1][0-9]\/[0-9]{4}"       # expression régulière acceptée pour une date (...)

      champs = "("                                        # ébauche de chaîne pour les noms de champs
      valeurs = "("                                       # ébauche de chaîne pour les valeurs

      # Demander successivement une valeur pour chaque champ
      for cha, datatype, nom in self.descriptif:
         if datatype == "k":                             # on ne demandera pas de saisie de n° d'enregistrement
            continue                                     # à l'utilisateur quiand le champ est clé primaire (numérotation auto.)
         champs = champs + cha + ","
         val = input("Entrez le champ %s :" % nom)
         if datatype == "i":
            if not expreg.match(erentier, val):
               print("\nSaisie incorrecte : %s pour masque %s" % (val, erentier))
               return 1
            valeurs = valeurs + val + ","
         elif datatype == "d":
            if not expreg.match(erdate, val):
               print("\nSaisie incorrecte : %s pour masque %s" % (val, erdate))
               return 1
            valeurs = valeurs + "STR_TO_DATE('%s','%s')," % (val, fmtdate)
         else:
            valeurs = valeurs + "'%s'," % (val)
      # Mettre en forme et exécuter la requête
      champs = champs[:-1] + ")"                      # supprimer la dernière virgule
      valeurs = valeurs[:-1] + ")"                    # puis ajouter une parenthèse aux variables de requêtes
      requete = "INSERT INTO %s %s VALUES %s" % (self.table, champs, valeurs)
      self.database.executer_requete(requete)
      # autre insertion ou non
      encore = input("Continuer (O/N) ? ")
      if encore.upper() == "O":
         return 0
      else:
         return 1

   def afficher_parametres(self):
      """ affiche les paramètres """
      pass

class GestionBD:
   """
   Mise en place et interfaçage d'une base de données MySQL
   Classe utilisée pour ouvrir, fermer et committer la BD
   Créer, supprimer les tables
   Et même exécuter des requêtes utilisateurs
   """

   def __init__(self, dbName, user, passwd, host):
      """ Constructeur qui établit la connexion éventuellement 1 paramètre de plus (..., port =3306) """
      try:
         self.connexion = mdb.connect(db=dbName, user=user, passwd=passwd, host=host)
      except Exception as err:
         print('La connexion BD a échoué :\n Erreur détectée :\n%s' % err)
         self.echec = 1
      else:
         self.cursor = self.connexion.cursor()   # création du curseur
         self.echec = 0

   def creer_tables(self, dico_tables):
      """ Création des tables décrites dans le dictionnaire dico_tables """
      for table in dico_tables:                            # parcours des clés du dict.
         requete = "CREATE TABLE %s (" % table
         pkey = ''
         for descr in dico_tables[table]:
            nom_champ = descr[0]                          # libellé du champ à créer
            tch = descr[1]                               # type de champ à créer
            if tch == 'i':
               # champ entier
               type_champ = 'INTEGER'
            elif tch == 'd':
               # champ date
               type_champ = 'DATE'
            elif tch == 'k':
               # champ 'clé primaire' (incrémenté automatiquement)
               type_champ = 'INTEGER AUTO_INCREMENT'
               pkey = nom_champ
            else:
               # champ texte
               type_champ = 'VARCHAR(%s)' % tch
            # construction de la requête
            requete = requete + "%s %s, " % (nom_champ, type_champ)
         # terminaison et exécution de la requête
         if pkey == '':
            requete = requete[:-2] + ")"
         else:
            requete = requete + "CONSTRAINT %s_pk PRIMARY KEY(%s))" % (pkey, pkey)
         self.executer_requete(requete)
      # transfert -> disque
      self.commiter_base()

   def supprimer_tables(self, dico_tables):
      """ Suppression des tables décrites dans le dictionnaire """
      for table in dico_tables.keys():
         requete = "DROP TABLE %s" % table
         self.executer_requete(requete)
      # transfert -> disque
      self.commiter_base()

   def executer_requete(self, requete):
      """ Exécution de la requête saisie par l'utilisateur, avec détection d'erreur éventuelle """
      try:
         self.cursor.execute(requete)
      except Exception as err:
         # afficher la requête et le message d'erreur système :
         print("Requête SQL incorrecte :\n%s\nErreur détectée :\n%s" % (requete, err))
         return 0
      else:
         return 1

   def afficher_resultat(self):
      """ Renvoi du résultat de la requête précédente (un tuple de tuples) """
      return self.cursor.fetchall()

   def commiter_base(self):
      """ Validation en BD avec transfert curseur vers disque """
      if self.connexion:
         self.connexion.commit()

   def fermer_base(self):
      """ Clôture de BD """
      if self.connexion:
         self.connexion.close()


"""
Programme principal
Connexion
Boucle de saisie d'action
Validation
Déconnexion
"""

# Création de l'objet-interface avec la base de données
base = GestionBD(Glob.dbName, Glob.user, Glob.passwd, Glob.host)
if base.echec:
   sys.exit()

# Boucle infinie d'affichage
while 1:
   print("\nQue voulez-vous faire :\n"\
      "1) Créer les tables de la base de données\n"\
      "2) Supprimer les tables de la base de données ?\n"\
      "3) Entrer des personnes\n"\
      "4) Entrer des taches\n"\
      "5) Entrer des rendez-vous\n"\
      "6) Lister les personnes\n"\
      "7) Lister les taches\n"\
      "8) Lister les rendez-vous\n"\
      "9) Exécuter une requête SQL quelconque\n"\
      "0) terminer\n")
   choix = int(input("Choisissez votre action ? "))
   if choix == 1:
      # création de toutes les tables décrites dans le dictionnaire
      base.creer_tables(Glob.dicoT)
   elif choix == 2:
      # suppression de toutes les tables décrites dans le dic.
      base.supprimer_tables(Glob.dicoT)
   elif choix == 3 or choix == 4 or choix == 5:
      # création d'un <enregistreur> de personnes ou de taches ou de rendez-vous
      nomtable = {3:'personnes', 4:'taches', 5:'rendezvous'}[choix]
      enreg = Enregistreur(base, nomtable)
      while 1:
         if enreg.entrer():
            break
   elif choix == 6 or choix == 7 or choix == 8:
      # listage de toutes les personnes, ou toutes les taches ou tous les rendez-vous
      nomtable = {6:'personnes', 7:'taches', 8:'rendezvous'}[choix]
      if base.executer_requete("SELECT * FROM %s" % nomtable):
         # analyser le résultat de la requête ci-dessus :
         print("\nTable : %s\n" % (nomtable))
         records = base.afficher_resultat()        # ce sera un tuple de tuples
         for rec in records:                       # => chaque enregistrement
            ligne = []
            ligne.append('Enregistrement : ')
            for item in rec:                       # => chaque champ dans l'enreg
               ligne.append(' ')
               ligne.append(item)                  # => complètent une ligne
            print(ligne)                           # => qui est affichée
   elif choix == 9:
      req = input("Entrez votre requête SQL : ")
      if base.executer_requete(req):
         print(base.afficher_resultat())          # ce sera un tuple de tuples
   else:
      base.commiter_base()
      base.fermer_base()
      break
