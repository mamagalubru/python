# -*- coding: cp1252 -*-

#import des modules utilisés
import random
import time

# Ce fichier définit quelques données partagées (forme de variables)
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

# classe joueur
class Joueur():
    # variables statiques de classe initialisées par défaut, mais changées au fil du jeu
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

    #fonction de lancer de 2 dés aleatoire + cases speciales
    def lancerdes(self):
        de1 = random.randint(1,6)
        de2 = random.randint(1,6)
        des = de1 + de2
        pos = self.position
        num = self.numero
        texte = "Joueur => " + str(num) + "\nPos AV => " + str(pos) + "\nDé1Dé2 => " + str(des) + "\nPos AP => " + str(des+pos)
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
        # déplacer le pion dans tous les cas
        self.deplacerpion()
        # inventer une phrase
        self.inventerphrase()
        # passer au joueur suivant
        self.changerjoueur()
        return

    def bloquer(self, de1, de2):
        # on regarde si bloqué dans le puits auparavant pour vérifier la libération
        pos = self.position
        texte = "RAS"
        if pos == 31 :
            if de1 == 6 or de2 == 6 :
                texte = "Vous avez fait un 6 ! \n Vous pouvez sortir du puits !"
            else :
                texte = "Vous n'avez pas fait un 6 ! \n Vous nagez toujours au fond du puits !"
                self.changerjoueur()
        # on regarde si bloqué en prison auparavant pour vérifier la libération
        if pos == 52 :
            self.compteur = self.compteur - 1
            if self.compteur < 1 :
                texte = "Vous êtes liberé de prison!"
            else :
                texte = "Vous restez encore bloqué en prison !"
                self.changerjoueur()
        self.dialogueNorth.set(texte)

    def deplacer(self, des):
        # on effectue le deplacement lié au tirage des dés :de1,de2
        self.position = self.position + des
        pos = self.position
        texte = "RAS"
        gagne = False
        # case trop haut
        if pos > 63 :
            texte = "Dommage, vous avez dépassé la cible !"
            trop = pos - 63
            pos = 63 - trop
        # cases bonus
        elif pos  == 6 :
            texte = "Pont : Vous avez pris le pont ! Vous passez directement à la case 12 !"
            pos = 12
        elif pos == 9 or pos ==18 or pos ==27 or pos ==36 or pos ==45 or pos ==54 :
            texte = "Vous êtes sur une case ''oie'' ! Vous doublez votre lancer de dés !"
            pos = pos + des
        # cases malus
        elif pos == 31 :
            texte = "Vous êtes au puits ! Vous devrez faire un 6 avec un des deux dés pour sortir !"
            pos = 31
        elif pos == 42 :
            texte = "Vous vous êtes perdu dans le labyrinthe ! Vous passez à la case 30 !"
            pos = 30
        elif pos == 52 :
            self.compteur = 3
            texte = "Vous êtes bloqué pour quelques tours en prison !"
            pos = 52
        elif pos == 58 :
            texte = "Mort : Vous êtes DEAD ! Vous retournez au départ !"
            pos = 1
        # case gagné
        elif pos == 63 :
            texte = "Bravo, vous avez gagné joueur " + str(self.numero)
            gagne = True
        self.position = pos
        self.dialogueNorth.set(texte)
        print("Joueur : " + str(self.numero) + " Dés : " + str(des) + " Case : " + str(pos))
        return gagne

    def deplacerpion(self):
        # déplacer le pion si possible
        x = casex[self.position]- 3*self.numero
        y = casey[self.position]- 3*self.numero
        if x < largeurCanevas and y < hauteurCanevas:
            self.canevas.coords(self.image,x,y)
            self.canevas.update()

    def inventerphrase(self):
        # inventer une petite phrase si rien d'autre n'est affiché
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

