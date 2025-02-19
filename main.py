#Author: Jared Winkens

#Imports
import pygame
from pygame.locals import *
import sys
from main_menu import MainMenu
from person import Person
from image_loader import SpriteSheetLoader

pygame.init()
FPS = 30
FramePerSec = pygame.time.Clock()
info = pygame.display.Info()
SCREEN_WIDTH = info.current_w * 0.8
SCREEN_HEIGHT = info.current_h * 0.8

window = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("My Game")
main_menu = MainMenu(window)
display_menu = True

walk_imgs = SpriteSheetLoader().load("__assets__/player/walk/",(300,300))
idle_imgs = SpriteSheetLoader().load("__assets__/player/idle/",(300,300))
player = Person(walk_imgs, idle_imgs, (SCREEN_WIDTH*0.5,SCREEN_HEIGHT*0.5))

# Game Loop
while True:
    if display_menu == True: main_menu.show()
    else: 
        window.fill((245,245,220))
        player.draw(window)
        player.move(window)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            display_menu = True
            
    if main_menu.start_button.is_pressed():
        display_menu = False
        
    if main_menu.quit_button.is_pressed():
        pygame.quit()
        sys.exit()
        
    pygame.display.update()
    FramePerSec.tick(FPS)