# -*- coding: cp1252 -*-

#import des modules utilis�s
import random
import time

# Ce fichier d�finit quelques donn�es partag�es (forme de variables)
# et la classe Joueur utiles au programme oie

#variables globales
largeurCanevas = 780
hauteurCanevas = 783
gagne = False
casex=[0, 40,130,230,320,415,510,610,700,700,700,700,700,700,700,700,610,510,415,320,230,130, 40, 40, 40, 40, 40, 40, 40,130,230,320,415,510,610,610,610,610,610,610,510,415,320,230,130,130,130,130,130,230,320,415,510,510,510,510,415,320,230,230,230,320,415,415]
#casey=[0,710,710,710,710,710,710,710,710,615,520,425,325,230,135, 42, 42, 42, 42, 42,42,42,42,135,230,325,425,520,615,615,615,615,615,615,615,520,425,325,230,135,135,135,135,135,135,230,325,425,520,520,520,520,520,425,325,230,230,230,230,325,425,425,425,325]
casey=[0,700,700,700,700,700,700,700,700,605,510,415,315,220,125, 32, 32, 32, 32, 32,32,32,32,125,220,315,415,510,605,605,605,605,605,605,605,510,415,315,220,125,125,125,125,125,125,220,315,415,510,510,510,510,510,415,315,220,220,220,220,315,415,415,415,315]

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

# classe joueur
class Joueur():
    # variables statiques de classe initialis�es par d�faut, mais chang�es au fil du jeu
    numerojoueurencours = 1
    nombreJoueurs = 4

    # constructeurs
    def __init__(self, numero, position, compteur, canevas, img, dialogueEast, dialogueNorth, dialogueSouth, dialogueBouton, bouton):
        self.numero = numero
        self.position = position
        self.compteur = compteur
        self.canevas = canevas
        self.image = img
        self.dialogueEast = dialogueEast
        self.dialogueNorth = dialogueNorth
        self.dialogueSouth = dialogueSouth
        self.dialogueBouton = dialogueBouton
        self.bouton = bouton

    #fonction de lancer de 2 d�s aleatoire + cases speciales
    def lancerdes(self):
        de1 = random.randint(1,6)
        de2 = random.randint(1,6)
        des = de1 + de2
        pos = self.position
        num = self.numero
        texte = "Joueur => " + str(num) + "\nPos AV => " + str(pos) + "\nD�1D�2 => " + str(des) + "\nPos AP => " + str(des+pos)
        self.dialogueEast.set(texte)
        self.bloquer(de1, de2)
        gagne = self.deplacer(des)
        if gagne:
            self.canevas.coords(self.image,415,325)
            self.canevas.update()
            self.bouton.text = "BRAVO !!!"
            self.bouton.pack()
            time.sleep(2)
            self.bouton.destroy()
            return
        # d�placer le pion dans tous les cas
        self.deplacerpion()
        # inventer une phrase
        self.inventerphrase()
        # passer au joueur suivant
        self.changerjoueur()
        return

    def bloquer(self, de1, de2):
        # on regarde si bloqu� dans le puits auparavant pour v�rifier la lib�ration
        pos = self.position
        texte = "RAS"
        if pos == 31 :
            if de1 == 6 or de2 == 6 :
                texte = "Vous avez fait un 6 ! \n Vous pouvez sortir du puits !"
            else :
                texte = "Vous n'avez pas fait un 6 ! \n Vous nagez toujours au fond du puits !"
                self.changerjoueur()
        # on regarde si bloqu� en prison auparavant pour v�rifier la lib�ration
        if pos == 52 :
            self.compteur = self.compteur - 1
            if self.compteur < 1 :
                texte = "Vous �tes liber� de prison!"
            else :
                texte = "Vous restez encore bloqu� en prison !"
                self.changerjoueur()
        self.dialogueNorth.set(texte)

    def deplacer(self, des):
        # on effectue le deplacement li� au tirage des d�s :de1,de2
        self.position = self.position + des
        pos = self.position
        texte = "RAS"
        gagne = False
        # case trop haut
        if pos > 63 :
            texte = "Dommage, vous avez d�pass� la cible !"
            trop = pos - 63
            pos = 63 - trop
        # cases bonus
        elif pos  == 6 :
            texte = "Pont : Vous avez pris le pont ! Vous passez directement � la case 12 !"
            pos = 12
        elif pos == 9 or pos ==18 or pos ==27 or pos ==36 or pos ==45 or pos ==54 :
            texte = "Vous �tes sur une case ''oie'' ! Vous doublez votre lancer de d�s !"
            pos = pos + des
        # cases malus
        elif pos == 31 :
            texte = "Vous �tes au puits ! Vous devrez faire un 6 avec un des deux d�s pour sortir !"
            pos = 31
        elif pos == 42 :
            texte = "Vous vous �tes perdu dans le labyrinthe ! Vous passez � la case 30 !"
            pos = 30
        elif pos == 52 :
            self.compteur = 3
            texte = "Vous �tes bloqu� pour quelques tours en prison !"
            pos = 52
        elif pos == 58 :
            texte = "Mort : Vous �tes DEAD ! Vous retournez au d�part !"
            pos = 1
        # case gagn�
        elif pos == 63 :
            texte = "Bravo, vous avez gagn� joueur " + str(self.numero)
            gagne = True
        self.position = pos
        self.dialogueNorth.set(texte)
        print("Joueur : " + str(self.numero) + " D�s : " + str(des) + " Case : " + str(pos))
        return gagne

    def deplacerpion(self):
        # d�placer le pion si possible
        x = casex[self.position]- 3*self.numero
        y = casey[self.position]- 3*self.numero
        if x < largeurCanevas and y < hauteurCanevas:
            self.canevas.coords(self.image,x,y)
            self.canevas.update()

    def inventerphrase(self):
        # inventer une petite phrase si rien d'autre n'est affich�
        phrase = liste_phrases[random.randint(1,20)]
        self.dialogueSouth.set(phrase)

    def changerjoueur(self):
        # passer au joueur suivant
        Joueur.numerojoueurencours = Joueur.numerojoueurencours + 1
        if Joueur.numerojoueurencours > Joueur.nombreJoueurs:
            Joueur.numerojoueurencours=1
        texte = 'A toi, joueur ' + str(Joueur.numerojoueurencours)
        self.dialogueBouton.set(texte)
        print(texte)

