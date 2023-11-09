import pygame
from assets import *


class Bullet:  # Juggernaught Ammo
    def __init__(self, pos, speed):
        self.x = pos[0]
        self.y = pos[1]
        self.width = 5
        self.height = 5
        self.pos = pos
        self.speed = speed
    def move(self):
        self.pos[0] = int(self.pos[0] + self.speed[0])
        self.pos[1] = int(self.pos[1] + self.speed[1])
        self.x = self.pos[0]
        self.y = self.pos[1]
    def draw(self):
        pygame.draw.circle(screen, blue, self.pos, 10, 3)
    def hitTest(self, x, y):
        if x > self.x - self.width / 2 and x < self.x + self.width / 2 and y > self.y - self.height / 2 and y < self.y + self.height / 2:
            return True
        else:
            return False
class Laser:  # Laser Cannons Ammo
    def __init__(self, start, end):
        self.start = start
        self.end = end
    def draw(self):
        pygame.draw.line(screen, red, self.start, self.end, 2)