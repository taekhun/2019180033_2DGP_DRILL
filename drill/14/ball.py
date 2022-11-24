import game_framework
from pico2d import *
import random

import game_world
import server

class Ball:

    def __init__(self):
        # Boy is only once created, so instance image loading is fine
        self.image = load_image('ball21x21.png')
        self.x, self.y = random.randint(0, 1837), random.randint(0, 1109)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def set_background(self, bg):
        self.bg = bg
        self.x = self.bg.w / 2
        self.y = self.bg.h / 2

    def update(self):
        pass

    def draw(self):
        sx, sy = self.x - server.background.window_left, self.y - server.background.window_bottom
        self.image.draw(sx, sy)

    def handle_collision(self, other, group):
        if group == 'ball:boy':
            game_world.remove_object(self)
