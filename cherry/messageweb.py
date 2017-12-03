#!C:\Python34\python.exe
# -*- coding: utf-8 -*-


"""
teste quelques propriétés web du serveur cherrypy
"""

# import du module web
import cherrypy

# classe web
class MonSiteWeb(object):
    # renvoie une page HTML index avec un lien vers une autre page unMessage
    def index(self):
        return '''
    <h2>Veuillez <a href="unMessage">cliquer ici </a>
    pour accéder à une page liée</h2>
    '''
    index.exposed = True

    # une autre méthode unMessage du même objet suffit pour produire la page
    def unMessage(self):
        return "<h1>génial, c'est l'index qui m'appelle</h1>"
    unMessage.exposed = True
    

# programme principal ==> démarrage du serveur web
cherrypy.quickstart(MonSiteWeb(), config = "tutoriel.conf")
