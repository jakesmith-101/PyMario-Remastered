import pygame, os
from menu.menu import Menu
from menu.options import GameOptionsMenu, AudioOptionsMenu, VideoOptionsMenu, ControlsOptionsMenu
# TODO: abstract most logic here to the Menu Base Class

class PauseMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        # Set the menu
        self.menu_img = pygame.image.load(os.path.join(self.game.assets_dir, "map", "menu.png"))
        self.menu_rect = self.menu_img.get_rect()
        self.menu_rect.center = (self.game.GAME_W*.85, self.game.GAME_H*.4)
        # Set the cursor and menu states
        self.menu_options = {0: "Game", 1: "Audio", 2: "Video", 3: "Controls", 4: "Exit"}
        self.index = 0
        self.cursor_img = pygame.image.load(os.path.join(self.game.assets_dir, "map", "cursor.png"))
        self.cursor_rect = self.cursor_img.get_rect()
        self.cursor_pos_y = self.menu_rect.y + 38
        self.cursor_rect.x, self.cursor_rect.y = self.menu_rect.x + 10, self.cursor_pos_y

    def update(self, delta_time, actions):  
        self.update_cursor(actions)      
        if actions["action1"]:
            self.transition_state()
        if actions["action2"]:
            self.exit_state()
        self.game.reset_keys()

    def render(self, display):
        # render the gameworld behind the menu, which is right before the pause menu on the stack
        #self.game.state_stack[-2].render(display)
        self.prev_state.render(display)
        display.blit(self.menu_img, self.menu_rect)
        display.blit(self.cursor_img, self.cursor_rect)

    def transition_state(self):
        if self.menu_options[self.index] == "Game": 
            pass # TO-DO
        elif self.menu_options[self.index] == "Audio": 
            pass # TO-DO
        elif self.menu_options[self.index] == "Video": 
            pass # TO-DO
        elif self.menu_options[self.index] == "Controls": 
            pass # TO-DO
        elif self.menu_options[self.index] == "Exit": 
            while len(self.game.state_stack) > 1:
                self.game.state_stack.pop()


    def update_cursor(self, actions):
        if actions['down']:
            self.index = (self.index + 1) % len(self.menu_options)
        elif actions['up']:
            self.index = (self.index - 1) % len(self.menu_options)
        self.cursor_rect.y = self.cursor_pos_y + (self.index * 32)