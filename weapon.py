import pygame
import math

class Weapon():
    def __init__(self, image):
        self.original_image = image
        self.angle = 0
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect()

    def update(self, player):
        self.rect.center = player.rect.center

        pos = pygame.mouse.get_pos()
        x_dist = pos[0]- self.rect.centerx
        y_dist = -(pos[1] - self.rect.centery)#pygame y coor increase dow the screen
        self.angle = math.degrees(math.atan2(y_dist,x_dist))

        #get mouse click
        if pygame.mouse.get_pressed()[0]:

    def draw(self, surface):
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        surface.blit(self.image, ((self.rect.centerx - int(self.image.get_width()/2)), self.rect.centery - int(self.image.get_height()/2)))

class Arrow(pygame.sprite.Sprite):
    def __init__(self, image, x,y, angle):
        pygame.sprite.Sprite.__init__(self)
        self.original_image = image
        self.angle = angle
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)