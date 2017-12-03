#!C:\Python34\python.exe
# -*- coding: utf-8 -*-
"""
teste des propriétés de lecture de fichier csv
"""
import csv
# lire tout un fichier csv du répertoire courant
fname = "contacts.csv"
file = open(fname, "rt")
try:
    reader = csv.reader(file)
    for row in reader:
        #
        # affiche la ligne entière lue
        #
        print("Ligne entière : ",row)
        #
        # N'affiche que colonne par colonne
        #
        print("1ère colonne : ",row[0])
        print("2ème colonne : ",row[1])
        print("3ème colonne : ",row[2])
        print("4ème colonne : ",row[2])

finally:
    file.close()
