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
ventana = pygame.display.set_mode((VentanaX,VentanaY))
pygame.display.set_caption("Hola, mundo!")
Mi_imagen = pygame.image.load("Ejemplo1/ovni.png")
Mi_imagen = pygame.transform.scale(Mi_imagen,(int(VentanaX*Porcentaje/100),int(VentanaY*Porcentaje/100)))

def DibujaImagen():
    ventana.blit(Mi_imagen,(PosX,PosY))


while True:
    ventana.fill(ColorFondo)
    DibujaImagen()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == K_LEFT:
                PosX-=Velocidad
            if event.key == K_RIGHT:
                PosX+=Velocidad
            if event.key == K_UP:
                PosY-=Velocidad
            if event.key == K_DOWN:
                PosY+=Velocidad

    pygame.display.update()