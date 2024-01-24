import pygame

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

    def __init__(self, game, x, y):
        self.x = x #0
        self.y = y #0
        self.speed = 5.5
        self.game = game
        self.surface = game.window

    def update(self):
        self.user_input()
        self.draw()

    def user_input(self):
    #    self.velocity_X = 0
    #    self.velocity_Y = 0

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.STANDING = False
            self.x -= self.speed * self.game.delta_time
            self.game.window.blit(player_img_size4, self.x, self.y)
        #    self.velocity_Y = -self.speed
        else:
            self.STANDING = True
        if keys[pygame.K_s]:
            self.STANDING = False
            self.x += self.speed * self.game.delta_time
            self.game.window.blit(player_img_size, self.x, self.y)
        if keys[pygame.K_a]:
            self.STANDING = False
            self.x -= self.speed * self.game.delta_time
            self.game.window.blit(player_img_size, self.x, self.y)
        if keys[pygame.K_d]:
            self.STANDING = False
            self.x += self.speed * self.game.delta_time
            self.game.window.blit(player_img_size, self.x, self.y)

    def draw(self):
        if self.STANDING == True:
            self.game.window.blit(player_img_size, self.x, self.y)
    
    
#player = Player()

