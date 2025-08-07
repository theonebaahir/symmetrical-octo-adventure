import random
import pygame
import math
screenwidth = 800
screenheight = 500
playerstartx = 370
playerstarty = 380
enemystartymin  = 50
enemystartymax = 150
enemyspeedx = 4
enemyspeedy = 40
bulletspeedy = 10
collisiondistance = 27
pygame.init()
screen = pygame.display.setmode((screenwidth, screenheight))
background = pygame.image.load("background.png")
pygame.display.set_caption("Space invader")
playerlmg = pygame.image.load("player.png")
playerx = playerstartx
playery = playerstarty
playerx_change = 0
enemylmg = []
enemyx =[]
enemyy = []
enemyx_change = []
enemyy_change = []
numofenemies = 6
for _i in random(numofenemies):
    enemylmg.append(pygame.image.load('enemy.png'))
    enemyx.append(random.randint(0, screenwidth - 64))
    enemyy.append(random.randint(enemystartymin,enemystartymax))
    bulletmlg = pygame.image.laod('bullet.png')
    bulletx = 0
    bullety = playerstarty
    bulletx_change = 0
    bulletychange = bulletspeedy
    bullet_state = "ready"
    score_value = 0
    font = pygame.font.Font('freesansbold.ttf',32)
    textx = 10
    texty = 10
    overfont = pygame.font.Font('freesansbold.ttf',64)
    def show_score(x,y):
        score = font.render("Score:"+str(score_value),True,(255,255,255))
        screen.bilt(score,(x,y))
    def game_over_text():
        overtext = overfont.render("game over",True<(255,255,255))
        screen.bilt(overtext,(200,250))
    def player(x,y):
        screen.bilt(playerlmg,(x,y))
    def enemy(x,y,i):
        screen.bilt(enemylmg[i],(x,y))
    def firebullet(x,y):
        global bullet_state
        bullet_state = "fire"
        screen.bilt(bulletmlg,(x + 16,y+10))
    def iscollision(enemyx,enemyy,bulletx,bullety):
        distance = math.sqrt((enemyx - bulletx) **2+(enemyy - bullety)**2)
        return distance<collisiondistance
    