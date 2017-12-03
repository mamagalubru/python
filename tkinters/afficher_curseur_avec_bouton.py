#!/usr/bin/env python
# -*- coding: cp1252 -*-

from tkinter import *
from time import *

class ProgressBar(Canvas):
    def __init__(self, master = None, **kw):
        Canvas.__init__(self, master,**kw)
        self.largeur = float(self.config()["width"][-1])+2
        self.hauteur = float(self.config()["height"][-1])+2

        self.valeur = 0
        self.barre = self.create_rectangle(0,0, self.largeur*self.valeur/100.,self.hauteur, fill = "Light Blue")
        self.texte = self.create_text(self.largeur/2. ,self.hauteur/2., text = str(int(self.valeur))+" %")

    def set_value(self, valeur):
        if 0<valeur<=100:
            self.valeur = valeur
            self.coords(self.barre, 0,0, self.largeur*self.valeur/100.,self.hauteur)
            valeur = str(float(valeur))
            self.itemconfig(self.texte, text = str(valeur)[:str(valeur).index('.')+3]+" %")
        else:
            raise ValueError("0<valeur<=100")

def demo_bar():
    fen_bar = Toplevel(fen)
    fen_bar.grab_set()

    progress = ProgressBar(fen_bar, height = 25)
    progress.grid(row = 1, column = 1, sticky = W+E)

    for i in range(1,101):
        progress.set_value(i)
        fen_bar.update()
        sleep(0.1)

if __name__ == '__main__':
    fen = Tk()
    Label(fen, text = "Démo ProgressBar").grid(row = 1, column = 1, padx = 5, pady = 5)
    Button(fen, text = "GO", command = demo_bar).grid(row = 2, column = 1, padx = 5, pady = 5)
    fen.mainloop()

