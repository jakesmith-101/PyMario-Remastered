import pygame

class Input():
    def __init__(self, loc_x, loc_y, width, height):
        self.rect = pygame.Rect(loc_x, loc_y, width, height)