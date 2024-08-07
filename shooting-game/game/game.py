import pygame
import requests
from player import Player
from enemy import Enemy
from bullet import Bullet

# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Create player
player = Player()

# Create groups for enemies and bullets
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()

# Add enemies to the group
for _ in range(10):
    enemy = Enemy()
    enemies.add(enemy)

# Create a group for all sprites
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(enemies)

# Game variables
running = True
game_over = False
player_score = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game_over:
                bullet = Bullet(player.rect.centerx, player.rect.top)
                all_sprites.add(bullet)
                bullets.add(bullet)

    if not game_over:
        all_sprites.update()

        # Check for collisions between bullets and enemies
        hits = pygame.sprite.groupcollide(bullets, enemies, True, True)
        for hit in hits:
            enemy = Enemy()
            enemies.add(enemy)
            all_sprites.add(enemy)
            player_score += 10  # Increase score for each hit

        # Check for collisions between player and enemies
        if pygame.sprite.spritecollideany(player, enemies):
            game_over = True

        # Draw everything
        screen.fill((0, 0, 0))
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    if game_over:
        # Display game over message
        font = pygame.font.Font(None, 74)
        text = font.render("Game Over", True, (255, 0, 0))
        screen.blit(text, (200, 250))
        pygame.display.flip()

        # Post score to leaderboard
        score_data = {
            'player_name': 'Player1',  # Replace with dynamic player name
            'score': player_score
        }
        response = requests.post('http://<EC2_INSTANCE_PUBLIC_IP>:5000/leaderboard', json=score_data)
        print(response.json())

        # Wait for a few seconds before quitting
        pygame.time.wait(3000)
        running = False

pygame.quit()
