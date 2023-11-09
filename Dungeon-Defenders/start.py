import pygame
import sys
from assets import *
import howtoplay
import game


def start():
    startrect = pygame.Rect(550, 250, 200, 50)  # Rectangles pour cliquer et sélectionner
    howrect = pygame.Rect(455, 350, 400, 50)
    quitrect = pygame.Rect(565, 450, 180, 50)
    backround = pygame.image.load("res/start.gif")
    
    while True:
        screen.blit(backround, [0, 0, 0, 0])
        mx, my = pygame.mouse.get_pos()
        mouserect = pygame.Rect(mx - 15, my - 15, 30, 30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
        if keys[pygame.K_SPACE]:
            game.game()

        renderedText = font2.render("D. Defenders", 1, white)
        screen.blit(renderedText, (270, 50))

        if mouserect.colliderect(
                startrect):  
            renderedText = font3.render(">Jouer", 1, orange)
            screen.blit(renderedText, (550, 250))
            if pygame.mouse.get_pressed()[0]:
                game.game()
        else:
            renderedText = font3.render("Jouer", 1, white)
            screen.blit(renderedText, (550, 250))
        
        if mouserect.colliderect(howrect):
            renderedText = font3.render(">How To Play", 1, orange)
            screen.blit(renderedText, (455, 350))
            
            if pygame.mouse.get_pressed()[0]:
                howtoplay.howtoplay()
        else:
            renderedText = font3.render("How To Play", 1, white)
            screen.blit(renderedText, (455, 350))

        if mouserect.colliderect(quitrect):
            renderedText = font3.render(">Quitter", 1, orange)
            screen.blit(renderedText, (565, 450))
            if pygame.mouse.get_pressed()[0]:
                pygame.quit()
                sys.exit()
        else:
            renderedText = font3.render("Quitter", 1, white)
            screen.blit(renderedText, (565, 450))

        pygame.display.flip()
        # Fin du Start Loop

