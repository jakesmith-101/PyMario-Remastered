import pygame
from state import State

# The base of all menus in the game
class Menu(State):
    def __init__(self, game):
        State.__init__(self, game)