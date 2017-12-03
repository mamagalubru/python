#!C:\Python34\python.exe
# -*- coding: utf-8 -*-

# on récupère et affiche les données transmises par un formulaire HTML

import cgi

form = cgi.FieldStorage()
nomv = form["visiteur"].value
texte = form["phrase"].value
print('Content-Type: text/html; charset=utf-8\n\n')
print('''<HTML><BODY>''')
print('''<H3>Merci, %s !</H3>''' % (nomv))
print('''<H4>Voici votre texte : %s !</H4>''' % (texte))

l=text.split()
print('''<P> %s </P>''' % (l))
for mot in l:
	print('''<P> %s </P>''' % (mot))


print('''</BODY></HTML>''')
