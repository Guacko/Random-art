# IMPORTATION DES MODULES NECESSAIRES (ne touche pas trop à ça à moins que tu veuille rajouter des trucs mais je pense pas)
import pygame
import random
import math


# VARIABLES (LES VALEURS DE DEPART MODIFIABLES OU JUSTE UTILISABLES PLUS BAS) 
# (dans une égalité c'est la variable de gauche qui prend la valeur de celle de droite pas l'inverse donc par exemple si x = 20 et y = 40 et qu'on fait x = y après les deux valent 40)
screenWidth = 1920
screenHeight = 1080
centerx = screenWidth/2 
centery = screenHeight/2
displaySurface = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption("Jeu Python")
clock = pygame.time.Clock()
run = True
fps = 40
red = [255,0,0]
green = [0,255,0]
blue = [0,0,255]
white = [255,255,255]
black = [0,0,0]


# on defini ce que va faire la fonction "redrawGameWindow()" (ce code ne s'execute que quand on l'appelle ici ça n'est que la définition, le code qu'on execute en général est dans le while plus bas ou juste au dessus)
def redrawGameWindow():

    #displaySurface.fill(black)  # remplit le background de la couleur choisie (permet aussi d'effacer en quelque sorte l'écran)
    cell1.drawCell() # on dessine chaque objet créé à partir de la classe "cell" 
    cell2.drawCell()
    cell3.drawCell()
    cell4.drawCell()
    cell5.drawCell()
    cell6.drawCell()
    cell7.drawCell()
    cell8.drawCell()
    cell9.drawCell()
    cell10.drawCell()
    cell20.drawCell()
    cell30.drawCell()
    cell40.drawCell()
    cell50.drawCell()
    cell60.drawCell()
    cell70.drawCell()
    cell80.drawCell()
    cell90.drawCell()
    cell11.drawCell()
    cell21.drawCell()
    cell31.drawCell()
    cell41.drawCell()
    cell51.drawCell()
    cell61.drawCell()
    cell71.drawCell()
    cell81.drawCell()
    cell91.drawCell()
    cell100.drawCell()
    cell200.drawCell()
    cell300.drawCell()
    cell400.drawCell()
    cell500.drawCell()
    cell600.drawCell()
    cell700.drawCell()
    cell800.drawCell()
    cell900.drawCell()
    cell1000.drawCell()
    cell2000.drawCell()
    cell3000.drawCell()
    cell4000.drawCell()
    cell5000.drawCell()
    cell6000.drawCell()
    cell7000.drawCell()
    cell8000.drawCell()
    cell9000.drawCell()
    cell1001.drawCell()
    cell2001.drawCell()
    cell3001.drawCell()
    cell4001.drawCell()
    cell5001.drawCell()
    cell6001.drawCell()
    cell7001.drawCell()
    cell8001.drawCell()
    cell9001.drawCell()

    cell1000.drawCell()
    cell2000.drawCell()
    cell3000.drawCell()
    cell4000.drawCell()
    cell5000.drawCell()
    cell6000.drawCell()
    cell7000.drawCell()
    cell8000.drawCell()
    cell9000.drawCell()
    cell10000.drawCell()
    cell20000.drawCell()
    cell30000.drawCell()
    cell40000.drawCell()
    cell50000.drawCell()
    cell60000.drawCell()
    cell70000.drawCell()
    cell80000.drawCell()
    cell90000.drawCell()
    cell10001.drawCell()
    cell20001.drawCell()
    cell30001.drawCell()
    cell40001.drawCell()
    cell50001.drawCell()
    cell60001.drawCell()
    cell70001.drawCell()
    cell80001.drawCell()
    cell90001.drawCell()
    cell100000.drawCell()
    cell200000.drawCell()
    cell300000.drawCell()
    cell400000.drawCell()
    cell500000.drawCell()
    cell600000.drawCell()
    cell700000.drawCell()
    cell800000.drawCell()
    cell900000.drawCell()
    cell1000000.drawCell()
    cell2000000.drawCell()
    cell3000000.drawCell()
    cell4000000.drawCell()
    cell5000000.drawCell()
    cell6000000.drawCell()
    cell7000000.drawCell()
    cell8000000.drawCell()
    cell9000000.drawCell()
    cell1000001.drawCell()
    cell2000001.drawCell()
    cell3000001.drawCell()
    cell4000001.drawCell()
    cell5000001.drawCell()
    cell6000001.drawCell()
    cell7000001.drawCell()
    cell8000001.drawCell()
    cell9000001.drawCell()
    pygame.display.update()

