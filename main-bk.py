import pygame
import time
import random

# Initialize Pygame
pygame.font.init()

# Constants
WIDTH, HEIGHT = 1000, 800
PLAYER_WIDTH, PLAYER_HEIGHT = 60, 80
PLAYER_VELOCITY = 5
EGG_WIDTH, EGG_HEIGHT = 40, 60
EGG_VELOCITY = 5
FPS = 60
FONT = pygame.font.SysFont("comicsans", 30)

# Load assets
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")
BG = pygame.transform.scale(pygame.image.load('bg.jpeg'), (WIDTH, HEIGHT))

player_image = pygame.image.load('player.png').convert_alpha()
player_image = pygame.transform.scale(player_image, (PLAYER_WIDTH, PLAYER_HEIGHT))

egg_image = pygame.image.load('egg.png').convert_alpha()
egg_image = pygame.transform.scale(egg_image, (EGG_WIDTH, EGG_HEIGHT))

def draw_window(player, elapsed_time, eggs, score):
	WIN.blit(BG, (0, 0))
	time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, (255, 255, 255))
	WIN.blit(time_text, (10, 10))
	
	score_text = FONT.render(f"Scores: {score}", 1, (255, 255, 255))
	WIN.blit(score_text, (WIDTH - score_text.get_width() - 10, 10))
	WIN.blit(player_image, (player.x, player.y))
	for egg in eggs:
		WIN.blit(egg_image, (egg.x, egg.y))
		# pygame.draw.rect(WIN, "red", (egg.x, egg.y, egg.width, egg.height))
	pygame.display.update()

def handle_player_movement(keys, player):
	if keys[pygame.K_LEFT] and player.x - PLAYER_VELOCITY >= 0:
		player.x -= PLAYER_VELOCITY
	if keys[pygame.K_RIGHT] and player.x + PLAYER_VELOCITY + player.width <= WIDTH:
		player.x += PLAYER_VELOCITY
	if keys[pygame.K_UP] and player.y - PLAYER_VELOCITY >= player.height:
		player.y -= PLAYER_VELOCITY
	if keys[pygame.K_DOWN] and player.y + PLAYER_VELOCITY + player.height <= HEIGHT:
		player.y += PLAYER_VELOCITY

def spawn_eggs(eggs, egg_add_increment):
	for _ in range(3):
		egg_x = random.randint(0, WIDTH - EGG_WIDTH)
		egg = pygame.Rect(egg_x, -EGG_HEIGHT, EGG_WIDTH, EGG_HEIGHT)
		eggs.append(egg)
	return max(200, egg_add_increment - 50)

def main():
	running = True
	score = 0
	player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
	clock = pygame.time.Clock()
	start_time = time.time()
	elapsed_time = 0
	eggs = []
	egg_spawn_time = 0
	egg_add_increment = 2000
	egg_count = 0

	while running:
		egg_count += clock.tick(FPS)
		elapsed_time = time.time() - start_time

		if egg_count > egg_add_increment:
			egg_add_increment = spawn_eggs(eggs, egg_add_increment)
			egg_count = 0

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		keys = pygame.key.get_pressed()
		handle_player_movement(keys, player)

		for egg in eggs[:]:
			egg.y += EGG_VELOCITY
			if egg.y > HEIGHT:
				eggs.remove(egg)
			elif egg.y + egg.height >= player.y and player.colliderect(egg):
				eggs.remove(egg)
				score += 1;
				# running = False
				break

		draw_window(player, elapsed_time, eggs, score)

	pygame.quit()

if __name__ == "__main__":
	main()
