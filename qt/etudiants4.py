#!/usr/bin/python
# -*- coding : utf-8 -*-
#
# qmainwindow.py
# Programme exemple pour la classe QMainWindow
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
class Demo(QApplication) :
   def __init__(self, args) :
      QApplication.__init__(self,args)
      # widget principal, il s'agit d'une fenêtre de dialogue
      self.main = QMainWindow()
      self.main.setWindowTitle("Demo QMainWindow")
      self.main.resize(640,480)
      #widget central : QTextEdit
      self.edit = QTextEdit("editor", self.main)
      self.edit.setFocus()
      self.main.setCentralWidget(self.edit)
      # ajout facile d'éléments dans la barre de menu
      # NOTE : crée la barre s'il n'existe pas
      self.main.menuBar().addAction("New")
      self.main.menuBar().addAction("Quit")
      # changement du message de status
      # NOTE : crée la zone de status si inexistante
      self.main.statusBar().showMessage("Demo en cours", 10000)
      self.main.show()
      self.connect(self,SIGNAL("lastWindowClosed()"),self,SLOT("quit()"))
      self.exec_()
if __name__ == "__main__" :
   app=Demo(sys.argv)