import pygame

class Entity():
    def __init__(self, loc_x=0, loc_y=0, width=25, height=50):
        self.rect = pygame.Rect(loc_x, loc_y, width, height)