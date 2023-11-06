import pygame

RESOLUTION = (1600, 900)
CAPTION = "Boomerang"

running = True

# Initialize pygame
pygame.init()
window_surface = pygame.display.set_mode(RESOLUTION)
pygame.display.set_caption(CAPTION)
window_surface.fill((255, 255, 255))

# Game loop
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False
        elif event.type == pygame.KEYDOWN:
            ...

pygame.quit()