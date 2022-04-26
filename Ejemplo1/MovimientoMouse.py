from random import randint
from pygame.locals import *
import pygame,sys

pygame.init()
VentanaX,VentanaY = 1500,700
Porcentaje = 20
ColorFondo = pygame.Color(255,255,255)
Dir = "Derecha"
Velocidad = 30
PosX = int(VentanaX/2)-int((VentanaX*Porcentaje/100)/2)
PosY = int(VentanaY/2)-int((VentanaY*Porcentaje/100)/2)
x1 = VentanaY-20
y1 = randint(40,VentanaX-40)
PosXA,PosYA = PosX,PosY
ventana = pygame.display.set_mode((VentanaX,VentanaY))
pygame.display.set_caption("Juguemos!")
Nave = pygame.image.load("Ejemplo1/ovni.png")
Nave = pygame.transform.scale(Nave,(int(VentanaX*Porcentaje*0.5/100),int(VentanaY*Porcentaje/100)))
Asteroid1 = pygame.image.load("Ejemplo1/3.png")
Asteroid1 = pygame.transform.scale(Asteroid1,(int(VentanaX*Porcentaje*0.3/100),int(VentanaY*Porcentaje*0.5/100)))


def DibujaNave():
    ventana.blit(Nave,(PosX,PosY))

def DibujaAsteroide1():
    ventana.blit(Asteroid1,(x1,y1))

while True:
    
    ventana.fill(ColorFondo)
    #DibujaNave()
    DibujaAsteroide1()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.K_DOWN:
            if event.key == K_LEFT:
                PosX-=Velocidad
            if event.key == K_RIGHT:
                PosX+=Velocidad
            if event.key == K_UP:
                PosY-=Velocidad
            if event.key == K_DOWN:
                PosY+=Velocidad
    PosX,PosY = pygame.mouse.get_pos()
    PosX-=int((VentanaX*Porcentaje/100)/2)
    PosY-=int((VentanaY*Porcentaje/100)/2)
    x1 -= 0.01
    if PosX!=PosXA and PosY!=PosXA:
        ColorFondo = pygame.Color(randint(0,150),randint(250,255),randint(0,150))
    PosXA,PosYA = PosX,PosY
    pygame.display.update()