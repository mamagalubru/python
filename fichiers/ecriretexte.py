#!C:\Python34\python.exe
# -*- coding: ISO-8859-1 -*-
"""
teste quelques propri�t�s sur l'�criture de fichier
"""
# ecrire sur un fichier dans le r�pertoire courant
fichier = open('ecriretexte.txt', 'w')
texte = '''Je suis rouge et bleu et vert et jaune � la fois \
(triple apostrophe) \
il dit "Qu'il est g�nant d'�tre �tourdi et mauve � la fois" \
(�chappement via antislash)  \n'''
print(texte)
fichier.write(texte)
fichier.close()
