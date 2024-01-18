import pygame
import math
import time
import sys
import random
import os
from player import *
from tree import *

class Game:
    def __init__(self):
        pygame.init()
        self.window_width = 1500
        self.window_height = 1000
        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption("Adventure of Thorsten")
        self.clock = pygame.time.Clock()
        self.run()

    def run(self):
        running = True
        while running == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

            if player.STANDING == True:
                Game.window.blit(player_img_size, player.pos)

            if tree.TREE_SPAWNING == True:	
                for i in range(tree_anzahl):
                    Game.window.blit(tree_size, (tree.x, tree.y))
                    tree.TREE_SPAWNING = False

            bg = pygame.transform.scale(pygame.image.load('grass.png').convert(), (Game.window_width, Game.window_height))
            Game.window.blit(bg, (0,0))

            tree.update()
            player.update()

            Game.clock.tick(60)
            pygame.display.update()
        
        pygame.quit()
    
game = Game()