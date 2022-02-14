#!/usr/bin/env python
# coding: utf-8

# # QUESTION 1

# In[1]:


from tkinter import *
import tkinter.font as tkFont
import random

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
    # vérifie l'évolution des cellules true or false
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
    # compte le nombre de cellules voisines
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


def play():
    # change la couleur des cellules en fonction de leur prochain état
    # définit l'arrêt du jeu et le message de fin...
    isNext = nextEvolution()
    for y in range(height):
        for x in range(width):
            if nextCells[y][x] == 1:
                couleur = "red"
            else:
                couleur = "white"
            canvas.itemconfig(grid[y][x], fill=couleur)
            currentCells[y][x] = nextCells[y][x]
    #print(currentCells,nextCells)
    
    if isNext:
        window.after(100, play)
    else:
        canvas.create_text(height*side/2, width*side/2,
                           text="C'est Fini, 1ere question done ! ", justify="center", width=width*side, font=tkFont.Font(family="Helvetica", size=26), fill="red")


height = 18
width = 18
wrap = 0  #wrap ou non 
startCells = []

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
window.title(" <3  Jeu de la Vie *__* <3")
window.geometry("300x320")
window.config(background = "orange")

canvas = Canvas(window, width=side*width, height=side*height)

evoluer=Button(window,text=" Quiter !", font = ('courier' , 10) ,command=window.destroy,background = "red" , relief = RAISED)  
   
evoluer.place(x=width//2-60,y=height+10) # choisit positionnement bouton
evoluer.pack()
canvas.pack()


def main():
    dessin()
    window.after(500, play)


if __name__ == '__main__':
    main()


# In[2]:


window.mainloop()


# In[ ]:




