import pygame
import time
import sys
import random
import os

pygame.init()

WIDHT, HEIGHT = 800, 600
display = pygame.display.set_mode((WIDHT, HEIGHT))
pygame.display.set_caption("Adventure of Thorsten")
clock = pygame.time.Clock()

running = True

player_img = os.path.join('C:\Users\Falco\Desktop\PyGame2', 'player.png')
tree_img = os.path.join('C:\Users\Falco\Desktop\PyGame2', 'TREE 1 - DAY.png')

class Player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        #pygame.draw.rect(display, "red", (self.x, self.y, self.width, self.height))
        self.image = pygame.image.load(player_img)


def handle_keys(self):
    keys = pygame.key.get_pressed()
    dist = 3
    if keys[pygame.K_w]:
        self.y -= dist
    if keys[pygame.K_s]:
        self.y += dist
    if keys[pygame.K_a]:
        self.x -= dist
    if keys[pygame.K_d]:
        self.x += dist

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
    
    def background(self, surface):
        bg = os.path.join('C:\Users\Falco\Desktop\PyGame2', 'grass.png')
        self.image2 = pygame.image.load(bg)
        surface.blit(self.image2, (0,0))

class Tree(object):
    def __init__(self):
        self.image = pygame.image.load(tree_img)
        self.x = 640
        self.y = 0
    def rock(self):
        dist = 2
        if running == Tree:
            self.x -= dist
    
    def rock_draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

tree = Tree
player = Player

while running:
    display.fill((24,164,86))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

    player.handle_keys()
    tree.tree()

    player.main(display)

    clock.tick(60)
    
    player.background(display)
    player.draw(display)
    tree.rock_draw(display)
    pygame.display.update()