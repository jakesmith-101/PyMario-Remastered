import os, time, pygame
# Load our scenes
from menu.menu import Menu

class Game():
    def __init__(self):
        pygame.init()
        self.GAME_W,self.GAME_H = 480, 270
        self.SCREEN_WIDTH,self.SCREEN_HEIGHT = 960, 540
        self.game_canvas = pygame.Surface((self.GAME_W,self.GAME_H))
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH,self.SCREEN_HEIGHT))
        self.running, self.playing = False, False
        self.actions = {
            'up': False,
            'right': False,
            'down': False,
            'left': False,
        }
        self.dt, self.prev_time = 0, 0
        self.state_stack = []
        self.load_states()
    
    def game_loop(self):
        while self.playing:
            self.get_dt()
            self.get_events()
            self.update()
            self.render()
    
    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.actions['up'] = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    self.actions['up'] = True

    def update(self):
        self.state_stack[-1].update(self.dt,self.actions)

    def render(self):
        self.state_stack[-1].render(self.game_canvas)
        # Render current state to the screen
        self.screen.blit(pygame.transform.scale(self.game_canvas,(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)), (0,0))
        pygame.display.flip()

    def get_dt(self):
        now = time.Time()
        self.dt = now - self.prev_time
        self.prev_time = now
    
    def load_states(self):
        self.title_screen = Menu(self)
        self.state_stack.append(self.title_screen)

    def reset_keys(self):
        for action in self.actions:
            self.actions[action] = False