#!C:\Python34\python.exe
# coding: utf8
"""
teste quelques propriétés de lecture de conte
"""
# lire tout un fichier du répertoire avec readlines
fichier = open('lireconte.txt','r')
liste = fichier.readlines()
for ligne in liste:
  print(ligne)
fichier.close()
# lire tout un fichier ligne par ligne avec readline
fichier = open('lireconte.txt','r')
while 1:
  ligne = fichier.readline()
  if ligne == '':
    break
  print(ligne)
fichier.close()
