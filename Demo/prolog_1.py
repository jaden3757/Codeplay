import pygame
import sys
from module1 import *
from but import *
from main1 import * #main
from item import *
from excel import *
import loading2
import security_room
import time
import Sound_controll
import sound
import time
import prolog_2

screen_width = 1000
screen_height = 600

LIGHT_BLACK = (50, 50, 50)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DARK_WHITE = (180, 180, 180)
GREEN = (100, 255, 100)
RED = (255, 50, 50)
LIGHT_BLACK = (50, 50, 50)

# 시작
pygame.init() 
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Moon Side")
clock = pygame.time.Clock()
run = True

# 텍스트관련 [삭제하지 말것]
def fadeout(width, height): 
    fade = pygame.Surface((width, height))
    fade.fill((0,0,0))
    for alpha in range(0, 255):
        fade.set_alpha(alpha)
        screen.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(5)

def fadein(width, height): 
    fade = pygame.Surface((width, height))
    fade.fill((0,0,0))
    for alpha in range(0, 255):
        fade.set_alpha(alpha - 254)
        screen.blit(fade, (0,0))
        pygame.display.update()
        # pygame.time.delay(5)

on = False

def maprun():
    global on

    move_button = button("Next", 80, 30, 900, 545)
    move_button.color = (70,70,70)
    move_button.textcolor = (0,0,0)
    move_button.textsize = 22
    move_button.font = 'pixel.ttf'

    sound.play_planets_S()

    run = True

    image2 = pygame.image.load("images/prolog1.png") # 임시 파일
    image2 = pygame.transform.scale(image2, (1000, 600))

    while run:
        # 세팅 [ 건드리지 말아야 할 것]
        screen.fill(pygame.color.Color(50, 50, 50))
        primg2("images/prolog1.png", 0, 0)
        # fadein(1000, 800)

        # myFont = pygame.font.SysFont( "arial", 30, True, False)
        # text_Title= myFont.render("Click to continue!", True, BLACK)
        # screen.blit(text_Title, (700, 450))

        move_button.draw()

        # | 이벤트 관리소 |
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            run = False
        # // Mouse_click
        if event.type == pygame.MOUSEBUTTONDOWN:
            buttoncheck() # [삭제하면 안되는 것]

        if pygame.mouse.get_pressed()[0] == 1:
            if move_button.check():
                on = True
                print("hello")

        if on == True:
            fadeout(1000, 800)
            # screen.blit(text_Title, (650, 450)
            prolog_2.maprun()

        #fin [끝]
        mousechange()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    maprun()