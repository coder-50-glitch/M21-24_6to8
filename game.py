import pygame, random

# Setup window and load assets
pygame.init()
W, H = 500, 400
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Sprite Collision")
clock = pygame.time.Clock()

bg = pygame.transform.scale(pygame.image.load("background.jpg"), (W, H))
font = pygame.font.SysFont("Times New Roman", 72)
screen_rect = screen.get_rect()

# Create Sprites using a quick loop
all_sprites = pygame.sprite.Group()
colors = ['black', 'red']
sprites = []

for color in colors:
    sprite = pygame.sprite.Sprite(all_sprites)
    sprite.image = pygame.Surface((30, 20))
    sprite.image.fill(pygame.Color(color))
    sprite.rect = sprite.image.get_rect(
        x=random.randint(0, W - 30), y=random.randint(0, H - 20)
    )
    sprites.append(sprite)

p1, p2 = sprites[0], sprites[1]
running, won = True, False

# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_x):
            running = False

    if not won:
        # Get movement inputs
        keys = pygame.key.get_pressed()
        dx = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * 5
        dy = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * 5
        
        # Move player and keep them inside screen bounds
        p1.rect.move_ip(dx, dy)
        p1.rect.clamp_ip(screen_rect)

        # Check for collision
        if p1.rect.colliderect(p2.rect):
            p2.kill()  # Removes sprite2 from all groups
            won = True

    # Drawing steps
    screen.blit(bg, (0, 0))
    all_sprites.draw(screen)

    if won:
        txt = font.render("You win!", True, (0, 0, 0))
        screen.blit(txt, txt.get_rect(center=screen_rect.center))

    pygame.display.flip()
    clock.tick(90)

pygame.quit()
