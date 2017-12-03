# -*- coding: cp1252 -*-

# Ce fichier définit quelques données, sous la forme de variables, utiles au programme oie

#variables globales
nbjoueurs=1
numjoueur=1
ralenti=0.09
largeurCanevas = 780
hauteurCanevas = 800

compteur=[0,0,0,0,0,0,0]
numcase=[0,1,1,1,1,1,1]
casex=[0, 40,130,230,320,415,510,610,700,700,700,700,700,700,700,700,610,510,415,320,230,130, 40, 40, 40, 40, 40, 40, 40,130,230,320,415,510,610,610,610,610,610,610,510,415,320,230,130,130,130,130,130,230,320,415,510,510,510,510,415,320,230,230,230,320,415,415]
casey=[0,710,710,710,710,710,710,710,710,615,520,425,325,230,135, 42, 42, 42, 42, 42,42,42,42,135,230,325,425,520,615,615,615,615,615,615,615,520,425,325,230,135,135,135,135,135,135,230,325,425,520,520,520,520,520,425,325,230,230,230,230,325,425,425,425,325]

itemphoto=1
item1=2
item2=3
item3=4
item4=5
item5=6
item6=7
pionjoueur=[0,item1,item2,item3,item4,item5,item6]

# Liste des phrases du jeu
liste_phrases = [
   "Mysql reste une base de données libre jusqu'en en 2008, \n Sun Microsystems achète alors MySQL, \n puis est acheté par Oracle en 2010.",
   "Lors de l'installation mysql, il faut se connecter en root \n pour créer d'autres utilisateurs à qui \n on donne des droits via la commande GRANT",
   "La fille de Michael « Monty » Widenius,  \n My, a donné son nom à MySQL",
   "Mysql, grâce à son succès international sur la toile \n permet de créer des formulaires de type WEB \n avec l’aide principalement du langage PHP ",
   "Mysql a été conçue pour saisir, lier et mettre en ordre \n les données présentant des relations \n et des contraintes entre elles",
   "SQL est un langage qui libère le programmeur \n de la spécification physique \n des chemins d’accès aux données",
   "Les noms des objets doivent être les plus expressifs possibles, \n utiliser des conventions de nommage, \n n'utiliser ni espaces ni caractères accentués",
   "InnoDB est le moteur de stockage par défaut pour le SGBDR MySQL, \n il est inclus d'origine dans toutes \n les distributions fournies par MySQL AB",
   "L'intégrité référentielle permet de vérifier la présence \n d'une donnée liée avant l'insertion \n ou la mise à jour de nouvelles données",
   "Un trigger (ou déclencheur) est une action à effectuer \n sur la base de données lors de l'occurrence \n d'un événement sur cette base de données",
   "Une des tâches principales d'un SGBD est d'assurer la sécurité \n des données en protégeant les accès aux données \n par un système de droits",
   "Le logiciel MySQL (TM) est un serveur de base de données \n très rapide, multi-thread, multiutilisateur, \n MySQL est une marque déposée de MySQL AB",
   "La table est le principal composant d’une BD, \n elle contient toutes les données concernant un tableau de valeurs \n et possède en général au moins 1 index",
   "Une vue est une requête enregistrée qui permet \n d’interroger et d’extraire les données en effectuant des choix \n notamment de sélection (SELECT)",
   "Un trigger (ou déclencheur) est une action complémentaire à effectuer \n planifiée sur la base de données \n lors de l'occurrence d'un événement (event) ",
   "Une base de données est représentée par une arborescence de fichiers, \n Mysql gère plusieurs databases réparties \n chacune sur un dossier différent ",
   "Mysql utilise en standard l’avantage majeur du modèle relationnel \n qui est l’indépendance complète entre les descriptions \n logiques et physiques",
   "La commande DROP DATABASE permet de supprimer \n totalement une base de données \n et tout ce qu’elle contient",
   "Une fois la convention acceptée par toute l'équipe de développement \n il faut la rendre publique \n et mettre en œuvre des contrôles systématiques",
   "Une table a une structure lignes / colonnes identique à celle \n des feuilles de calcul d’un tableur \n avec des lignes et des colonnes",
   "Pour relier 2 tables celles-ci doivent contenir \n au moins un champ commun et de même type \n dont les noms peuvent être différents)",
]
