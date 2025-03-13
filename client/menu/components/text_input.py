import pygame
from menu.components.input import Input

class TextInput(Input):
    def __init__(self, loc_x, loc_y, width, height):
        Input.__init__(loc_x, loc_y, width, height)