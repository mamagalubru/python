#!C:\Python34\python.exe
# -*- coding: utf-8 -*-


"""
teste quelques propriétés 
"""

import cherrypy

# classe web
class MonSiteWeb(object):
    def index(self):
        return "<h1>Bonjour</h1>"
    index.exposed = True
    

# programme principal
cherrypy.quickstart(MonSiteWeb(), config = "tutoriel.conf")
