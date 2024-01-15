import pygame
import math
import time
import sys
import random
import os
from settings import *

pygame.init()


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Adventure of Thorsten")
clock = pygame.time.Clock()

#Player
player_img = pygame.image.load('Character.png')
player_img_size = pygame.transform.scale(player_img, (200, 325))
player_img2 = pygame.image.load('Character2.png')
player_img_size2 = pygame.transform.scale(player_img2, (200, 325))
player_img3 = pygame.image.load('Character3.png')
player_img_size3 = pygame.transform.scale(player_img3, (200, 325))
player_img4 = pygame.image.load('Character4.png')
player_img_size4 = pygame.transform.scale(player_img4, (200, 325))

#Tree
tree = pygame.image.load('TREE_DAY.png')
tree_size = pygame.transform.scale(tree, (250, 375))
tree_anzahl = 6

#background
bg = pygame.transform.scale(pygame.image.load('grass.png').convert(), (WIDTH, HEIGHT))

class Player(pygame.sprite.Sprite):
    STANDING = True

    def __init__(self):
        super().__init__()
        self.pos = pygame.math.Vector2(playerX, playerY)
        self.speed = PLAYER_SPEED

    def user_input(self):
        self.velocity_X = 0
        self.velocity_Y = 0

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            player.STANDING = False
            self.velocity_Y = -self.speed
            screen.blit(player_img_size4, player.pos)
        else:
            player.STANDING = True
        if keys[pygame.K_s]:
            player.STANDING = False
            self.velocity_Y = self.speed
            screen.blit(player_img_size, player.pos)
        if keys[pygame.K_a]:
            player.STANDING = False
            self.velocity_X = -self.speed
            screen.blit(player_img_size2, player.pos)
        if keys[pygame.K_d]:
            player.STANDING = False
            self.velocity_X = self.speed
            screen.blit(player_img_size3, player.pos)

    def move(self):
        self.pos += pygame.math.Vector2(self.velocity_X, self.velocity_Y)

    def update(self):
        self.user_input()
        self.move()
player = Player()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
    screen.blit(bg, (0,0))
    
    if player.STANDING == True:
        screen.blit(player_img_size, player.pos)

    for x in range(tree_anzahl):
        x = random.randint(0, WIDTH - 50)
        y = random.randint(0, HEIGHT - 50)
        screen.blit(tree_size, (x, y))

    player.update()

    clock.tick(60)
    pygame.display.update()