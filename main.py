import pygame
import math
import time
import sys
import random
import os
import player
import tree

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

            bg = pygame.transform.scale(pygame.image.load('grass.png').convert(), (game.window_width, game.window_height))
            Game.window.blit(bg, (0,0))

            #tree.update()
            #player.update()

            self.delta_time = self.clock.tick(60)
            pygame.display.update()
        
        pygame.quit()
    
game = Game()