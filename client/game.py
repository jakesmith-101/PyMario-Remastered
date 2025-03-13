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
            'up': False,        # move up: W or UP
            'right': False,     # move right: D or RIGHT
            'down': False,      # move down: S or DOWN
            'left': False,      # move left: A or LEFT
            'action1': False,   # action 1: O or SPACE
            'action2': False,   # action 2: P or LSHIFT
            'start': False,     # pause/select: ENTER or ESCAPE
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
    
    def get_events(self): # rewrite to make controls changable
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    self.actions['up'] = True
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    self.actions['right'] = True
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    self.actions['down'] = True
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    self.actions['left'] = True
                if event.key == pygame.K_o or event.key == pygame.K_SPACE:
                    self.actions['action1'] = True
                if event.key == pygame.K_p or event.key == pygame.K_LSHIFT:
                    self.actions['action2'] = True
                if event.key == pygame.K_RETURN or event.key == pygame.K_ESCAPE:
                    self.actions['start'] = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    self.actions['up'] = False
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    self.actions['right'] = False
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    self.actions['down'] = False
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    self.actions['left'] = False
                if event.key == pygame.K_o or event.key == pygame.K_SPACE:
                    self.actions['action1'] = False
                if event.key == pygame.K_p or event.key == pygame.K_LSHIFT:
                    self.actions['action2'] = False
                if event.key == pygame.K_RETURN or event.key == pygame.K_ESCAPE:
                    self.actions['start'] = False

    def update(self):
        self.state_stack[-1].update(self.dt,self.actions)

    def render(self):
        self.state_stack[-1].render(self.game_canvas)
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