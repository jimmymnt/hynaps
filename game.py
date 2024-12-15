import pygame
from bullet import Bullet
from constants import (
  WIDTH, HEIGHT, FPS, WHITE, BLACK, RED, YELLOW, SLIDER_WIDTH, SLIDER_HEIGHT, DARK_GRAY,
  LEFT_HIT, RIGHT_HIT, LEFT_SPACE_SHIP, RIGHT_SPACE_SHIP, BULLET_HIT_SOUND, SPACE,
  BULLET_FIRE_SOUND, VOLUME_TEXT, LEFT_HEALTH_TEXT, RIGHT_HEALTH_TEXT, BULLET_VELOCITY
)
from spaceship import Spaceship

class Game:
  def __init__(self):
    pygame.init()
    self.running = True
    self.dragging = False
    self.clock = pygame.time.Clock()
    self.left_bullets = []
    self.right_bullets = []
    self.volume = 0.1  # Default volume (10%)
    self.slider_x = WIDTH // 2 - SLIDER_WIDTH - 20
    self.slider_y = 50
    self.knob_radius = 10
    self.left_spaceship = Spaceship(100, 300, LEFT_SPACE_SHIP)
    self.right_spaceship = Spaceship(800, 300, RIGHT_SPACE_SHIP)
    self.left_health = 10
    self.right_health = 10
    self.border = pygame.Rect(WIDTH // 2 - 5, 0, 10, HEIGHT)
    self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Space Invaders")
    BULLET_FIRE_SOUND.set_volume(self.volume)
    BULLET_HIT_SOUND.set_volume(self.volume)

  def draw_window(self):
    self.screen.blit(SPACE, (0, 0))
    self.screen.blit(self.left_spaceship.image, (self.left_spaceship.rect.x, self.left_spaceship.rect.y))
    self.screen.blit(self.right_spaceship.image, (self.right_spaceship.rect.x, self.right_spaceship.rect.y))
    self.screen.blit(LEFT_HEALTH_TEXT.render(f"Health: {self.left_health}", 1, WHITE), (10, 10))
    self.screen.blit(RIGHT_HEALTH_TEXT.render(f"Health: {self.right_health}", 1, WHITE), (WIDTH - 210, 10))
    
    # Draw slider
    pygame.draw.rect(self.screen, WHITE, (self.slider_x, self.slider_y, SLIDER_WIDTH, SLIDER_HEIGHT))
    knob_x = self.slider_x + int(self.volume * SLIDER_WIDTH)
    pygame.draw.circle(self.screen, RED, (knob_x, self.slider_y + SLIDER_HEIGHT // 2), self.knob_radius)

    # Draw volume percentage
    volume_text = VOLUME_TEXT.render(f"Volume: {int(self.volume * 100)}%", True, WHITE)
    self.screen.blit(volume_text, (self.slider_x, self.slider_y - 50))

    # Draw bullets
    for bullet in self.left_bullets + self.right_bullets:
      bullet.draw(self.screen)

    pygame.draw.rect(self.screen, DARK_GRAY, self.border)
    pygame.display.update()

  def handle_bullets(self):
    for bullet in self.left_bullets[:]:
      bullet.move()
      if self.right_spaceship.rect.colliderect(bullet.rect):
        BULLET_HIT_SOUND.play()
        pygame.event.post(pygame.event.Event(RIGHT_HIT))
        self.left_bullets.remove(bullet)
      elif bullet.rect.x > WIDTH:
        self.left_bullets.remove(bullet)

    for bullet in self.right_bullets[:]:
      bullet.move()
      if self.left_spaceship.rect.colliderect(bullet.rect):
        BULLET_HIT_SOUND.play()
        pygame.event.post(pygame.event.Event(LEFT_HIT))
        self.right_bullets.remove(bullet)
      elif bullet.rect.x < 0:
        self.right_bullets.remove(bullet)

  def handle_events(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.running = False

      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LCTRL:
          bullet = Bullet(
            self.left_spaceship.rect.x + self.left_spaceship.rect.width,
            self.left_spaceship.rect.y + self.left_spaceship.rect.height // 2 + 4,
            BULLET_VELOCITY,
            RED
          )
          self.left_bullets.append(bullet)
          bullet.fire_play()

        if event.key == pygame.K_RCTRL:
          bullet = Bullet(
            self.right_spaceship.rect.x,
            self.right_spaceship.rect.y + self.right_spaceship.rect.height // 2 + 4,
            -BULLET_VELOCITY,
            YELLOW
          )
          self.right_bullets.append(bullet)
          bullet.fire_play()

      # Handle mouse events
      if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        knob_x = self.slider_x + int(self.volume * SLIDER_WIDTH)
        if abs(mouse_x - knob_x) <= self.knob_radius and abs(mouse_y - self.slider_y) <= self.knob_radius:
          self.dragging = True  # Start dragging

      if event.type == pygame.MOUSEBUTTONUP:
        self.dragging = False  # Stop dragging
      
      winner_text = None
      if event.type == LEFT_HIT:
        self.left_health -= 1
        if self.left_health == 0:
          print("RIGHT WINS!")
          winner_text = "RIGHT WINS!"
          self.running = False
      
      if event.type == RIGHT_HIT:
        self.right_health -= 1
        if self.right_health == 0:
          print("LEFT WINS!")
          winner_text = "LEFT WINS!"
          self.running = False
      
      if winner_text:
        font = pygame.font.Font(None, 74)
        text = font.render(winner_text, True, WHITE)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.screen.blit(text, text_rect)

        # Delay for 2 seconds
        pygame.display.flip()
        pygame.time.wait(2000)

  def update_volume(self):
    if self.dragging:
      mouse_x, _ = pygame.mouse.get_pos()
      knob_x = max(self.slider_x, min(mouse_x, self.slider_x + SLIDER_WIDTH))
      self.volume = (knob_x - self.slider_x) / SLIDER_WIDTH
      BULLET_FIRE_SOUND.set_volume(self.volume)
      BULLET_HIT_SOUND.set_volume(self.volume)

  def run(self):
    while self.running:
      self.clock.tick(FPS)
      self.handle_events()
      self.update_volume()
      keys = pygame.key.get_pressed()
      self.left_spaceship.handle_movement(keys, left=True)
      self.right_spaceship.handle_movement(keys, left=False)
      self.handle_bullets()
      self.draw_window()

if __name__ == "__main__":
  game = Game()
  game.run()