#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
import tkinter.font as tkFont
import random
import threading
import numpy as np


# In[2]:


def dessin():
    # dessin de la config de départ sur la matrice
    for y in range(height):
        for x in range(width):
            grid[y][x] = canvas.create_rectangle(
                x*side, y*side, (x+1)*side, (y+1)*side, outline="gray", fill="white")
    for cell in startCells:
        canvas.itemconfig(grid[cell[1]][cell[0]], fill="black")
        currentCells[cell[1]][cell[0]] = 1


def nextEvolution():
    # vérifie l'évolution des cellules
    countChangeCells = 0
    for y in range(height):
        for x in range(width):
            currentState = currentCells[y][x]
            countNeighbors = whoIsAround(x, y, wrap)
            isAlive = False if currentState == 0 else True
            nextState = isCellAlive(countNeighbors, isAlive)
            nextCells[y][x] = nextState
            if currentState != nextState:
                countChangeCells += 1
    return countChangeCells > 0


def whoIsAround(x, y, wrap):
    # compte le nombre de cellueles voisines
    countNeighbors = 0
    for i in range(y-1, y+2):
        for j in range(x-1, x+2):
            if not (i == y and j == x):
                if wrap == 0 and height > i >= 0 and width > j >= 0 and currentCells[i][j] == 1:
                    countNeighbors += 1
                if wrap == 1:
                    wrapX = j
                    wrapY = i
                    if i < 0:
                        wrapY = height - 1
                    if i >= height:
                        wrapY = 0
                    if j < 0:
                        wrapX = width - 1
                    if j >= width:
                        wrapX = 0
                    if currentCells[wrapY][wrapX] == 1:
                        countNeighbors += 1
    return countNeighbors


def isCellAlive(countNeighbors, isAlive):
    # les règles du jeu : la cellule va-t-elle s'éteindre ou non ?
    if isAlive:
        if countNeighbors == 2 or countNeighbors == 3:  
            return True
        else:
            return False
    else:
        if countNeighbors == 3:  # exactement 3
            return True
        else:
            return False


def life2(y,x,B,env):
    # change la couleur des cellules en fonction de leur prochain état
    # définit l'arrêt du jeu et le message de fin...
    isNext = nextEvolution()
    
    if nextCells[y][x] == 1:
        couleur = "black"
    else:
        couleur = "white"
    canvas.itemconfig(grid[y][x], fill=couleur)
    currentCells[y][x] = nextCells[y][x]
    if not isNext:
        B.wait(env)
        canvas.create_text(height*side/2, width*side/2,
                           text="C'est Fini Lydia à reussi son mini projet", justify="center", width=width*side, font=tkFont.Font(family="Helvetica", size=26), fill="red")

        
 


# In[3]:


n=18
class Barriere:
    def __init__(self,n_max):
        self.n_max = n_max
        self.cond = threading.Condition()
        
        self.count = n_max
        self.sense = True
        
    def wait(self,env):
        global fen
        with self.cond:
            env.local_sense = not env.local_sense
            self.count -=1
            if self.count == 0:
                self.count = self.n_max
                self.sense = env.local_sense
                self.cond.notify_all()
            else:
                self.cond.wait_for(lambda:self.sense == env.local_sense)
B = Barriere(n*n)
class  Thread_lydia(threading.Thread):
    def  __init__(self ,i,j):
        threading.Thread.__init__(self)
        self.i= i 
        self.j = j 
    
    def run (self) : 
        env = threading.local()
        env.local_sense = True
        global currentCells
        global wrap
        while True :
            nb_voisin =whoIsAround(self.i , self.j,wrap) ## compte le nombre de cellules voisines
            #print(nb_voisin)
            B.wait(env)
            if (currentCells[self.i][self.j]==1) :
                    if (nb_voisin!= 2  and  nb_voisin !=3  )  :
                        currentCells[self.i][self.j] = 0
            if (currentCells[self.i][self.j] == 0 and nb_voisin==3 ) :
                currentCells[self.i][self.j] = 1
                
            life2(self.i,self.j,B,env)
               
            B.wait(env)
          #  print(currentCells)
#
def thraed () : 
    thread = []
    for i in range (0,width) :
        l_thread = []
        for j in range(0,width) : 
            l_thread.append(Thread_lydia(i,j))
        thread.append(l_thread)
    thread = np.array(thread)    
    ## Start les thread 
    print(np.shape(thread))
    for i in range(0,width) : 
        for j in range(0,width) : 
            thread[i][j].start()
            


# In[ ]:





# In[4]:


##########test
height = 18  # matrice carré
width = 18
wrap = 0
startCells = []
B = Barriere(18*18)
# largeur d'une cellule (en px)
side = 15
# matrice des cellules à l'instant T0
currentCells = [[random.choice([0, 1])
                       for j in range(width)]
                      for i in range(height)] 
# matrice des cellules à l'instant T1
nextCells = [[0 for row in range(height)] for col in range(width)]
# matrice de la grille générale
grid = [[0 for row in range(height)] for col in range(width)]

# création de la matrice de jeu
window = Tk()
window.title("<3  Jeu de la Vie *__* <3")
window.geometry("320x320")
window.config(background = "blue")

canvas = Canvas(window, width=side*width, height=side*height)

evoluer=Button(window,text=" Quiter !", font = ('courier' , 10) ,command= lambda :window.destroy,background = "red" , relief = RAISED)  

evoluer.place(x=270//2-60,y=270+10) # choisit positionnement bouton
evoluer.pack()
canvas.pack()


# In[5]:


def main():
    dessin()
    window.after(1000,thraed)    
 


# In[ ]:


main()
window.mainloop()


# In[ ]:




