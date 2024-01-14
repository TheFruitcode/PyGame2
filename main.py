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

#background
bg = pygame.transform.scale(pygame.image.load('grass.png').convert(), (WIDTH, HEIGHT))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.pos = pygame.math.Vector2(playerX, playerY)
        self.speed = PLAYER_SPEED

    def user_input(self):
        self.velocity_X = 0
        self.velocity_Y = 0

        keys = pygame.key.get_pressed()
    
        if keys[pygame.K_w]:
            self.velocity_Y = -self.speed
            screen.blit(player_img_size4, player.pos)
            STANDING = False
        if keys[pygame.K_s]:
            self.velocity_Y = self.speed
            screen.blit(player_img_size, player.pos)
            STANDING = False
        if keys[pygame.K_a]:
            self.velocity_X = -self.speed
            screen.blit(player_img_size2, player.pos)
            STANDING = False
        if keys[pygame.K_d]:
            self.velocity_X = self.speed
            screen.blit(player_img_size3, player.pos)
            STANDING = False
    
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
    
    screen.blit(player_img_size, player.pos)

    player.update()

    clock.tick(60)

    pygame.display.update()