import pygame, objects

class UI:
    def __init__(self,window_size=[1080, 720]):
        pygame.init()

        # 2. Set up the display window
        self.screen = pygame.display.set_mode(window_size)
        pygame.display.set_caption("Self driving cars")
        self.objects = []
        
    def add_object(self, obj):
        self.objects.append(obj)

    def new_road(self, start_x, start_y, end_x, end_y):
        self.add_object(objects.Road(start_x, start_y, end_x, end_y))


    def draw_all(self):
        for obj in self.objects:
            obj.draw(self.screen)