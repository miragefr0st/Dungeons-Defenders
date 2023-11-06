import pygame as pg
import constants as c
from enemy import Enemy

#initialiser pygame
pg.init()

#create clock
clock = pg.time.Clock()

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1020
FPS = 60

#créer la fenêtre
screen = pg.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
pg.display.set_caption("Dungeons Defenders")   

#load images
enemy_image = pg.image.load()
#game loop
run = True
while run:
    
    clock.tick(c.FPS)
    
    #event handler
    for event in pg.event.get():
        #quit program
        if event.type == pg.QUIT:
            run == False
            
pg.quit()

    

    
