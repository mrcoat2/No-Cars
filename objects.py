import ui
import pygame

class Road:
    def __init__(self, start_x, start_y, end_x, end_y):
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        
        self.road_color = (54, 53, 52)
        self.width = 50
    
    def draw(self, screen):
        pygame.draw.line(screen, self.road_color, (self.start_x, self.start_y), (self.end_x, self.end_y), self.width)

if __name__ == '__main__':
    pass