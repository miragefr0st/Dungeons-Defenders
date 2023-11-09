import pygame
import math
import projectile
from assets import *


# Tour rafalle
class Tour:  
    def __init__(self, x, y, screen, size):
        self.x = x
        self.y = y
        self.cost = 300
        self.image = pygame.image.load("res/towerimg1.gif")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.reload = 0
    def shoot(self):
        if self.reload > 60 and len(enemies1) > 0:
            min_d = 300  # Tower's Range
            enemy = None
            for e1 in enemies1:
                d = math.sqrt((t1.x - e1.x) ** 2 + (t1.y - e1.y) ** 2)
                if d < min_d:
                    min_d = d
                    enemy = e1
            if enemy != None:
                angle = math.atan2(t1.y - enemy.y - 30, t1.x - enemy.x - 30)
                bx = -5 * math.cos(angle)
                by = -5 * math.sin(angle)
                bullet = projectile.Bullet([t1.x, t1.y], [bx, by])
                bullets.append(bullet)
            self.reload = 0
        self.reload = self.reload + 1
    def draw(self):
        screen.blit(self.image, (self.x - self.width / 2, self.y - self.height / 2))
    def hitTest(self, x, y):
        if x > self.x - self.width / 2 and x < self.x + self.width / 2 and y > self.y - self.height / 2 and y < self.y + self.height / 2:
            return True
        else:
            return False

# Canon Laser
class Tour2:  
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.cost = 500
        self.image = pygame.image.load("res/towerimg2.gif")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.reload = 0
    def shoot(self):
        if self.reload > 15 and len(enemies1) > 0:
            min_d = 150  # Tower's Range
            enemy = None
            for e1 in enemies1:
                d = math.sqrt((t2.x - e1.x - 15) ** 2 + (t2.y - e1.y - 15) ** 2)
                if d < min_d:
                    min_d = d
                    enemy = e1
            if enemy != None:
                laser = projectile.Laser([self.x, self.y], [enemy.x + 15, enemy.y + 15])
                lasers.append(laser)
            self.reload = 0
        self.reload = self.reload + 1
    def draw(self):
        screen.blit(self.image, (self.x - self.width / 2, self.y - self.height / 2))
    def hitTest(self, x, y):
        if x > self.x - self.width / 2 and x < self.x + self.width / 2 and y > self.y - self.height / 2 and y < self.y + self.height / 2:
            return True
        else:
            return False

# Farmer     
class Tour3:  
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.cost = 1000
        self.image = pygame.image.load("res/towerimg3.gif")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
    def draw(self):
        screen.blit(self.image, (self.x - self.width / 2, self.y - self.height / 2))
    def hitTest(self, x, y):
        if x > self.x - self.width / 2 and x < self.x + self.width / 2 and y > self.y - self.height / 2 and y < self.y + self.height / 2:
            return True
        else:
            return False        
        
