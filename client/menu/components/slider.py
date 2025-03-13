import pygame
from menu.components.input import Input

class Slider(Input):
    def __init__(self, loc_x, loc_y, width, height):
        # slider is a little different, a small rect that slides along a line
        Input.__init__(loc_x, loc_y, width, height)