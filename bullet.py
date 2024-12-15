import pygame

from constants import BULLET_FIRE_SOUND

class Bullet:
  def __init__(self, x, y, velocity, color):
    self.rect = pygame.Rect(x, y, 10, 5)
    self.velocity = velocity
    self.color = color
  
  def set_velocity(self, velocity):
    self.velocity = velocity

  def get_velocity(self):
    return self.velocity

  def move(self):
    self.rect.x += self.velocity

  def draw(self, window):
    pygame.draw.rect(window, self.color, self.rect)
  
  def fire_play(self):
    BULLET_FIRE_SOUND.play()