import pygame,sys
from pygame.locals import *
import pygame,sys


pygame.init()
ventana = pygame.display.set_mode((400,300))
pygame.display.set_caption("Hola, mundo!")
X = 60
Y = 80
ColorFondo = pygame.Color(70,80,150)
ColorLinea = pygame.Color(255,0,0)
ColorCirculo = pygame.Color(120,255,180)
ColorRectangulo = pygame.Color(255,255,255)
ColorPoligono = pygame.Color(220,180,180)
ventana.fill(ColorFondo)
pygame.draw.line(ventana,ColorLinea,(X,Y),(160,100),3)
pygame.draw.circle(ventana,ColorCirculo,(X+200,Y+100),50)
pygame.draw.rect(ventana,ColorRectangulo,(X+50,Y+100,100,40))
pygame.draw.polygon(ventana,ColorPoligono,((0,0),(3,2),(120,0),(60,90),(180,75)))

while True:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()