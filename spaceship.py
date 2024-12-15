import pygame

from constants import SPACESHIP_WIDTH, SPACESHIP_HEIGHT, SPACE_VELOCITY, WIDTH, HEIGHT

class Spaceship:
  def __init__(self, x, y, image):
    self.rect = pygame.Rect(x, y, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    self.image = image
    self.velocity = SPACE_VELOCITY

  def handle_movement(self, keys, left=True):
    if left:
      if keys[pygame.K_a] and self.rect.x - self.velocity > 0:  # LEFT
        self.rect.x -= self.velocity
      if keys[pygame.K_d] and self.rect.x + SPACESHIP_WIDTH < WIDTH / 2:  # RIGHT
        self.rect.x += self.velocity
      if keys[pygame.K_w] and self.rect.y - self.velocity > 0:  # UP
        self.rect.y -= self.velocity
      if keys[pygame.K_s] and self.rect.y + SPACESHIP_HEIGHT + 20 < HEIGHT:  # DOWN
        self.rect.y += self.velocity
    else:
      if keys[pygame.K_LEFT] and self.rect.x - self.velocity > WIDTH / 2 + 10:  # LEFT
        self.rect.x -= self.velocity
      if keys[pygame.K_RIGHT] and self.rect.x + SPACESHIP_WIDTH < WIDTH:  # RIGHT
        self.rect.x += self.velocity
      if keys[pygame.K_UP] and self.rect.y - self.velocity > 0:  # UP
        self.rect.y -= self.velocity
      if keys[pygame.K_DOWN] and self.rect.y + SPACESHIP_HEIGHT + 20 < HEIGHT:  # DOWN
        self.rect.y += self.velocity
