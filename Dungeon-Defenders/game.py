import pygame
import sys
from enemy import Enemy1
from assets import *
import lose


def game():


    gameVar={}
    with open("game.txt", "r") as game_:
        game = game_.read()
        exec(game, gameVar)

    from turret import Tour, Tour2, Tour3

    # Game Loop 
    while True:
        xpos = int(gameVar.get("xpos", 0)) + int(gameVar.get("xspeed", 0))  # Enemy Movement
        ypos = int(gameVar.get("ypos", 0)) + int(gameVar.get("yspeed", 0))
        screen.blit(backround, [0, 0, 0, 0])
        mx, my = pygame.mouse.get_pos()
        mouserect = pygame.Rect(mx - 25, my - 25, 50, 50)  # Définir le "mouserec" pour placer et supprimer des tours
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()

        # Raccourcis pour le build des tours   
        if keys[pygame.K_1]:  
            icon = 1
            click = 0
        if keys[pygame.K_2]:
            icon = 2
            click = 0
        if keys[pygame.K_3]:
            icon = 3
            click = 0
        if keys[pygame.K_d]:
            click = 0
            icon = 0

        # Placer des tours 
        if pygame.mouse.get_pressed()[0]:
            if int(gameVar.get("click", 0)) == 0:
                if int(gameVar.get("icon", 0)) == 1 and int(gameVar.get("money", 0)) >= 300 and int(gameVar.get("place", 0)) == 0:  # Voir si on a assez d'argent et si on peut placer ou pas
                    t1 = Tour(mx, my)
                    Tours1.append(t1)
                    money = int(gameVar.get("money", 0)) - 300
                if int(gameVar.get("icon", 0)) == 2 and int(gameVar.get("money", 0)) >= 500 and int(gameVar.get("place", 0)) == 0:
                    t2 = Tour2(mx, my)
                    Tours2.append(t2)
                    money = int(gameVar.get("money", 0)) - 500
                click = 1

                if int(gameVar.get("icon", 0)) == 3 and int(gameVar.get("money", 0)) >= 1000 and int(gameVar.get("place", 0)) == 0:
                    t3 = Tour3(mx, my)
                    Tours3.append(t3)
                    money = int(gameVar.get("money", 0)) - 1000
                click = 1

        # Voir si le placement de la tour est valide
        if mouserect.colliderect(trackrect1) or mouserect.colliderect(trackrect2) or mouserect.colliderect(
                trackrect3) or mouserect.colliderect(trackrect4) or mouserect.colliderect(
                trackrect5) or mouserect.colliderect(menurect1) or mouserect.colliderect(
                menurect2) or mouserect.colliderect(menurect3) or mouserect.colliderect(
                menurect4) or mouserect.colliderect(menurect5) or mouserect.colliderect(menurect6):
            place = 1
        else:
            place = 0

        for t1 in Tours1:  # S'assurer qu'on ne peut pas placer une tour sur une autre
            if t1.hitTest(mx, my):
                place = 1

        for t2 in Tours2:
            if t2.hitTest(mx, my):
                place = 1

        for t3 in Tours3:
            if t3.hitTest(mx, my):
                place = 1

        # Vendre tours
        if pygame.mouse.get_pressed()[
            2]:  # Si on clique sur CliqueDroit sur la tour on peut la remove et recevoir du gold
            for t1 in Tours1:
                if t1.hitTest(mx, my):
                    money = money + 200
                    Tours1.remove(t1)

        if pygame.mouse.get_pressed()[2]:
            for t2 in Tours2:
                if t2.hitTest(mx, my):
                    money = money + 350
                    Tours2.remove(t2)

        if pygame.mouse.get_pressed()[2]:
            for t3 in Tours3:
                if t3.hitTest(mx, my):
                    money = money + 750
                    Tours3.remove(t3)

        # Suivre l'image de la tour avec le curseur 
        if click != 1 and icon == 1:  # Suivre l'icône de la tour jusqu'au curseur pendant la phase de placement
            screen.blit(tower1, (mx - 25, my - 25))
            renderedText = font1.render("Tour Rafalle", 1, white)
            screen.blit(renderedText, (545, 600))
            renderedText = font1.render("Appuyez sur D pour deselectionner", 1, white)
            screen.blit(renderedText, (500, 90))
            renderedText = font1.render("Prix: $300           Range: Elevee           Damage: Bas", 1, white)
            screen.blit(renderedText, (250, 640))
            renderedText = font1.render("Degats groupes mais tires lentement et rates frequemment", 1, white)
            screen.blit(renderedText, (220, 680))
            if place == 0:
                pygame.draw.circle(screen, green, [mx, my], 300,
                                   1)  # Si le placement est valide et qu'il y a suffisamment de gold, le cercle devient vert
            if place == 1 or int(gameVar.get("money", 0)) < 300:
                pygame.draw.circle(screen, red, [mx, my], 300,
                                   1)  # Si le placement n'est pas valide ou s'il n'y a pas suffisamment de gold, le cercle devient rouge

        if click != 1 and icon == 2:
            screen.blit(tower2, (mx - 25, my - 25))
            renderedText = font1.render("Appuyez sur D pour deselectionner", 1, white)
            screen.blit(renderedText, (500, 90))
            renderedText = font1.render("Canon Laser", 1, white)
            screen.blit(renderedText, (545, 600))
            renderedText = font1.render("Prix: $500           Range: Bas           Damage: Elevee", 1, white)
            screen.blit(renderedText, (250, 640))
            renderedText = font1.render("Ne rates pas et tires rapidement", 1, white)
            screen.blit(renderedText, (400, 680))
            if place == 0:
                pygame.draw.circle(screen, green, [mx, my], 150, 1)
            if place == 1 or int(gameVar.get("money", 0)) < 500:
                pygame.draw.circle(screen, red, [mx, my], 150, 1)

        if click != 1 and icon == 3:
            screen.blit(tower3, (mx - 25, my - 25))
            renderedText = font1.render("Appuyez sur D pour deselectionner", 1, white)
            screen.blit(renderedText, (500, 90))
            renderedText = font1.render("Factory", 1, white)
            screen.blit(renderedText, (558, 600))
            renderedText = font1.render("Prix: $1000           Range: None           Damage: None", 1, white)
            screen.blit(renderedText, (235, 640))
            renderedText = font1.render("Génère 75 $ toutes les 5 secondes", 1, white)
            screen.blit(renderedText, (400, 680))
            if place == 0:
                pygame.draw.circle(screen, green, [mx, my], 75, 1)
            if place == 1 or int(gameVar.get("money", 0)) < 500:
                pygame.draw.circle(screen, red, [mx, my], 75, 1)

        # Retire les ennemis et ajoute de l'argent lorsque l'ennemi est touché
        for e1 in enemies1:  # Test de collision entre les balles du Juggernaut et les ennemis (à l'aide d'une fonction dans la classe Enemy)
            for b in bullets:
                if e1.hitTest(b.x, b.y) or e1.hitTest(b.x + b.width, b.y) or e1.hitTest(b.x,
                                                                                        b.y + b.height) or e1.hitTest(
                        b.x + b.width, b.y + b.height):
                    e1.health = e1.health - 1
                    break

        for e1 in enemies1:  # Test de collision entre le laser et les ennemis (à l'aide d'une fonction dans la classe Enemy)
            for l in lasers:
                if e1.hitTest(l.end[0], l.end[1]) or e1.hitTest(l.end[0], l.end[1]) or e1.hitTest(l.end[0], l.end[
                    1]) or e1.hitTest(l.end[0], l.end[1]):
                    e1.health = e1.health - 2
                    lasers.remove(l)
                    break

        for e1 in enemies1:  # Enlever les ennemis et décompter des vies s'ils atteignent la fin
            if e1.x < -30:
                enemies1.remove(e1)
                lives = lives - 1

        # List functions 
        for t1 in Tours1:
            t1.shoot()
            t1.draw()

        for t2 in Tours2:
            t2.shoot()
            t2.draw()

        for t3 in Tours3:
            t3.draw()

        for b in bullets:
            b.draw()
            b.move()
            if b.pos[0] < 0 or b.pos[0] > width or b.pos[1] < 0 or b.pos[
                1] > height:  # Supprimer les balles lorsqu'elles atteignent le bord de la map
                bullets.remove(b)

        for l in lasers:
            l.draw()

        if int(gameVar.get("producecount", 0)) >= 500:  # Gestion du timer pour les factory et fréquence à laquelle elles génèrent de l'argent
            for t3 in Tours3:
                money = money + 75
            producecount = 0

        for e1 in enemies1:
            if e1.health <= 0:  # Supprime les ennemis lorsque leur pv atteint zéro
                enemies1.remove(e1)
                money = money + 2
            e1.draw()
            e1.move()

        # Compteurs d'apparition des ennemis
        if int(gameVar.get("enemycount", 0)) % int(gameVar.get("alienspacing", 30)) == 0 and int(gameVar.get("spawncount", 0)) < int(gameVar.get("numaliens", 0)):  # Alienspacing correspond à la fréquence d'apparition d'un ennemi, tandis que spawncount indique combien sont générés
            e1 = Enemy1(1300, 162)
            enemies1.append(e1)
            spawncount = int(gameVar.get("spawncount", 0)) + 1 # Combien d'extraterrestres ont été générés dans cette vague
            empty = 0

        if len(enemies1) <= 0 and empty == 0:  # Fin de la vague 
            hlth = hlth + 4  # Increase Health
            healthspacing = healthspacing + 2  # Augmenter l'espacement pour la barre de santé (dans la classe Enemy)
            money = money + 250  # Add Money
            spawncount = 0
            if numaliens < 65:  # Ajouter plus d'ennemis jusqu'à 65 (pour que les vagues ne soient pas trop longues)
                numaliens = numaliens * 1.5
            if alienspacing > 5:  # Réduire l'espacement des extraterrestres lors de leur apparition  (afin qu'ils ne forment pas une masse  dense)
                alienspacing = alienspacing - 1
            if spd < 10:  # Rendre les ennemis plus rapides jusqu'à une limite (pour éviter qu'ils ne contournent les rectangles de barrière)
                spd = spd + 2  
            empty = 1  
            wave = wave + 1  # Changer le compteur de vague en haut de l'écran

        if int(gameVar.get("enemycount", 0)) >= 100:  # déterminer la fréquence d'apparition des ennemis
            enemycount = 0

        if int(gameVar.get("lives", 0)) <= 0:  # Check si Game Over
            lose.lose(wave)

        # Compteurs 
        enemycount = int(gameVar.get("enemycount", 0)) + 1
        producecount = int(gameVar.get("producecount", 0)) + 1


        # Rendus/Affichages
        renderedText = font1.render("$" + str(int(gameVar.get("money", 0))), 1, white, )  # Gold
        screen.blit(renderedText, (10, 10))
        renderedText = font1.render("PV: " + str(int(gameVar.get("lives", 0))), 1, white, )  # PV
        screen.blit(renderedText, (1100, 10))
        renderedText = font1.render("Wave: " + str(int(gameVar.get("waves", 0))), 1, white, )  # Vague
        screen.blit(renderedText, (600, 10))
        pygame.display.flip()
        pygame.time.delay(10)  # FPS
        # Fin de Game Loop