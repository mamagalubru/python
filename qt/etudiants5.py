#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# qlabel.py
# Programme exemple pour la classe QLabel
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
class Demo(QApplication) :
   def __init__(self,args) :
      QApplication.__init__(self, args)
      # widget principal, il s'agit d'une fenˆetre de dialogue
      self.dialog = QDialog()
      self.dialog.setWindowTitle("Dialog")
      # premier élément textuel, nom de l'objet = ”text1”
      self.text1 = QLabel(self.dialog)
      # taille de l'objet et positionnement absolu
      self.text1.setGeometry(QRect(120,80,180,70))
      # le texte `a afficher
      self.text1.setText("Le texte \ntient sur \nplusieurs lignes !")
      # mise en page : très facile !
      self.text2 = QLabel(self.dialog)
      self.text2.setText("<h1><font color='red'>Et la mise en page<br>"+ " est possible</font></h1>")
      self.text2.setGeometry(QRect(120,220,250,100))
      self.connect(self,SIGNAL("lastWindowClosed()"),self,SLOT("quit()"))
      self.dialog.show()
      self.exec_()
if __name__ == "__main__" :
   x = Demo(sys.argv)