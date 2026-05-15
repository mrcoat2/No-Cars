import pygame
import ui
import objects

# 1. Initialize Pygame
CarUI = ui.UI()
screen = CarUI.screen

# 3. Game Loop
running = True

CarUI.new_road(200,200,200,600)
while running:
    # Check for events (like clicking the 'X' button)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 4. Drawing
    screen.fill((0, 255, 0))  # Fill background with white
    CarUI.draw_all()  # Draw blue circle

    # 5. Update the display
    pygame.display.flip()

# 6. Clean up and quit
pygame.quit()
