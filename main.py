import pygame
import constants
from hero import Hero
from weapon import Weapon
pygame.init()

screen = pygame.display.set_mode((constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT))
pygame.display.set_caption("Dungeon Crawler")
#create clock for maintaing frame rate
clock = pygame.time.Clock()

#define player movement variable
moving_up= False
moving_down= False
moving_left= False
moving_right= False

#helper to scale image
def scale_img(image, scale):
    w = image.get_width()
    h= image.get_height()
    return pygame.transform.scale(image, (w*scale, h*scale))


#load weapon images
bow_image = scale_img(pygame.image.load("assets/images/weapons/bow.png").convert_alpha(), constants.WEAPON_SCAPE)
arrow_image = scale_img(pygame.image.load("assets/images/weapons/arrow.png").convert_alpha(), constants.WEAPON_SCAPE)


#load character images
mob_animations = []
mob_types= ["elf","imp","skeleton","goblin","muddy","tiny_zombie","big_demon"]

animation_types = ["idle", "run"]
for mob in mob_types:
    #load images
    animation_list = []
    for animation in animation_types:
        #reset temporary list of images
        temp_list = []
        for i in range(4):
            img = pygame.image.load(f"assets/images/characters/{mob}/{animation}/{i}.png").convert_alpha()
            img = scale_img(img,constants.SCALE)
            temp_list.append(img)
        animation_list.append(temp_list)
    mob_animations.append(animation_list)

#create player
player = Hero(100,100, mob_animations, 0)


#players weapon
bow = Weapon(bow_image)

#main game loop
game = True
while game:
    #control frame rate
    clock.tick(constants.FPS)
    screen.fill(constants.BG)
    #calculate player movement d - delta
    dx= 0
    dy= 0
    if moving_up == True:
        dy = -constants.SPEED
    if moving_down ==True:
        dy= constants.SPEED
    if moving_right == True:
        dx= -constants.SPEED
    if moving_left ==True:
        dx = constants.SPEED


    #move player
    player.move(dx,dy)
    #update player
    player.update()
    bow.update(player)

    #draw player
    player.draw(screen)
    bow.draw(screen)

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        #take keyboard presses
        if event.type == pygame.KEYDOWN:
            if event.key ==pygame.K_w:
                moving_up = True
            if event.key ==pygame.K_s:
                moving_down =True
            if event.key ==pygame.K_a:
                moving_right =True
            if event.key ==pygame.K_d:
                moving_left =True
        #keyboard button release
        if event.type == pygame.KEYUP:
            if event.key ==pygame.K_w:
                moving_up = False
            if event.key ==pygame.K_s:
                moving_down =False
            if event.key ==pygame.K_a:
                moving_right =False
            if event.key ==pygame.K_d:
                moving_left =False

    pygame.display.update()
pygame.quit()
