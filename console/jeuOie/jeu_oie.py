#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2013, Adrien Tétar. All Rights Reserved.
# Créé par bruno, le 10/12/2016 en Python 3.4
#
import random
import sys
import os

def errNumber():
	print("Nombre de joueurs incorrect.")
	exit(0)

def jet():
	d1 = random.randrange(1, 7)
	d2 = random.randrange(1, 7)
	if (d1+d2 == 9):
		return (d1+d2, d1)
	else:
		return (d1+d2, 0)

def printf(string):
	print(string)
	input()

def argsort(seq):
	return [x for x,y in sorted(enumerate(seq), key = lambda x: x[1])]

def ordre(number):
	res = [0] * number
	for i in range(0, number):
		printf("Le joueur " + str(i+1) + " lance les dés..")
		res[i] = jet()[0]
		printf(res[i])
	# Check for duplicates
	if (len(set(res)) == len(res)):
		# [::-1] will reverse the array because we want it decreasingly sorted
		return argsort(res)[::-1]
	else:
		print("Il faut recommencer le tirage.")
		return ordre(number)

def infoJoueurs(ordre):
	for i in range(0, len(ordre)):
		if (i == 0):
			print("\nLe joueur " + str(ordre[i]+1) + " commence"),
		elif (i == 1):
			print(", suivi du joueur " + str(ordre[i]+1)),
		else:
			print(", puis du joueur " + str(ordre[i]+1)),
	print(".")

print("#################### Jeu de l'oie ####################")
if (len(sys.argv) < 2 or sys.argv[1] == "help"):
	print("Il s'agit d'un jeu de l'oie en ligne de commandes.")
	print("Le but est d'atteindre le jardin de l'oie qui se situe\nà la 63ième "
		+ "case, mais attention... des pièges sont là\npour altérer votre progression. "
		+ "Vous êtes prêt?\nSaisissez-vous des dés et tentez d'atteindre le jardin!\n")
	print("Usage: python oie.py <argument>\n")
	print("> Arguments acceptés:")
	print("'help': affiche cette fenêtre d'aide")
	print("nombre: nombre de joueurs, compris entre 2 et 4 inclus")
	print("> Dépendances:")
	print("Python 3")
	exit(0)
try:
	int(sys.argv[1])
except ValueError:
	errNumber()
if (int(sys.argv[1]) < 2 or int(sys.argv[1]) > 4):
	errNumber()
print("> Ordre de jeu:")
joueurs = ordre(int(sys.argv[1]))
infoJoueurs(joueurs)
print("\n> Début du jeu:")
premierTour = True
repos = [0] * int(sys.argv[1])
position = [0] * int(sys.argv[1])
puits = -1
prison = -1
while True:
	if (premierTour == False):
		print("\n> Nouveau tour! " + str(position))
	for i in range(0, len(joueurs)):
		if (repos[i] > 0):
			printf("Le joueur " + str(joueurs[i]+1) + " se repose pour " + str(repos[i]) + "tours.")
			repos[i] -= 1
		elif (puits == i):
			printf("Le joueur " + str(joueurs[i]+1) + " est coincé dans le puits...")
		elif (prison == i):
			printf("Le joueur " + str(joueurs[i]+1) + " est coincé en prison...")
		else:
			printf("Le joueur " + str(joueurs[i]+1) + " lance les dés...")
			cur = jet()
			printf(str(cur[0]) + ": vous vous rendez à la case " + str(position[i]+cur[0]) + ".\n")
			if (premierTour and (position[i]+cur[0]) % 9 == 0):
				printf("Une oie vous empêche de vous arrêter!")
				printf("Vous avancez encore du nombre de cases indiqué par les dés.")
				position[i] += 2 * cur[0]
			elif (position[i]+cur[0] == 9):
				print("Vous avez fait 9 au premier tour!")
				if (cur[1] == 6 or cur[1] == 3):
					printf("6+3... vous passez directement à la case 26.")
					position[i] = 26
				else: # (cur[1] == 4 or cur[1] == 5)
					printf("4+5... vous passez directement à la case 53.")
					position[i] = 53
			elif (position[i]+cur[0] == 6):
				printf("Vous êtes sur la case 6... un pont vous fait passer à la case 12!")
				position[i] = 12
			elif (position[i]+cur[0] == 19):
				printf("Vous êtes sur la case 19... vous décidez de séjourner à l'hôtel!")
				repos[i] = 2
			elif (position[i]+cur[0] == 31):
				if (puits == 0):
					printf("Vous êtes tombé dans un puits... vous attendez de l'aide des autres joueurs.")
					puits = i
				else:
					printf("Vous êtes tombé dans un puits... mais vous avez sauvé le joueur " + str(puits) + " au passage!")
					puits = i
			elif (position[i]+cur[0] == 42):
				printf("Vous êtes tombé dans un labyrinthe... vous finissez par sortir à la case 30.")
				position[i] = 30
			elif (position[i]+cur[0] == 52):
				if (prison == 0):
					printf("Vous êtes en prison... vous attendez un quelconque signe des autres joueurs.")
					prison = i
				else:
					printf("Vous finissez en prison... mais vous avez libéré le joueur " + str(prison) + " au passage!")
					prison = i
			elif (position[i]+cur[0] == 58):
				printf("Vous avez rencontré la faucheuse... vous vous réveillez au départ du jeu.")
				position[i] = 0
			elif (position[i]+cur[0] == 63):
				printf("Vous avez gagné... bravo!")
				printf("Le joueur " + str(joueurs[i]+1) + " remporte la partie.")
				exit(0)
			elif (position[i]+cur[0] > 63):
				printf("Oups, vous avez manqué le jardin de l'oie... vous tombez " + str(position[i]+cur[0] - 63) + " cases derrière.")
				position[i] = 63 - (position[i]+cur[0] - 63)
			else:
				printf("L'endroit a l'air sûr.")
				position[i] = position[i]+cur[0]
premierTour = False
