# -*- coding: utf-8 -*-

import pygame
import sys
from module1 import *
from but import *
from main1 import * #main
from item import *
from tkinter import *
# from sp3 import *
import sp3
import sp6
import Sound_controll

# 시작
pygame.init() 
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Moon Side")
clock = pygame.time.Clock()

LIGHT_BLACK = (50, 50, 50)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DARK_WHITE = (180, 180, 180)
GREEN = (100, 255, 100)
RED = (255, 50, 50)
LIGHT_BLACK = (50, 50, 50)

# 텍스트관련 [삭제하지 말것]
scr = 0
ch = 1

def setscr(script): # setscr(a) a번째 대사 출력 
    global ch
    global scr
    scr = script
    ch = 1

def textls(): # 텍스트 수동 입력
    global ch
    global scr
    if ch == 1:
        if scr == 0: # 0번째 대사(시작시 무조건 출력)
            t1.reset("> 샘플 맵입니다")
            t1.next("[ 인벤토리 열기 : 우측 하단 I 버튼 ]")
        if scr == 1: # 1번째 대사
            t1.reset("..")
        if scr == 2: # 2번째 대사 [이 아래에 더 추가 가능]
            t1.reset("..")
        ch = 0



def room1():
    holy = itemobject("light2.png", "빛", 100, 100, 200, 200)
    run = True

    sound = ("Cynthia.mp3")
    pygame.mixer.music.load(sound)
    pygame.mixer.music.play(-1)

    while run:
        password = 10293
        # 세팅 [ 건드리지 말아야 할 것]
        screen.fill(pygame.color.Color(50, 50, 50))
        pygame.draw.rect(screen, (20,20,20), [20, 20, 560, 560])
        # main [여기에 코드 입력]
        holy.draw()

        # UI
        prtext2("ROOMNUM | ROOMCODE", 20, 30, 30)
        drawui()
        textls()
        textprinting()
        
        # // All_event [이벤트창]
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            run = False
        # // Mouse_click
        if event.type == pygame.MOUSEBUTTONDOWN:
            buttoncheck() # [삭제하면 안되는 것]
            itemcheck(holy)

        if pygame.key.get_pressed()[pygame.K_q]:
            sp3.game_over()

        if pygame.key.get_pressed()[pygame.K_e]:
            sp6.security_room()

        if pygame.key.get_pressed()[pygame.K_m]:
            Sound_controll.sound_controll()
        
        #fin [끝]
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


room1()
