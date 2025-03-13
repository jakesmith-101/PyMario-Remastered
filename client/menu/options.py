import pygame, os
from menu.menu import Menu

class OptionsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

class GameOptionsMenu(OptionsMenu):
    def __init__(self, game):
        OptionsMenu.__init__(self, game)

class AudioOptionsMenu(OptionsMenu):
    def __init__(self, game):
        OptionsMenu.__init__(self, game)

class VideoOptionsMenu(OptionsMenu):
    def __init__(self, game):
        OptionsMenu.__init__(self, game)

class ControlsOptionsMenu(OptionsMenu):
    def __init__(self, game):
        OptionsMenu.__init__(self, game)