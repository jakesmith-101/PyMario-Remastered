import pygame, os
from state import State
from menu.pause import PauseMenu
from client.world.entity.player import Player

class Game_World(State):
    def __init__(self, game):
        State.__init__(self,game)
        self.player = Player(self.game)
        self.grass_img = pygame.image.load(os.path.join(self.game.assets_dir, "map", "grass.png"))

    def update(self,delta_time, actions):
        # Check if the game was paused 
        if actions["start"]:
            new_state = PauseMenu(self.game)
            new_state.enter_state()
        self.player.update(delta_time, actions)
    def render(self, display):
        display.blit(self.grass_img, (0,0))
        self.player.render(display)