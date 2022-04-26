from pygame.locals import *
import pygame,sys
from random import randint

from pygame.time import delay

pygame.init()
VentanaX,VentanaY = 1500,1000
Porcentaje = 50
ColorFondo = pygame.Color(160,160,255)
Dir = "Derecha"
Velocidad = 10
PosX = int(VentanaX/2)-int((VentanaX*Porcentaje/100)/2)
PosY = int(VentanaY/2)-int((VentanaY*Porcentaje/100)/2)
ventana = pygame.display.set_mode((VentanaX,VentanaY))
pygame.display.set_caption("Hola, mundo!")
Mi_imagen = pygame.image.load("Ejemplo1/ovni.png")
Mi_imagen = pygame.transform.scale(Mi_imagen,(int(VentanaX*Porcentaje/100),int(VentanaY*Porcentaje/100)))

def DibujaImagen():
    ventana.blit(Mi_imagen,(PosX,PosY))


while True:
    if Dir=="Derecha" and PosX<VentanaX-int((VentanaX*Porcentaje/100)):
        PosX+=Velocidad
    else:
        Dir="Izquierda"
    if Dir=="Izquierda" and PosX>0:
        PosX-=Velocidad
    else:
        Dir="Derecha"
    ventana.fill(ColorFondo)
    DibujaImagen()
    
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.display.update()