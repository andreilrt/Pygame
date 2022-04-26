from pygame.locals import *
import pygame,sys


from pygame.time import delay

pygame.init()
VentanaX,VentanaY = 1500,1000
RectX,RectY = 1,1
Porcentaje = 30
ColorFondo = pygame.Color(160,160,255)
Dir = "Derecha"
Velocidad = 1
PosX = int(VentanaX/2)-int((VentanaX*Porcentaje/100)/2)
PosY = int(VentanaY/2)-int((VentanaY*Porcentaje/100)/2)
ventana = pygame.display.set_mode((VentanaX,VentanaY))
pygame.display.set_caption("Hola, mundo!")
Mi_imagen = pygame.image.load("Ejemplo1/ovni.png")
Mi_imagen = pygame.transform.scale(Mi_imagen,(int(VentanaX*Porcentaje/100),int(VentanaY*Porcentaje/100)))

rectangulo = pygame.Rect(RectX-RectX,RectY-RectY,RectX,RectY)
ColorRectangulo = pygame.Color(255,0,0)

def DibujaImagen():
    ventana.blit(Mi_imagen,(PosX,PosY))

def DibujarRectangulos():
    rectangulo.left,rectangulo.top = pygame.mouse.get_pos()
    rectangulo.left,rectangulo.top=rectangulo.left-int(RectX/2),rectangulo.top-int(RectY/2)
    pygame.draw.rect(ventana,ColorRectangulo,rectangulo)


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
    if ventana.get_at(pygame.mouse.get_pos())!=ColorFondo and ventana.get_at(pygame.mouse.get_pos()) != ColorRectangulo:
        ColorFondo = pygame.Color(255,255,255)
    else:
        ColorFondo = pygame.Color(160,160,255)
    DibujarRectangulos()
    if ColorFondo == pygame.Color(255,255,255):
        Velocidad = 0
    else:
        Velocidad = 1
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.display.update()