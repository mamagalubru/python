#!/usr/bin/python
# -*- coding : utf-8 -*-
#
# helloworld2.py
# Un traditionnel ”Hello World” avec une approche objet plus propre

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

# Classe définissant un bouton avec le texte Hello World !
class HelloButton(QPushButton) :
   def __init__ (self, args) :
      QPushButton.__init__ (self,None)
      self.setText("Hello World !")

class HelloApplication(QApplication) :
   def __init__ (self, args) :
      QApplication.__init__ (self,args)
      # Creation et affichage d'un objet HelloButton
      self.button=HelloButton(self)
      self.button.show()
      # Traitement des divers evenements
      self.connect(self,SIGNAL("lastWindowClosed()"),self,SLOT("quit()"))
      self.connect(self.button,SIGNAL("clicked()"),self,SLOT("quit()"))
      #boucle principale de traitement des evenements
      self.exec_()

if __name__ == "__main__" :
   app=HelloApplication(sys.argv)