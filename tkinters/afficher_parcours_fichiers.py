# -*- coding: cp1252 -*-
from tkinter import *
from os import getcwd
from tkinter.filedialog import askdirectory

class Parcourir(Frame):
    def __init__(self, master = None, command = None, **kw):
        Frame.__init__(self, master, **kw)

        self.chemin = StringVar()
        self.chemin.set(getcwd())
        
        self.command = command

        self.entree_chemin = Entry(self, text = self.chemin, width = 70)
        self.entree_chemin.grid(row = 1, column = 1, padx = 5, pady = 5)

        self.bouton = Button(self, text = "Parcourir", command = self.parcours)
        self.bouton.grid(row = 1, column = 2, padx = 5, pady = 5)

    def parcours(self):
        chemin = askdirectory()
        if chemin != '':
            self.chemin.set(chemin)
            if self.command != None:
                self.command()

    def get(self):
        return str(self.chemin.get())

def demo_parcours():
    global label_parcours, parcours
    
    fen_parcours = Toplevel(fen)
    fen_parcours.grab_set()

    label_parcours = Label(fen_parcours)
    label_parcours.grid(row = 0, column = 1)

    parcours = Parcourir(fen_parcours, command = modify_label, border = 2, relief = RAISED)
    parcours.grid(row = 1, column = 1)
    modify_label()

def modify_label():
    label_parcours.config(text = parcours.get())

if __name__ == '__main__':
    fen = Tk()
    Label(fen, text = "Démo Parcours").grid(row = 1, column = 1, padx = 5, pady = 5)
    Button(fen, text = "GO", command = demo_parcours).grid(row = 2, column = 1, padx = 5, pady = 5)
    fen.mainloop()