class cell: # on définit une classe "cell" avec ces attributs (paramètres) et définitions (les actions dont est capable l'objet) (les classes sont des sortes de templates que tu fait pour créer plein d'objets similaires)
    def __init__(self): # ici dessous on retrouve tous les attributs (jusqu'a la ligne self.speedy)
        self.color = [random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)]
        self.size = random.randrange(1,2)
        self.rage = random.randrange(0,10)
        self.libido = random.randrange(0,10)
        self.x = round(centerx + random.randrange(2000,25000))
        #self.y = round(centery) j'ai rajouter random.randrange pour viré le trais avec tt les points
        self.y = round(centery + random.randrange(2000,25000))
        self.speedx = random.randrange(-2,3)
        self.speedy = random.randrange(-2,3)

    def drawCell(self): # ici c'est la première et unique action que fait une cellule actuellement (on pourrait en rajouter d'autres) (jusqu'a self.size = 1)
        pygame.draw.circle(displaySurface,self.color,(self.x,self.y),self.size)
        # if random.randrange(0,100) < 100:
        #     self.speedy = random.randrange(0,self.size*4)
        #     self.speedx = random.randrange(-6,7)
        self.x -= round((-(centery - self.y)/10) + ((self.x - centerx)/100))
        self.y -= round(((centerx - self.x)/10) + ((self.y - centery)/100))
        if self.x>screenWidth:
            self.x=random.randrange(0,screenWidth)
        if self.y>screenWidth:
            self.y=random.randrange(0,screenWidth)
            if self.size<=10:
                self.size += 1
            else:
                self.size = 1
        
# ici c'est le "début" du code réel ont commence par créer plein d'objet celln é partir de la classe (template) décrite plus haut
cell1 = cell()
cell2 = cell()
cell3 = cell()
cell4 = cell()
cell5 = cell()
cell6 = cell()
cell7 = cell()
cell8 = cell()
cell9 = cell()
cell10 = cell()
cell20 = cell()
cell30 = cell()
cell40 = cell()
cell50 = cell()
cell60 = cell()
cell70 = cell()
cell80 = cell()
cell90 = cell()
cell11 = cell()
cell21 = cell()
cell31 = cell()
cell41 = cell()
cell51 = cell()
cell61 = cell()
cell71 = cell()
cell81 = cell()
cell91 = cell()
cell100 = cell()
cell200 = cell()
cell300 = cell()
cell400 = cell()
cell500 = cell()
cell600 = cell()
cell700 = cell()
cell800 = cell()
cell900 = cell()
cell1000 = cell()
cell2000 = cell()
cell3000 = cell()
cell4000 = cell()
cell5000 = cell()
cell6000 = cell()
cell7000 = cell()
cell8000 = cell()
cell9000 = cell()
cell1001 = cell()
cell2001 = cell()
cell3001 = cell()
cell4001 = cell()
cell5001 = cell()
cell6001 = cell()
cell7001 = cell()
cell8001 = cell()
cell9001 = cell()

cell1000 = cell()
cell2000 = cell()
cell3000 = cell()
cell4000 = cell()
cell5000 = cell()
cell6000 = cell()
cell7000 = cell()
cell8000 = cell()
cell9000 = cell()
cell10000 = cell()
cell20000 = cell()
cell30000 = cell()
cell40000 = cell()
cell50000 = cell()
cell60000 = cell()
cell70000 = cell()
cell80000 = cell()
cell90000 = cell()
cell10001 = cell()
cell20001 = cell()
cell30001 = cell()
cell40001 = cell()
cell50001 = cell()
cell60001 = cell()
cell70001 = cell()
cell80001 = cell()
cell90001 = cell()
cell100000 = cell()
cell200000 = cell()
cell300000 = cell()
cell400000 = cell()
cell500000 = cell()
cell600000 = cell()
cell700000 = cell()
cell800000 = cell()
cell900000 = cell()
cell1000000 = cell()
cell2000000 = cell()
cell3000000 = cell()
cell4000000 = cell()
cell5000000 = cell()
cell6000000 = cell()
cell7000000 = cell()
cell8000000 = cell()
cell9000000 = cell()
cell1000001 = cell()
cell2000001 = cell()
cell3000001 = cell()
cell4000001 = cell()
cell5000001 = cell()
cell6000001 = cell()
cell7000001 = cell()
cell8000001 = cell()
cell9000001 = cell()
# ici on à le programme qui va tourner indéfiniement dans le while jusqu'a ce que quelqu'un ferme la fenêtre ce qui fait prendre à la variable run la valeur 0 ou faux (1 étant vrai mais pour les conditions dans python on utilise "True" et "False")
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    redrawGameWindow() # la seule action que j'ai rajouté dans la boucle "infinie", ça appelle la fonction "redrawGameWindow()" et effectue tout ce qui y est déclaré
    clock.tick(fps)

pygame.quit() # run devient faux alors on quite la boucle infinie et on arrive ici (ça quitte tout cette fonction)




# Aide: 
# quand tu met ta souris à gauche du code ta des petites flèches pour ouvrir en détail ou fermer le trop de détail de déclarations diverses
# tu peut faire clic droit sur une variable, fonction, classe et voir comment elle est définie avec "go to definition"
# une classe "class quelqueChose()" c'est comme une template de variable qui aurait plein de paramètre et de fonctions définies
# une definition "def quelqueChose()" c'est une fonction (un bout de code) qui peut être exécuté à chaque fois qu'on appelle le titre (quelqueChose() , effectuera tout le code se trouvant sous la déclaration de cette définition)