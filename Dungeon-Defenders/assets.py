import pygame

pygame.init()

size = width, height = 1280, 720
screen = pygame.display.set_mode(size,pygame.SHOWN)

# Chargez les images
tower1 = pygame.image.load("res/towerimg1.gif")
tower2 = pygame.image.load("res/towerimg2.gif")
tower3 = pygame.image.load("res/towerimg3.gif")
backround = pygame.image.load("res/Arriere-plan.gif")

# Fonts
font1 = pygame.font.Font("res/pixelmix.ttf", 23)
font2 = pygame.font.Font("res/pixelmix_bold.ttf", 90)
font3 = pygame.font.Font("res/pixelmix_bold.ttf", 50)
font4 = pygame.font.Font("res/pixelmix_bold.ttf", 48)
font5 = pygame.font.Font("res/pixelmix_bold.ttf", 75)

# Barriers 
barrierleftrect = pygame.Rect(978, 524, 150, 50)  # Directions des aliens
barrierrightrect = pygame.Rect(220, 360, 50, 50)
barrierdownrect = pygame.Rect(185, 150, 50, 50)
barrierdownrect2 = pygame.Rect(1045, 320, 1000, 50)
trackrect1 = pygame.Rect(229, 159, 1030, 40)  # Montres ou les tours ne peuvent pas etre placees
trackrect2 = pygame.Rect(229, 170, 40, 175)
trackrect3 = pygame.Rect(229, 328, 822, 40)
trackrect4 = pygame.Rect(1010, 330, 40, 199)
trackrect5 = pygame.Rect(0, 489, 1030, 40)
menurect1 = pygame.Rect(230, 0, 824, 200)
menurect2 = pygame.Rect(0, 0, 1280, 57)
menurect3 = pygame.Rect(175, 75, 935, 15)
menurect4 = pygame.Rect(230, 583, 824, 200)
menurect5 = pygame.Rect(0, 663, 1280, 57)
menurect6 = pygame.Rect(175, 625, 935, 150)

# Couleurs 
teal = [0, 150, 255]
black = [0, 0, 0]
white = [255, 255, 255]
green = [0, 255, 0]
red = [255, 0, 0]
blue = [0, 0, 255]
orange = [255, 156, 55]

# Listes
enemies1 = []
Tours1 = []
Tours2 = []
Tours3 = []
bullets = []
lasers = []

t1 = None
t2 = None

gameVar={}
with open("game.txt", "r") as game_:
    game = game_.read()
    exec(game, gameVar)
xspeed = int(gameVar.get("xspeed", 0))
yspeed = int(gameVar.get("yspeed", 0))
xpos = int(gameVar.get("xpos", 0))
ypos = int(gameVar.get("ypos", 0))
money = int(gameVar.get("money", 2000))
lives = int(gameVar.get("lives", 10))
click = int(gameVar.get("click", 0))
icon = int(gameVar.get("icon", 0))
place = int(gameVar.get("place", 0))
enemycount = int(gameVar.get("enemycount", 0))
producecount = int(gameVar.get("producecount", 0))
wave = int(gameVar.get("wave", 1))
spawncount = int(gameVar.get("spawncount", 0))
alienspacing = int(gameVar.get("alienspacing", 30))
numaliens = int(gameVar.get("numaliens", 5))
empty = int(gameVar.get("empty", 0))
hlth = int(gameVar.get("hlth", 10))
spd = int(gameVar.get("spd", 3))
healthspacing = int(gameVar.get("healthspacing", -10))