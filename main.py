import pygame
from pygame.locals import *
import sys
from modelos.util import cargar_imagen
from modelos.constructores import *
import random

SCREEN_WIDTH = 300
SCREEN_HEIGHT = 300
ICON_SIZE = 32

def game():
  pygame.init()
  director = Director()
  # director1 = Director()
  # director2 = Director()  
  director.set_constructor(ConstructorHumanos())
  heroe = director.get_heroe()

  director.set_constructor(ConstructorZombie())
  #director.set_constructor(ConstructorZombie())

  img_inicio = cargar_imagen('imagenes/inicio2.jpg')
  img_fondo = cargar_imagen('imagenes/fondo.jpg')
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

  pygame.mouse.set_visible(False)

  
  zombie= director.get_zombie()
  zombie2= director.get_zombie1()
  jugando = False
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()
    teclas = pygame.key.get_pressed()
    if teclas[K_SPACE]:

      heroe.ubicar((200,200))
      zombie.ubicar((100,100))
      zombie2.ubicar((150,150))
      #pygame.time.delay(100)
      jugando = True
    if jugando:
      #1
      screen.blit(img_fondo, (0, 0))
      #print("sentido heroe: "+str(heroe.update()))
      heroe.update()
      posHeroe = heroe.draw(screen)
      #print(heroe.getposicion())
      #print(heroe.getposicion()[1])
      #print(zombie.getposicion())
      #print(zombie.getposicion()[1])
      zombie.update()
      #zombie2.ubicar((170,170))
      posZombie1 = zombie.draw(screen)
      

      zombie2.update()
      posZombie2 = zombie2.draw(screen)
      
      if(posZombie1[0]==posHeroe[0] and posZombie1[1]==posHeroe[1]):
        jugando = False
        print("fin del juego")

      if(posZombie2[0]==posHeroe[0] and posZombie2[1]==posHeroe[1]):
        jugando = False
        print("fin del juego")

      # if(zombie2.getposicion()[0]==heroe.getposicion()[0] and zombie2.getposicion()[1]==heroe.getposicion()[1]):
      #  jugando=False
      #  print("fin del juego")
       
    else:
      screen.blit(img_inicio, (0, 0))
    pygame.display.update()
    pygame.time.delay(100)
    #print(jugando)


if __name__ == '__main__':
  game()