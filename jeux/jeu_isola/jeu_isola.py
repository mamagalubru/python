from tkinter import *
from random import randrange

#            * Règles du jeu *  
#    A chaque tour de jeu, vous déplacez le pion bleu
#    d'une case dans une des huit directions, puis
#    vous bloquez une case autour du pion adverse.
#    Votre adversaire (l'ordinateur) procède de même.
#    Le jeu se termine quand l'un des deux joueurs
#    est bloqué.
#    Pour déplacer votre pion, cliquez avec le bouton
#    gauche dans la case de destination.
#    Pour bloquer une case, cliquez dessus avec le 
#    bouton droit.

def carre(x,y,col):
    can.create_rectangle(x,y,x+50,y+50, fill=col, outline='black')

def bloc(x,y):
    can.create_rectangle(x+4,y+4,x+45,y+45, fill="red", outline='black')

def case_jouable():
    "recherche de la meilleure case jouable par l'ordi"
    # on note les huits cases qui entourent le pion, puis pour chaque
    # case libre on recommence l'opération et ce sur quatre niveaux.
    global bx,by
    rc = [0,0,0,0,0,0,0,0]
    for n1 in range(0,8):
        x1,y1 = bx + kx[n1], by + ky[n1]
        if jeu[y1][x1] == 0:
            rc[n1] += 1
            for n2 in range(0,8):
                x2,y2 = x1 + kx[n2], y1 + ky[n2]
                if jeu[y2][x2] == 0:
                    rc[n1] += 2
                    for n3 in range(0,8):
                        x3,y3 = x2 + kx[n3], y2 + ky[n3]            
                        if jeu[y3][x3] == 0:
                            rc[n1] += 3                             
                            for n4 in range(0,8):
                                x4,y4 = x3 + kx[n4], y3 + ky[n4]
                                if x4 in range(7) and y4 in range(9):
                                    if jeu[y4][x4] == 0:
                                        rc[n1] += 4
                                        
    rs,ts = -1,0
    for i in range(8):
        if rc[i] > ts:
            rs = i
            ts = rc[i]
    return rs        

def case_bloque():
    "recherche de la meilleure case à bloquer par l'ordi"
    # identique à la case jouable, mais sur 3 niveau seulement,
    # à partir du pion du joueur.
    global px,py,jeu
    rc = [0,0,0,0,0,0,0,0]
    for n1 in range(0,8):
        x1,y1 = px + kx[n1], py + ky[n1]
        if jeu[y1][x1] == 0:
            rc[n1] += 1
            for n2 in range(0,8):
                x2,y2 = x1 + kx[n2], y1 + ky[n2]
                if jeu[y2][x2] == 0:
                    rc[n1] += 2
                    for n3 in range(0,8):
                        x3,y3 = x2 + kx[n3], 2 + ky[n3]
                        if jeu[y3][x3] == 0:
                            rc[n1] += 3
    rs,ts = -1,0
    for i in range(0,8):
        if rc[i] > ts:
            rs = i
            ts = rc[i]
    return rs        
                
def pion_orange(y,x):
    "déplace le pion orange"
    global bx,by,jeu
    ax, ay = x, y
    x1, y1 = (x-1) * 50+3, (y-1)*50+3
    if jeu[ay][ax] == 0:
        jeu[by][bx] = 0
        jeu[ay][ax] = 2
        can.coords(poran, x1,y1, x1+44,y1+44)  # l'affiche à la nouvelle position
        bx, by = ax, ay                        # et stocke son adresse
      
def bloc_rouge(y,x):
    "dessiner un carré rouge sur le damier"
    global px,py,jeu
    ax,ay = x,y
    if jeu[ay][ax] == 0:  
        bloc((ax-1)*50,(ay-1)*50)
        jeu[ay][ax] = 9
              
