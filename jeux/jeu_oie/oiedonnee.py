# -*- coding: cp1252 -*-

# Ce fichier d�finit quelques donn�es, sous la forme de variables, utiles au programme oie

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
   "Mysql reste une base de donn�es libre jusqu'en en 2008, \n Sun Microsystems ach�te alors MySQL, \n puis est achet� par Oracle en 2010.",
   "Lors de l'installation mysql, il faut se connecter en root \n pour cr�er d'autres utilisateurs � qui \n on donne des droits via la commande GRANT",
   "La fille de Michael � Monty � Widenius,  \n My, a donn� son nom � MySQL",
   "Mysql, gr�ce � son succ�s international sur la toile \n permet de cr�er des formulaires de type WEB \n avec l�aide principalement du langage PHP ",
   "Mysql a �t� con�ue pour saisir, lier et mettre en ordre \n les donn�es pr�sentant des relations \n et des contraintes entre elles",
   "SQL est un langage qui lib�re le programmeur \n de la sp�cification physique \n des chemins d�acc�s aux donn�es",
   "Les noms des objets doivent �tre les plus expressifs possibles, \n utiliser des conventions de nommage, \n n'utiliser ni espaces ni caract�res accentu�s",
   "InnoDB est le moteur de stockage par d�faut pour le SGBDR MySQL, \n il est inclus d'origine dans toutes \n les distributions fournies par MySQL AB",
   "L'int�grit� r�f�rentielle permet de v�rifier la pr�sence \n d'une donn�e li�e avant l'insertion \n ou la mise � jour de nouvelles donn�es",
   "Un trigger (ou d�clencheur) est une action � effectuer \n sur la base de donn�es lors de l'occurrence \n d'un �v�nement sur cette base de donn�es",
   "Une des t�ches principales d'un SGBD est d'assurer la s�curit� \n des donn�es en prot�geant les acc�s aux donn�es \n par un syst�me de droits",
   "Le logiciel MySQL (TM) est un serveur de base de donn�es \n tr�s rapide, multi-thread, multiutilisateur, \n MySQL est une marque d�pos�e de MySQL AB",
   "La table est le principal composant d�une BD, \n elle contient toutes les donn�es concernant un tableau de valeurs \n et poss�de en g�n�ral au moins 1 index",
   "Une vue est une requ�te enregistr�e qui permet \n d�interroger et d�extraire les donn�es en effectuant des choix \n notamment de s�lection (SELECT)",
   "Un trigger (ou d�clencheur) est une action compl�mentaire � effectuer \n planifi�e sur la base de donn�es \n lors de l'occurrence d'un �v�nement (event) ",
   "Une base de donn�es est repr�sent�e par une arborescence de fichiers, \n Mysql g�re plusieurs databases r�parties \n chacune sur un dossier diff�rent ",
   "Mysql utilise en standard l�avantage majeur du mod�le relationnel \n qui est l�ind�pendance compl�te entre les descriptions \n logiques et physiques",
   "La commande DROP DATABASE permet de supprimer \n totalement une base de donn�es \n et tout ce qu�elle contient",
   "Une fois la convention accept�e par toute l'�quipe de d�veloppement \n il faut la rendre publique \n et mettre en �uvre des contr�les syst�matiques",
   "Une table a une structure lignes / colonnes identique � celle \n des feuilles de calcul d�un tableur \n avec des lignes et des colonnes",
   "Pour relier 2 tables celles-ci doivent contenir \n au moins un champ commun et de m�me type \n dont les noms peuvent �tre diff�rents)",
]
