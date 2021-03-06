# -*- coding: utf-8 -*-

import pygame
import sys
from module1 import *
from but import *
from main1 import * #main
from item import *

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
            t1.reset("> 생산시설입니다.")
            t1.next("[ 인벤토리 열기 : 우측 하단 I 버튼 ]")
            
        if scr == 1: # 1번째 대사
            t1.reset("중요한건 없는 것 같다.")
        if scr == 2: # 2번째 대사 [이 아래에 더 추가 가능]
            t1.reset("어디로 가시겠습니까? ")


        ch = 0

def maprun():
    global run
    # 버튼 만드는 곳
    # variable(버튼이름) = button(text, width, height, x좌표, y좌표)
    # variable.draw() // 버튼을 화면에 출력
    # variable.check() // 버튼 위에 마우스가 있다면 1, 아니면 0출력
    # variable.color = (R,G,B) // 버튼 색 설정
    # variable.textcolor = (R,G,B) // 텍스트 색 설정
    # variable.textsize = (텍스트사이즈)

    # objectname = itemobject(사진파일, 개체이름, x크기, y크기, x좌표, y좌표)
    holy = itemobject("light2.png", "빛", 100, 100, 200, 200)
    exploration = button("집중 탐사", 100, 50, 650, 500)
    exploration.color = (255,255,255)
    exploration.textcolor = (000,000,000)
    exploration.textsize = (20)

    aaa = button("B보안실", 100, 50, 650, 500)
    aaa.color = (255,255,255)
    aaa.textcolor = (000,000,000)
    aaa.textsize = (20)

    exploration = button("집중 탐사", 100, 50, 650, 500)
    exploration.color = (255,255,255)
    exploration.textcolor = (000,000,000)
    exploration.textsize = (20)
    
    bbb = button("취소", 100, 50, 850, 500)
    bbb.color = (255,255,255)
    bbb.textcolor = (000,000,000)
    bbb.textsize = (20)
    
    see = button("이동 목록", 100, 50, 850, 500)
    see.color = (255,255,255)
    see.textcolor = (000,000,000)
    see.textsize = (20)
    
    mode = 0

    while run:
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

        if mode == 0:
            exploration.on()
            see.on()
        else:
            exploration.off()
            see.off()
        
        if mode == 1:
            aaa.on()
            bbb.on()
        else:
            aaa.off()
            bbb.off()

        exploration.draw()
        see.draw()
        aaa.draw()
        bbb.draw()

        # // Mouse_click
        if event.type == pygame.MOUSEBUTTONDOWN:
            buttoncheck() # [삭제하면 안되는 것]
            itemcheck(holy)
            if exploration.check() == 1:
                setscr(1)
            if see.check() == 1:
                setscr(2)
                mode = 1
            if aaa.check() == 1:
                pass
            if bbb.check() == 1:
                mode = 0
                setscr(0)
        if pygame.key.get_pressed()[pygame.K_m]:
            pass

        #fin [끝]
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()