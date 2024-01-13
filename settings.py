import pygame

WIDTH = 800
HEIGHT = 600

#Player
player_img = pygame.image.load('Character.png')
player_img_size = pygame.transform.scale(player_img, (200, 325))
playerX = 0
playerY = 0
PLAYER_SPEED = 5.5