import pygame
import random

screenWidth = 1400
screenHeight = 700
displaySurface = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption("Jeu Python")
clock = pygame.time.Clock()
run = True
fps = 270
red = [255,0,0]
green = [0,255,0]
blue = [0,0,255]
white = [255,255,255]
black = [0,0,0]
dotList = []
numberOfDots = random.randrange(0,200)

class dot (object):
    def __init__(self):
        self.x = random.randrange(0,screenWidth)
        self.y = random.randrange(0,screenHeight)
        self.color = [random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)]
        self.height = random.randrange(1,10)
    def draw (self):
        pygame.draw.circle(displaySurface,self.color,(self.x,self.y),self.height)      

i=0
while i < numberOfDots:
    i += 1
    dotList.append(dot())

def redrawGameWindow():
    for dots in dotList:
        dots.draw()
    pygame.display.update()

while run:
    for event in pygame.event.get():
                 if event.type == pygame.QUIT:
                    run = False
    for dots in dotList:
        dots.x += random.randrange(-3,4)
        dots.y += random.randrange(-3,4)    
    redrawGameWindow()
    clock.tick(fps)
pygame.quit()