from pygame.locals import *
import pygame,sys
from random import randint

from pygame.time import delay

pygame.init()
VentanaX,VentanaY = 500,300
Porcentaje = 10
ventana = pygame.display.set_mode((VentanaX,VentanaY))
pygame.display.set_caption("Hola, mundo!")
Mi_imagen = pygame.image.load("Ejemplo1/Yo - Perfil.jpeg")
Mi_imagen = pygame.transform.scale(Mi_imagen,(int(VentanaX*Porcentaje/100),int(VentanaY*Porcentaje/100)))

def DibujaImagen():
    PosX = randint(0,VentanaX-int(VentanaX*Porcentaje/100))
    PosY = randint(0,VentanaY-int(VentanaY*Porcentaje/100))

    ventana.blit(Mi_imagen,(PosX,PosY))

while True:
    ventana.fill((pygame.Color(0,0,0)))
    DibujaImagen()
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.display.update()