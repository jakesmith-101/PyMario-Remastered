import pygame

class Entity():
    def __init__(self, loc_x=0, loc_y=0, width=25, height=25):
        self.rect = pygame.Rect(loc_x, loc_y, width, height)
    
    def move(self, dir_x=0, dir_y=0):
        self.rect.x += dir_x
        self.rect.y += dir_y

    