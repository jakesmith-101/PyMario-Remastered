import pygame
from world.entity.entity import Entity

# base class for coins, powerups etc
# slightly different from other entities

class Item(Entity):
    def __init__(self, loc_x=0, loc_y=0, width=25, height=25):
        Entity.__init__(loc_x, loc_y, width, height)