def ordi_joue():
    global bx,by,px,py,jeu,fin,flag
    pmes.configure(text = ' Je réfléchis... ')
    nc = case_jouable()
    if nc < 0:
        fin = 1
        fin_jeu()
    else:    
        pion_orange(by+ky[nc],bx+kx[nc])   
        nc = case_bloque()
        if nc < 0:
            fin = 1
            fin_jeu()
        else:    
            bloc_rouge(py+ky[nc],px+kx[nc])
            flag = 0
            pmes.configure(text = ' A vous de jouer ')

def pion_bleu(x,y):
    "déplace le pion bleu"
    global bx,by,px,py,jeu
    ax, ay = x, y
    x1, y1 = (x-1) * 50+3, (y-1)*50+3
    if abs(ax-px) <= 1 and abs(ay-py) <= 1 and jeu[ay][ax] == 0:
        jeu[py][px] = 0
        jeu[ay][ax] = 1
        can.coords(pbleu, x1,y1, x1+44,y1+44)   # l'affiche à la nouvelle position
        px, py = ax, ay                 # et stocke son adresse
        pmes.configure(text = ' Bloquez une case ')
      
def blocage(x,y):
    "dessiner un carré rouge sur le damier"
    global bx,by,jeu
    ax, ay = x, y
    if abs(ax-bx)<=1 and abs(ay-by)<=1 and jeu[ay][ax] == 0:  
        bloc((ax-1)*50,(ay-1)*50)
        jeu[ay][ax] = 9
        
def point_pion(event):                          # clic gauche
    global flag
    x,y = event.x // 50 + 1, event.y // 50 + 1
    if flag == 0:
      pion_bleu(x,y)
      flag = 1

def point_bloc(event):                          # clic droit
    global flag
    x,y = event.x // 50 + 1, event.y // 50 + 1
    if flag == 1:
      blocage(x,y)
      flag = 2
      ordi_joue()

def fin_jeu():
    global fin
    if fin == 1:
        pmes.configure(text = ' Bravo! Vous avez gagné!!! ')
    else:    
        pmes.configure(text = " Youpi! J'ai gagné la partie! ")
        
def debut_jeu():
    "commence une partie"  
    for i in range(8):      # remplissage des bords pour simplifier les tests
        jeu[0][i] = 9
        jeu[9][i] = 9
    for i in range(10):
        jeu[i][0] = 9
        jeu[i][7] = 9
    if jr == 2:
        ordi_joue()
    else:
        flag = 0
        pmes.configure(text = ' A vous de jouer ')
   
#---------------------------------------------------------------------------------          
fen = Tk()
fen.title('ISOLA')
fen.configure(background = "green")
can = Canvas(fen, width =300, height =400, bg ='white')
can.pack(side =TOP, padx =5, pady =5)
can.bind("<Button-1>", point_pion)
can.bind("<Button-3>", point_bloc)
pmes = Label(fen,text=' Un petit clic sur Jouer ',font ="Arial 12", bg ="#C0C0F0")
pmes.pack()
b1 = Button(fen, text ='  Jouer  ', command =debut_jeu, font ="Arial 12")
b1.pack(side =LEFT, padx =3, pady =3)
b2 = Button(fen, text =' Abandonner ', command =fin_jeu, font ="Arial 12")
b2.pack(side =RIGHT, padx =3, pady =3)

jeu = [[0]*8 for lig in range(10)]
px,py = 3,8
bx,by = 4,1
jr = randrange(2)+1
kx = [0,  1,1,1,0,-1,-1,-1]
ky = [-1,-1,0,1,1, 1, 0,-1]
for y in range(8):
    for x in range(6): 
        carre(x*50,y*50,'#008000')  
pbleu = can.create_oval(103, 353, 146, 396, fill="blue", outline='black')
poran = can.create_oval(153, 3, 196, 46, fill="orange", outline='black') 
jeu[1][4] = 2
jeu[8][3] = 1
fin, flag = 0,0
    
fen.mainloop()    
