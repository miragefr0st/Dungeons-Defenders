import pygame as pg

class Enemy(pg.sprite.Sprite):
    def _init_(self, pos, image):
        pg.sprite.Sprite._init_(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = pos