#!C:\Python34\python.exe
# -*- coding: utf-8 -*-

# on lance le programme en créant simplement une classe

class MonSiteWeb:
    def index():
        return '''<H3>Page index web produite par une classe Python</H3>'''

msw = MonSiteWeb
print('Content-Type: text/html; charset=utf-8\n\n')
header = '''<HTML><HEAD><TITLE>BONJOUR</TITLE></HEAD><BODY><H1>MonSiteWeb Python</H1>'''
footer = '''</BODY></HTML>'''
body = msw.index()
html = header + body + footer
print(html)
