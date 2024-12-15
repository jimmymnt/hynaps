import pygame
import os

pygame.mixer.init()
pygame.font.init()

WIDTH, HEIGHT = 1000, 600

FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
LEFT_VELOCITY = 5
YELLOW = (255, 255, 0)
RIGHT_VELOCITY = 5
BULLET_VELOCITY = 7
DARK_GRAY = (105, 105, 105)
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

# EVENT
LEFT_HIT = pygame.USEREVENT + 1
RIGHT_HIT = pygame.USEREVENT + 2

BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'Gun+Silencer.mp3'))
BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'Grenade+1.mp3'))

# Slider settings
SLIDER_WIDTH = 200
SLIDER_HEIGHT = 10
KNOB_RADIUS = 10

LEFT_HEALTH_TEXT = pygame.font.SysFont('comicsans', 30)
RIGHT_HEALTH_TEXT = pygame.font.SysFont('comicsans', 30)
VOLUME_TEXT = pygame.font.SysFont('comicsans', 30)

SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

SPACE = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'space.png')), (WIDTH, HEIGHT))

LEFT_SPACE_SHIP_IMG = pygame.image.load(
  os.path.join('Assets', 'spaceship_left.png'),
)

LEFT_SPACE_SHIP = pygame.transform.rotate(
  pygame.transform.scale(LEFT_SPACE_SHIP_IMG, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)),
  90
)

RIGHT_SPACE_SHIP_IMG = pygame.image.load(
  os.path.join('Assets', 'spaceship_right.png'),
)

RIGHT_SPACE_SHIP = pygame.transform.rotate(
  pygame.transform.scale(RIGHT_SPACE_SHIP_IMG, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)),
  270
)

SPACE_VELOCITY = 5