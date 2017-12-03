#!C:\Python34\python.exe
# -*- coding: utf-8 -*-

# on lance le site en créant simplement une classe avec 2 fonctions liées

class MonSiteWeb:
    def __init__(self, content_type, header, footer):
        self.content_type = '''Content-Type: text/html; charset=utf-8\n\n'''
        self.header = '''<HTML><HEAD><TITLE>BONJOUR</TITLE></HEAD><BODY><H1>MonSiteWeb Python</H1>\n'''
        self.footer = '''</BODY></HTML>'''

    def index(self):
        return '''<H2>Paragraphe produit par une première classe Python</H2>\n'''
    def bienvenue(self):
        return '''<H3>Paragraphe produit par une seconde classe Python</H3>\n'''

msw = MonSiteWeb("ct","hd","ft")
body = msw.index() + msw.bienvenue()
html = msw.content_type + msw.header + body + msw.footer
print(html)
