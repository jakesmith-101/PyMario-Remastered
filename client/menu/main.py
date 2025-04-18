from menu.menu import Menu
from world.world import World

class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        

    def update(self, delta_time, actions):
        if actions["start"]:
            new_state = World(self.game)
            new_state.enter_state()
        self.game.reset_keys()

    def render(self, display):
        display.fill((255,255,255))
        self.game.draw_text(display, "Game States Demo", (0,0,0), self.game.GAME_W/2, self.game.GAME_H/2 )