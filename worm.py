# -*- coding: utf-8 -*-

from collections import deque

class Worm(object):
    def __init__(self):
        self.structure = deque([])
        self.length = 3
        self.score = 0

    def add(self, position):
        gameover = False
        if len(self.structure) >= self.length:
            self.structure.popleft()
        if position in self.structure:
            gameover = True
        self.structure.append(position)
        return gameover


    def eatApple(self):
        self.score += 10
        self.length += 3

