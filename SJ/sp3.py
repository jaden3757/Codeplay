# -*- coding: utf-8 -*-

import pygame
import sys
from module1 import *
from but import *
from main1 import * #main
from item import *
# from sp2 import *
import sp2
import sp6
import Sound_controll

LIGHT_BLACK = (50, 50, 50)
# 시작
pygame.init() 
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Moon Side")
clock = pygame.time.Clock()
run = True

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

# 버튼 만드는 곳
# variable(버튼이름) = button(text, width, height, x좌표, y좌표)
# variable.draw() // 버튼을 화면에 출력
# variable.check() // 버튼 위에 마우스가 있다면 1, 아니면 0출력
# variable.color = (R,G,B) // 버튼 색 설정
# variable.textcolor = (R,G,B) // 텍스트 색 설정
# variable.textsize = (텍스트사이즈)

# objectname = itemobject(사진파일, 개체이름, x크기, y크기, x좌표, y좌표)
# holy = itemobject("light2.png", "빛", 100, 100, 200, 200)

def game_over():
    global BLACK
    global LIGHT_BLACK
    sound = ("C:\\Users\\정성환\\Desktop\\pythonworkspace\\Pygame\\pygame_info\\Planets.mp3")

    pygame.mixer.music.load(sound)

    pygame.mixer.music.play(-1)

    run = True
    
    while run:
        # 세팅 [ 건드리지 말아야 할 것]
        # screen.fill(pygame.color.Color(50, 50, 50))
        # pygame.draw.rect(screen, (20,20,20), [20, 20, 560, 560])
        # main [여기에 코드 입력]
        # holy.draw()

        # UI
        # prtext2("ROOMNUM | ROOMCODE", 20, 30, 30)
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
            # itemcheck(holy)

        if pygame.key.get_pressed()[pygame.K_w]:
            sp2.room1()

        if pygame.key.get_pressed()[pygame.K_e]:
            sp6.security_room()
        
        if pygame.key.get_pressed()[pygame.K_m]:
            Sound_controll.sound_controll()

        screen.fill(LIGHT_BLACK)

        myFont = pygame.font.SysFont( "microsoftphagspa", 50, True, False)
        text_Title_yes= myFont.render("Game Over", True, BLACK)
        screen.blit(text_Title_yes, (int(screen_width / 2) - 140, int(screen_height) / 2 - 100))
        #fin [끝]
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()