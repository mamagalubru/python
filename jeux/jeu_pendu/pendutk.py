# -*- coding: ISO-8859-1 -*-

# Ce fichier contient le jeu du pendu.
# Il s'appuie sur les fichiers :- pendudonneestk.py et pendufonctionstk.py

from tkinter import *
from pendudonneestk import *
from pendufonctionstk import *

# d�but des fonctions

def accepterNom():
   rc.utilisateur = entryjoueur.get()
   # pour debug print("Bonjour te voici !!! " + rc.utilisateur + '\n')
   rc.utilisateur = verif_nom_utilisateur(rc.utilisateur)
   # pour debug print('Jeu du Pendu pour ' + rc.utilisateur + '\n')
   titre.config(text='Jeu du Pendu pour ' + rc.utilisateur)
   titre.pack()
   labeljoueur.pack_forget()
   entryjoueur.pack_forget()
   boutonjoueur.pack_forget()
   # Si l'utilisateur n'a pas encore de score, on l'ajoute
   if rc.utilisateur not in rc.scores.keys():
      rc.scores[rc.utilisateur] = 0 # 0 point pour commencer

def accepterLettre(event):
   rc.lettre = entrylettre.get()
   # pour debug print("Bonjour te voil� !!! " + rc.lettre)
   penalite = verif_lettre(rc.lettre, rc.lettres_trouvees, rc.mot_a_trouver)
   rc.nb_chances = rc.nb_chances - penalite
   # recherche du mot
   rc.mot_trouve = recup_mot_masque(rc.mot_a_trouver, rc.lettres_trouvees)
   resultat.config(text='Resultat : ' + rc.mot_trouve + ' ' + str(rc.nb_chances))
   resultat.pack()
   entrylettre.delete(first=0,last=4)
   entrylettre.pack()
   afficherPendu()
   # A-t-on trouv� le mot, ou nos chances sont-elles �puis�es ?
   if rc.mot_a_trouver==rc.mot_trouve:
      print("F�licitation ! Vous avez trouv� le mot {0}.".format(rc.mot_a_trouver))
      # On met � jour le score utilisateur
      rc.scores[rc.utilisateur] += rc.nb_chances
      # on enregistre le score
      enregistrer_scores(rc.scores)
      # On affiche les scores utilisateur
      print("Vous finissez la partie avec {0} points.".format(rc.scores[rc.utilisateur]))

def afficherPendu():
   n = rc.nb_chances
   if n > 6:
      # dessin.create_line(x1,y1,x2,y2, fill = 'green', width = 5)
      dessin.create_line(10,10,10,98, fill = 'green', width = 5)
      dessin.create_line(10,10,98,10, fill = 'green', width = 5)
      dessin.create_line(10,25,25,10, fill = 'green', width = 5)
      dessin.create_line(5,98,15,98, fill = 'green', width = 5)
      print("Vous �tes d�j� sous l'�chafaud\n")
   elif n == 6:
      # dessin.create_line(x1,y1,x2,y2, fill = 'green', width = 5)
      dessin.create_line(50,10,50,20, fill = 'green', width = 2)
      print("Vous �tes sur la corde raide\n")
   elif n == 5:
      # dessin.create_oval(x1,y1,x2,y2, fill = 'orange', width = 0)
      dessin.create_oval(30,20,70,50, fill = 'orange', width = 0)
      print("Vous avez la t�te pendue\n")
   elif n == 4:
      # dessin.create_rectangle(x1,y1,x2,y2,outline = 'red', width = 10)
      dessin.create_rectangle(30, 50, 70, 80, fill = 'red', width = 0)
      print("Vous �tes pendu corps et �me\n")
   elif n == 3:
      # dessin.create_line(x1,y1,x2,y2, fill = 'green', width = 5)
      dessin.create_line(30,55,10,60, fill = 'red', width = 10)
      print("Vous �tes pendu un bras dans le vide\n")
   elif n == 2:
      # dessin.create_line(x1,y1,x2,y2, fill = 'green', width = 5)
      dessin.create_line(70,55,90,60, fill = 'red', width = 10)
      print("Vous �tes pendu deux bras dans le vide\n")
   elif n == 1:
      # dessin.create_line(x1,y1,x2,y2, fill = 'green', width = 5)
      dessin.create_line(35,80,40,95, fill = 'orange', width = 10)
      print("Vous �tes pendu une jambe dans le vide\n")
   else:
      # dessin.create_line(x1,y1,x2,y2, fill = 'green', width = 5)
      dessin.create_line(65,80,60,95, fill = 'orange', width = 10)
      # dessin.create_text(x1,y1,text = 'PENDU !!!')
      dessin.create_text(50, 35, text = 'pendu')
      print("Vous �tes pendu !!!\n")
   dessin.pack()
    
# d�but du programme

# On cr�e la classe recherche
rc = Recherche()
# On r�cup�re les scores de la partie
rc.scores = recup_scores()
# On r�cup�re les mots � trouver
rc.mot_a_trouver = choisir_mot()

# cr�ation de la fen�tre, vous pouvez choisir le nom que vous voulez pour votre fen�tre
tk = Tk()
# cr�ation du label contenant le texte "Jeu du Pendu " de couleur noire
titre = Label(tk, text='Jeu du Pendu pour ' + rc.utilisateur)
# ins�re le texte dans la fen�tre
titre.pack()

# cr�ation du label contenant le texte "Saisir votre nom " de couleur noire
labeljoueur = Label(tk, text='saisir votre nom ')
labeljoueur.pack()
# cr�ation entr�e contenant le nom
entryjoueur = Entry(tk, width = 30)
entryjoueur.pack()
# cr�ation du bouton, associ� � l'action valider le nom du joueur
boutonjoueur = Button(tk, text="valider le nom du joueur", command=accepterNom)
boutonjoueur.pack()

# cr�ation du label contenant le texte "Saisir votre lettre " de couleur noire
labellettre = Label(tk, text='saisir une seule lettre puis Return')
labellettre.pack()
# cr�ation entr�e contenant une lettre et liaison action via touche Return
entrylettre = Entry(tk, width = 2)
entrylettre.pack()
entrylettre.bind("<Return>",accepterLettre)

# cr�ation du label contenant le r�sultat mot_trouve de couleur noire
resultat = Label(tk, text='Resultat � venir ')
# ins�re le texte dans la fen�tre
resultat.pack()

# cr�ation du canevas qui va dessiner le pendu
dessin = Canvas(tk, width = 100, height = 100)
# dessin.create_rectangle(x1,y1,x2,y2,outline = 'blue', width = 5)
dessin.create_rectangle(5,5,100,100,outline = 'blue', width = 1)
dessin.pack()

# mettre � jour
tk.update()
tk.geometry(tk.geometry())

# lance la boucle principale
tk.mainloop()

