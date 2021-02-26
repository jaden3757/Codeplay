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

# def fadein(width, height): 
#     fade = pygame.Surface((width, height))
#     fade.fill((0,0,0))
#     for alpha in range(0, 255):
#         fade.set_alpha(255-alpha)
#         # screen.blit(fade, (0,0))
#         pygame.display.update()
#         pygame.time.delay(5)


# def maprun():
#     move_button = button("Next", 80, 50, 750, 500)
#     move_button.color = (50,50,50)
#     move_button.textcolor = (0,0,0)
#     move_button.textsize = 22
#     move_button.font = 'pixel.ttf'

#     move1_button = button("Next", 80, 50, 750, 500)
#     move1_button.color = (50,50,50)
#     move1_button.textcolor = (0,0,0)
#     move1_button.textsize = 22
#     move1_button.font = 'pixel.ttf'

#     run = True

#     images = ["images/hole.jpg", "teaser-5.png"]

#     while run:
#         # 세팅 [ 건드리지 말아야 할 것]
#         # screen.fill(pygame.color.Color(50, 50, 50))
#         # main [여기에 코드 입력] > 이미지 오브젝트, 텍스트(prtext) 등등
#         primg2("images/hole.jpg", 0, 0)

#         # | 이벤트 관리소 |

#         event = pygame.event.poll()
#         if event.type == pygame.QUIT:
#             run = False

#         # move_button.draw()
#         # if move_button.check():
#         #     if pygame.mouse.get_pressed()[0] == 1:
#         #         print("Hello")
#         #         time.sleep(0.5)
#         #         primg2(images[0], 0, 0)
#         #         fadeout(1000, 600)
        
#         move1_button.draw()
#         if move1_button.check():
#             if pygame.mouse.get_pressed()[0] == 1:
#                 for i in range(0, 2):
#                     print("Hello")
#                     # fadeout(1000, 600)
#                     # time.sleep(0.5)
#                     primg2(images[i], 0, 0)

#         # // Mouse_click
#         #fin [끝]

#         pygame.display.flip()
#         clock.tick(60)

#     pygame.quit()

# if __name__ == '__main__':
#     maprun()

# -*- coding: utf-8 -*-
on = False

def maprun():
    global on

    move_button = button("Next", 100, 50, 800, 500)
    move_button.color = (255,255,255)
    move_button.textcolor = (0,0,0)
    move_button.textsize = 22
    move_button.font = 'pixel.ttf'

    move1_button = button("Next", 100, 50, 800, 500)
    move1_button.color = (255,255,255)
    move1_button.textcolor = (0,0,0)
    move1_button.textsize = 22
    move1_button.font = 'pixel.ttf'

    sound.play_cynthia_S()
    run = True

    image = pygame.image.load("teaser-5.png")
    image2 = pygame.image.load("images/hole.jpg")

    sound.play_Moodside_S()

    while run:
        # 세팅 [ 건드리지 말아야 할 것]
        screen.fill(pygame.color.Color(50, 50, 50))
        primg2("images/hole.jpg", 0, 0)

        myFont = pygame.font.SysFont( "arial", 30, True, False)
        text_Title= myFont.render("Click to continue!", True, BLACK)
        screen.blit(text_Title, (700, 450))

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
            primg2("teaser-5.png", 0, 0)
            move1_button.draw()
            screen.blit(text_Title, (650, 450))
            if move1_button.clicking():
                loading2.maprun()

        #fin [끝]
        mousechange()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    maprun()