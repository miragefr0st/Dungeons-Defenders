import pygame
from assets import *

gameVar={}
with open("game.txt", "r") as game_:
    game = game_.read()
    exec(game, gameVar)

class Enemy1:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("res/alien.gif")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.xspeed = -int(gameVar.get("spd", 0))
        self.yspeed = 0
        self.health = int(gameVar.get("hlth", 0))

    def draw(self):
        screen.blit(self.image, (self.x, self.y))
        for x in range(0, self.health):
            rct = pygame.Rect(self.x - int(gameVar.get("healthspacing", 0)) + x * 1, self.y - 5, 3, 4)
            pygame.draw.rect(screen, green, rct, 0)

    def move(self):
        rect = self.image.get_rect()
        rect.left = self.x
        rect.top = self.y
        if rect.colliderect(barrierleftrect):
            self.xspeed = -int(gameVar.get("spd", 0))
            self.yspeed = 0
        if rect.colliderect(barrierrightrect):
            self.xspeed = int(gameVar.get("spd", 0))
            self.yspeed = 0
        if rect.colliderect(barrierdownrect) or rect.colliderect(barrierdownrect2):
            self.xspeed = 0
            self.yspeed = int(gameVar.get("spd", 0))
        self.x += self.xspeed
        self.y += self.yspeed

    def hitTest(self, x, y):
        if x > self.x - 25 and x < self.x + self.width + 25 and y > self.y - 25 and y < self.y + self.height + 25:
            return True
        else:
            return False

class Enemy2(Enemy1):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.image.load("res/boss.gif")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.health = 20  # ajuste la santé du boss selon tes besoins
        self.xspeed = -1  # ajuste la vitesse du boss selon tes besoins
        self.yspeed = 0
class Boss(Enemy1):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.image.load("res/boss.gif")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.health = 50  # ajuste la santé du boss selon tes besoins
        self.xspeed = -1  # ajuste la vitesse du boss selon tes besoins
        self.yspeed = 0
                
