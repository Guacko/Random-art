import pygame
import random
import math

screenWidth = 800
screenHeight = 800
centerx = screenWidth//2
centery = screenHeight//2
displaySurface = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption("Shore")
clock = pygame.time.Clock()
run = True
fps = 27
red = [255,0,0]
green = [0,255,0]
blue = [0,0,255]
white = [255,255,255]
black = [0,0,0]
counter = 0
seconde = 0

class dot (object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.size = 5
        self.color = [random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)]
    def draw(self):
        pygame.draw.circle(displaySurface,[random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)],(self.x,self.y),self.size) 
    def drawrectangle(self):
        self.x += round(math.cos(seconde)) 
        self.y += round(math.sin(seconde)) 
        

def redrawGameWindow():
    frite.draw()
    pygame.display.update()

frite = dot(centerx,centery)

while run:
    for event in pygame.event.get():
                 if event.type == pygame.QUIT:
                    run = False
    if counter >= fps:
        seconde += 1
        counter = 0
    else:
        counter += 1
    frite.drawrectangle()
    redrawGameWindow()
    clock.tick(fps)
pygame.quit()