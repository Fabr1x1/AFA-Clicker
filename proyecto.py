#Constantes
size= (800,800)
FPS= 30

#Creamos la clase Items 
class Item:
    def __init__(self, rect, text,base_AFA, base_cps_each):
    self.rect = rect
    self.text = text
    self.count = 0
    self.base_AFA = base_AFA
    self.cps_each = base_cps_each


#Definimos los CPS
    def total_cps(self):
        return self.cps_each * self.count

#Definimos la economía 
    def AFA(self):
        return self.base_AFA * 1.15**self.count

    def click(self):
        AFA = self.AFA()
        global indefinido
        if indefinido >= AFA:
            self.count += 1
            indefinido -= AFA

    def collidepoint(self, point):
        return self.rect.collidepoint(point)

#Importamos los módulos
import sys
import pygame
from pygame.locals import*

pygame.init()

fpsClock = pygame.time.Clock()
#Generamos dimensiones de la pantalla
screen = pygame.display.set_mode(size)

#Creamos nombre para la pantalla
pygame.display.set_caption("AFA Clicker")

BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)

BUTTON_BG_COLOR = pygame.Color(68, 93, 255)
BUTTON_BORDER_COLOR = pygame.Color(85, 50, 232)

FONT = pygame.font.SysFont("sysfont", 24)
#imagen personaje 1
Character1 = pygame.image.load("")

AFA = 0
CPS = 0.0


for event in pygame.event.get():
    if event.type == QUIT:
        pygame.quit()
        sys.exit()