import pygame
from main import *

#Player
player_img = pygame.image.load('Character.png')
player_img_size = pygame.transform.scale(player_img, (200, 325))
player_img2 = pygame.image.load('Character2.png')
player_img_size2 = pygame.transform.scale(player_img2, (200, 325))
player_img3 = pygame.image.load('Character3.png')
player_img_size3 = pygame.transform.scale(player_img3, (200, 325))
player_img4 = pygame.image.load('Character4.png')
player_img_size4 = pygame.transform.scale(player_img4, (200, 325))

class Player():
    STANDING = True

    def __init__(self):
        self.x = 0
        self.y = 0
        self.speed = 5.5

    def user_input(self):
        self.velocity_X = 0
        self.velocity_Y = 0

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            player.STANDING = False
            self.velocity_Y = -self.speed
            Game.window.blit(player_img_size4, player.pos)
        else:
            player.STANDING = True
        if keys[pygame.K_s]:
            player.STANDING = False
            self.velocity_Y = self.speed
            Game.window.blit(player_img_size, player.pos)
        if keys[pygame.K_a]:
            player.STANDING = False
            self.velocity_X = -self.speed
            Game.window.blit(player_img_size2, player.pos)
        if keys[pygame.K_d]:
            player.STANDING = False
            self.velocity_X = self.speed
            Game.window.blit(player_img_size3, player.pos)

    def move(self):
        self.pos += pygame.math.Vector2(self.velocity_X, self.velocity_Y)

    def update(self):
        self.user_input()
        self.move()

player = Player()

