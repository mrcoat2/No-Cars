import ui
import pygame

ROAD_COLOR = (54, 53, 52)
ROAD_WIDTH = 50

CAR_SIZE = 20

class TopRoadNode:
    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y

class RoadNode:
    def __init__(self, start_node, end_x, end_y):
        if start_node == 0:
            self.start_node = TopRoadNode(end_x, end_y) # If start_node = 0 then attach to the top of the tree
        else:
            self.start_node = start_node

        self.end_x = end_x
        self.end_y = end_y
        
        self.color = ROAD_COLOR
        self.width = ROAD_WIDTH
    
    def draw(self, screen):
        pygame.draw.line(screen, self.color, (self.start_x, self.start_y), (self.end_x, self.end_y), self.width)

class Car:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x-CAR_SIZE/2, y-CAR_SIZE/2, CAR_SIZE, CAR_SIZE)
        
        self.color = (255, 53, 52)
        self.width = 50
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

if __name__ == '__main__':
    pass