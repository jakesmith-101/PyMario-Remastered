import pygame

# Foreground, Middleground and Background terrain (bushes etc.)
# entirely cosmetic, late implement

class Ground():
    def __init__(self, place='middle', loc_x=0, loc_y=0, width=25, height=25):
        self.rect = pygame.Rect(loc_x, loc_y, width, height)
        self.place = place

    