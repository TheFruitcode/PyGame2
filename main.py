import pygame
import time
import sys
import random
import os

pygame.init()

display = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Adventure of Thorsten")


clock = pygame.time.Clock()


#Player
player_img = pygame.image.load('Character.png')
player_img_size = pygame.transform.scale(player_img, (200, 325))
playerX = 0
playerY = 0

#tree_img = pygame.image.load('C:\Users\Falco\Desktop\PyGame2', 'TREE 1 - DAY.png')

def player():
    display.blit(player_img_size, (playerX, playerY))
    #pygame.draw.rect(display, "red", (self.x, self.y, self.width, self.height))
    #self.image = pygame.image.load(player_img)
    
#def background(self, surface):
    #bg = os.path.join('C:\Users\Falco\Desktop\PyGame2', 'grass.png')
    #self.image2 = pygame.image.load(bg)
    #surface.blit(self.image2, (0,0))

#class Tree(object):
#    def __init__(self, x=640, y=0, dist=2):
#        #self.image = pygame.image.load(tree_img)
#        self.x = x
#        self.y = y
#        self.dist = dist
#        
#        def rock(self):
#            self.x -= dist
#    
#    def rock_draw(self, surface):
#        surface.blit(self.image, (self.x, self.y))

#y = random.randint(0, 400)
#tree = Tree(640, y)

#tree = Tree

while True:
    display.fill((24,164,86))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player.playerY -= 5
    if keys[pygame.K_s]:
        player.playerY += 5
    if keys[pygame.K_a]:
        player.playerX -= 5
    if keys[pygame.K_d]:
        player.playerX += 5

    #player.main(display)

    player()

    clock.tick(60)

    pygame.display.update()