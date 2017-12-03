#!C:\Python34\python.exe
# -*- coding: utf-8 -*-
"""
lecture de fichier xml
parcourant chaque noeud nommé
"""
from xml.dom import minidom
# lire tout un fichier xml du répertoire courant 
doc = minidom.parse('contacts.xml')
# parcourir chaque noeud contact
contacts = doc.getElementsByTagName('contact')
for contact in contacts:
    attrs   = contact.attributes
    nom = attrs['name']
    prenom = attrs['firstname']
    print(prenom.nodeValue," ",nom.nodeValue)
# parcourir chaque noeud programming
progs = doc.getElementsByTagName('programming')
for prog in progs:
    specs   = prog.attributes
    spec = specs['lang']
    print("Spécialité : ",spec.nodeValue)
