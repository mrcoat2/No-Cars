import threading
import pygame
import ui
import socket
import pickle

# 1. Initialize Pygame
CarUI = ui.UI()
screen = CarUI.screen

# 3. Game Loop
running = True
clock = pygame.time.Clock()

address = "127.0.0.1"
port = 4090

road_p_one = CarUI.new_road_tree(200,200)
road_p_two = CarUI.new_road_node(road_p_one, 200, 500)
road_p_three = CarUI.new_road_node(road_p_two, 500, 500)
fiveHundredNorth = CarUI.new_road_node(road_p_three, 500, 100)
road_p_four = CarUI.new_road_node(road_p_three, 500, 800)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((address, port)) # Bind to address and port
    s.listen()                   # Enable server to accept connections
    s.settimeout(0.001)

    while running:
        # Accept car client #
        try:
            conn, addr = s.accept()
            print("Client connected")
            CarUI.new_car(conn)
        except:
            pass  # No client available

        # Logic
        # fiveHundredNorth.p_x -= 1
        CarUI.audit_cars()        

        # 4. Drawing
        screen.fill((0, 255, 0))  # Fill background with gree
        CarUI.draw_all()  # Draw blue circle
        
        # 5. Update the display
        pygame.display.flip()

        # Check for events (like clicking the 'X' button)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        clock.tick(60) # Limit to 60 frames per second

    # 6. Clean up and quit
    pygame.quit()
