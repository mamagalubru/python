#!C:\Python34\python.exe
# -*- coding: ISO-8859-1 -*-
"""
teste quelques propriétés sur l'écriture de fichier
"""
# ecrire sur un fichier dans le répertoire courant
fichier = open('ecriretexte.txt', 'w')
texte = '''Je suis rouge et bleu et vert et jaune à la fois \
(triple apostrophe) \
il dit "Qu'il est génant d'être étourdi et mauve à la fois" \
(échappement via antislash)  \n'''
print(texte)
fichier.write(texte)
fichier.close()
