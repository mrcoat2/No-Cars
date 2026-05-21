import pygame
import ui
import objects

# 1. Initialize Pygame
CarUI = ui.UI()
screen = CarUI.screen

# 3. Game Loop
running = True
clock = pygame.time.Clock()

road_p_one = CarUI.new_road_tree(200,200)
road_p_two = CarUI.new_road_node(road_p_one, 200, 500)
road_p_three = CarUI.new_road_node(road_p_two, 500, 500)
fiveHundredNorth = CarUI.new_road_node(road_p_three, 500, 100)
road_p_four = CarUI.new_road_node(road_p_three, 500, 800)
CarUI.new_car(200,250)

while running:
    # Check for events (like clicking the 'X' button)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Logic
    # fiveHundredNorth.p_x -= 1

    # 4. Drawing
    screen.fill((0, 255, 0))  # Fill background with gree
    CarUI.draw_all()  # Draw blue circle

    # 5. Update the display
    pygame.display.flip()
    clock.tick(60) # Limit to 60 frames per second

# 6. Clean up and quit
pygame.quit()
