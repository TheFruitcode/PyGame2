import pygame
from main import *

#Tree
tree = pygame.image.load('TREE_DAY.png')
tree_size = pygame.transform.scale(tree, (180, 280))
tree_anzahl = 4

class Tree(pygame.sprite.Sprite):
    TREE_SPAWNING = False
    def update(self):
        self.x = random.randint(0, Game.window_width - 50)
        self.y = random.randint(0, Game.window_height - 50)
        tree.TREE_SPAWNING = True

    #if tree.TREE_SPAWNING == True:	
    #    for i in range(tree_anzahl):
    #        Game.window.blit(tree_size, (tree.x, tree.y))
    #        tree.TREE_SPAWNING = False
tree = Tree()