# IMPORTATION DES MODULES NECESSAIRES (ne touche pas trop à ça à moins que tu veuille rajouter des trucs mais je pense pas)
import pygame
import random
import math


# VARIABLES (LES VALEURS DE DEPART MODIFIABLES OU JUSTE UTILISABLES PLUS BAS) 
# (dans une égalité c'est la variable de gauche qui prend la valeur de celle de droite pas l'inverse donc par exemple si x = 20 et y = 40 et qu'on fait x = y après les deux valent 40)
screenWidth = 1500
screenHeight = 900
centerx = screenWidth//2 
centery = screenHeight//2
displaySurface = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption("Jeu Python")
clock = pygame.time.Clock()
run = True
fps = 60
red = [255,0,0]
green = [0,255,0]
blue = [0,0,255]
white = [255,255,255]
black = [0,0,0]
counter = 0
numberOfCells =0
numberOfCellsMax = 200
cellList = []


class cell: # on définit une classe "cell" avec ces attributs (paramètres) et définitions (les actions dont est capable l'objet) (les classes sont des sortes de templates que tu fait pour créer plein d'objets similaires)
    def __init__(self): # ici dessous on retrouve tous les attributs (jusqu'a la ligne self.speedy)
        self.color = [random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)]
        self.size = random.randrange(1,5)

        self.x = round(centerx + random.randrange(-screenWidth//3,screenWidth//3))
        self.y = round(centery + random.randrange(-screenHeight//3, screenHeight//3)) #j'ai rajouter random.randrange pour viré le trais avec tt les points
        #self.y = round(centery + random.randrange(-screenHeight/2,screenHeight/2))
        self.speedx = 1
        self.speedy = 1
        self.counter = 0

    def drawCell(self): # ici c'est la première et unique action que fait une cellule actuellement (on pourrait en rajouter d'autres) (jusqu'a self.size = 1)
        pygame.draw.circle(displaySurface,self.color,(self.x,self.y),self.size)

    def moveCell(self):
        if random.randrange(0,100) < 100:
            self.speedy = random.randrange(0,self.size*40)
            self.speedx = random.randrange(-6,7)
        self.x += round((-(centery - self.y)/random.randrange(100,500)) - ((self.x - centerx)/random.randrange(100,1000)))
        self.y += round(((centerx - self.x)/random.randrange(100,500)) - ((self.y - centery)/random.randrange(100,1000)))
        
        if self.x>screenWidth:
            self.x=random.randrange(0,screenWidth)

        if self.y>screenWidth:
            self.y=random.randrange(0,screenWidth)
            if self.size<=10:
                self.size += 1
            else:
                self.size = 1

# on defini ce que va faire la fonction "redrawGameWindow()" (ce code ne s'execute que quand on l'appelle ici ça n'est que la définition, le code qu'on execute en général est dans le while plus bas ou juste au dessus)
def redrawGameWindow():
    #displaySurface.fill(black)
    for cells in cellList:
        cells.drawCell()
        pass
    pygame.display.update()

def updateWindow():
    for cells in cellList:
        cells.moveCell()

def InitialCreation():
    global numberOfCells
    while numberOfCells < numberOfCellsMax:
        numberOfCells += 1
        cellList.append(cell())

InitialCreation()

# ici c'est le "début" du code réel ont commence par créer plein d'objet celln é partir de la classe (template) décrite plus haut
# ici on à le programme qui va tourner indéfiniement dans le while jusqu'a ce que quelqu'un ferme la fenêtre ce qui fait prendre à la variable run la valeur 0 ou faux (1 étant vrai mais pour les conditions dans python on utilise "True" et "False")
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    updateWindow()
    redrawGameWindow() # la seule action que j'ai rajouté dans la boucle "infinie", ça appelle la fonction "redrawGameWindow()" et effectue tout ce qui y est déclaré
    clock.tick(fps)

pygame.quit() # run devient faux alors on quite la boucle infinie et on arrive ici (ça quitte tout cette fonction)

# Aide: 
# quand tu met ta souris à gauche du code ta des petites flèches pour ouvrir en détail ou fermer le trop de détail de déclarations diverses
# tu peut faire clic droit sur une variable, fonction, classe et voir comment elle est définie avec "go to definition"
# une classe "class quelqueChose()" c'est comme une template de variable qui aurait plein de paramètre et de fonctions définies
# une definition "def quelqueChose()" c'est une fonction (un bout de code) qui peut être exécuté à chaque fois qu'on appelle le titre (quelqueChose() , effectuera tout le code se trouvant sous la déclaration de cette définition)