from pygame import *
from pygame.sprite import Sprite
import random


class Zombie(Sprite):
  
#  instance = None
#  def __new__(cls, *arg, **kargs):
#    if cls.instance is None:
#      cls.instance = object.__new__(cls, *arg, **kargs)
#    return cls.instance

  def __init__(self):
    Sprite.__init__(self)
    self.sentido = 0
    self.velocidad = 10
    self.cont = 0
    self.vida = 100
    self.puntos = 0

  def ubicar(self, pos):
    self.rect.x = pos[0]
    self.rect.y = pos[1]

  def set_sprites(self, sprites):
    self.imagenes = sprites
    self.image = self.imagenes[self.sentido][0]
    self.rect = self.image.get_rect()

  def update(self):
    teclas = key.get_pressed()
    r = (random.randrange(0, 20,10))
    movimiento = random.randrange(0, 4, 1)
    print(movimiento)
    if teclas[K_LEFT] or teclas[K_RIGHT] or teclas[K_UP] or teclas[K_DOWN]:
      if movimiento == 0:
          self.rect.left -= (self.velocidad+r)
          self.sentido = 1
      if movimiento == 1:
        self.rect.left += (self.velocidad+r)
        self.sentido = 0
      if movimiento == 2:
        self.rect.top += (self.velocidad+r)
        self.sentido = 2
      if movimiento == 3:
        self.rect.top -= (self.velocidad+r)
        self.sentido = 3
  
      self.image = self.imagenes[self.sentido][self.cont]
      self.cont += 1
      self.cont %= 3
      self.puntos += 1

      # print(random.randrange(0, 3, 1))
      # print(random.randrange(0, 2, 1))

      # self.rect.top += (random.randrange(0, 6, 2))
      # self.rect.left -= (random.randrange(0, 5, 1))

      self.rect.top %=300
      self.rect.left %=300
    
  def draw(self, screen):
    fuente = font.Font(None, 20)
    texto = fuente.render("puntos: " + str(self.puntos), 1, (20,20,50))
    screen.blit(self.image, self.rect)
    list2 = [self.rect.x, self.rect.y]
    return list2
    # screen.blit(texto, (self.rect.x - 20, self.rect.y -15))
