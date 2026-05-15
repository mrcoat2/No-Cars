import pygame
import objects

# 1. Initialize Pygame
pygame.init()

# 2. Set up the display window
screen = pygame.display.set_mode([1080, 720])
pygame.display.set_caption("My First Pygame")

# 3. Game Loop
running = True
while running:
    # Check for events (like clicking the 'X' button)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 4. Drawing
    screen.fill((0, 255, 0))  # Fill background with white
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)  # Draw blue circle

    # 5. Update the display
    pygame.display.flip()

# 6. Clean up and quit
pygame.quit()
