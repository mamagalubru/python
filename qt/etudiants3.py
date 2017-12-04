#!/usr/bin/python
# -*- coding : utf-8 -*-
#
# qdialog.py
# Programme exemple pour la classe QDialog
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

class Demo(QApplication) :
   def __init__ (self,args) :
      QApplication.__init__(self, args)
      # dialogue de sélection de fichier
      s = QFileDialog.getOpenFileName(None, "Boite d'ouverture de fichier")
      # conversions nécessaires entre QString et le type str de python
      h = "<h1>Vous avez choisi le fichier</h1>\n<i>"
      h = h + s + "</i>"
      # message d'information sur le fichier sélectionné
      QMessageBox.information(None, "Fichier choisi", h)

if __name__ == "__main__" :
   x = Demo(sys.argv)