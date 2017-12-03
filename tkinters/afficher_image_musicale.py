import winsound
from tkinter import *


'''
Ce fichier définit un essai de fenêtre sous TK 
Le programme va afficher une image dans une fenêtre Tkinter
Puis jouer un son ou une musique sous windows
'''

# créer une fenêtre
tk = Tk()

# créer un canevas
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
# charger une image
mon_image = PhotoImage(file='C:\\Python34\\tests\\images\\guitare.gif')
# afficher l'image
canvas.create_image(0, 0, anchor = NW, image = mon_image)
# afficher le texte
canvas.create_text(300, 100, text = 'image de musique')
# jouer une musique sous windows
winsound.PlaySound('C:\\Python34\\tests\\musiques\\guitare.wav',winsound.SND_FILENAME)

tk.mainloop()
