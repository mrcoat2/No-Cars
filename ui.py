import pygame, objects

class UI:
    def __init__(self,window_size=[1080, 720]):
        pygame.init()

        # 2. Set up the display window
        self.screen = pygame.display.set_mode(window_size)
        pygame.display.set_caption("Self driving cars")
        self.objects = []
        self.cars = []
        
    def add_object(self, obj):
        self.objects.append(obj)

    def new_road_tree(self, start_x, start_y):
        node = objects.RoadNode(0, start_x, start_y)
        self.add_object(node)
        return node

    def new_road_node(self, start_node, end_x, end_y):
        node = objects.RoadNode(start_node, end_x, end_y)
        self.add_object(node)
        return node

    def new_car(self, sock):
        car = objects.Car(sock)
        self.add_object(car)
        self.cars.append(car)

    def audit_cars(self):
        for car in self.cars:
            car.audit()

    def draw_all(self):
        for obj in self.objects:
            obj.draw(self.screen)