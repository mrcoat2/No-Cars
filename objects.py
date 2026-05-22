import pickle

import ui
import pygame
import math
import socket

ROAD_COLOR = (54, 53, 52)
ROAD_WIDTH = 50

CAR_SIZE = 20

class TopRoadNode:
    def __init__(self, start_x, start_y):
        self.p_x = start_x
        self.p_y = start_y

class RoadNode:
    def __init__(self, start_node, end_x, end_y):
        if start_node == 0:
            self.start_node = TopRoadNode(end_x, end_y) # If start_node = 0 then attach to the top of the tree
        else:
            self.start_node = start_node

        self.p_x = end_x
        self.p_y = end_y
        
        self.color = ROAD_COLOR
        self.width = ROAD_WIDTH
    
    def draw(self, screen):
        # Start line half a road width back and end further
        # Calculate angle
        run = self.start_node.p_x - self.p_x
        rise = self.start_node.p_y - self.p_y
        if run == 0:
            start_draw_x = self.start_node.p_x
            start_draw_y = self.start_node.p_y - ROAD_WIDTH/2

            end_draw_x = self.p_x
            end_draw_y = self.p_y + ROAD_WIDTH/2
        else:
            slope = rise / run
            theta = math.atan(slope)
            start_draw_x = self.start_node.p_x - math.cos(theta) * ROAD_WIDTH/2
            start_draw_y = self.start_node.p_y - math.sin(theta) * ROAD_WIDTH/2

            end_draw_x = self.p_x + math.cos(theta) * ROAD_WIDTH/2
            end_draw_y = self.p_y + math.sin(theta) * ROAD_WIDTH/2

        pygame.draw.line(screen, self.color, (start_draw_x, start_draw_y), (end_draw_x, end_draw_y), self.width)

class Car:
    def __init__(self, sock):
        self.sock = sock
        self.init_car() # Initialize car position from server data
        
        self.color = (255, 53, 52)
        self.width = 50
        self.speed = [0, 0] # [x_speed, y_speed]
        self.destination = None

    def init_car(self):
        raw_data = self.sock.recv(1024) # Receive car position data
        car_data = pickle.loads(raw_data)
        self.x = car_data[0]
        self.y = car_data[1]
        self.width = car_data[2]
        self.height = car_data[3]
        print(f"Initialized car at position ({self.x}, {self.y}) with size ({self.width}x{self.height})")

        self.rect = pygame.Rect(self.x-self.width/2, self.y-self.height/2, self.width, self.height)

    def audit(self):
        self.sock.sendall(b"audit")
        
        raw_data = self.sock.recv(1024)
        print(f"Received audit data: {raw_data}")
            
        if raw_data:
            car_data = pickle.loads(raw_data)
            self.x = car_data[0]
            self.y = car_data[1]
            self.width = car_data[2]
            self.height = car_data[3]
            self.rect.x = self.x - self.width/2
            self.rect.y = self.y - self.height/2

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

if __name__ == '__main__':
    pass