#!C:\Python34\python.exe
# -*- coding: utf-8 -*-
"""
teste quelques propriétés en ecriture de fichier
"""
# ecrire sur un fichier dans le répertoire courant
fichier = open('ecriretout.txt', 'w')
texte = '''Je suis rouge et bleu et vert et jaune à la fois \
(triple apostrophe) \
il dit "Qu'il est génant d'être étourdi et mauve à la fois" \
(échappement via antislash)  \n'''
print(texte)
fichier.write(texte)
fichier.close()
# ecrire ligne par ligne en append
fichier = open('ecriretout.txt', 'a')
for i in range(1, 11):
    texte = "Ajoutée à la fin, je suis la ligne "+str(i)+"\n"
    print(texte)
    fichier.write(texte)
fichier.close()
