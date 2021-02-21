# -*- coding: utf-8 -*-

import pygame
import sys
from module1 import *
from but import *
from main1 import * #main
from item import *
from excel import *
# import Sound_controll, sound2
# 방 import 하는 곳 (지도상에서 붙어있는 방 알아서 전부 import 해주길 바람)
import loading2
import security_room

import time
import Sound_controll
import sound

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
            t1.reset("바닥이 흙인 것 같다.")
        if scr == 3: 
            t1.reset("이동목록")
        ch = 0

#                       *중요*
# 1. sheetname을 파일 이름으로 예시) sp3.py 면 'sp3'
#    + itemo.xlsx에 파일 이름으로 시트를 추가해야함 (.py 빼고)
# 2. 방을 이어지게(파일 오가기) 하고 싶다면 알아서 임포트 하고
#    방이름(파일이름).maprun() 으로 다른 방으로 이동
# 3. 변수 선언은 반드시 maprun함수 안에 해야함(지역변수 문제 때문)
# 4. 대사 출력은 setscr(a), 대사들은 textls 안에 알아서 만들기
btn_on = False

def maprun():
    global scr
    global ch
    global run
    global btn_on
    # 버튼 만드는 곳
    # variable(버튼이름) = button(text, width, height, x좌표, y좌표)
    # variable.draw() // 버튼을 화면에 출력
    # variable.check() // 버튼 위에 마우스가 있다면 1, 아니면 0출력
    # variable.color = (R,G,B) // 버튼 색 설정
    # variable.textcolor = (R,G,B) // 텍스트 색 설정
    # variable.textsize = (텍스트사이즈)

    sheetname = 'sp2' # 엑셀파일에 자신이 원하는 방의 이름을 시트로 추가 (건드려야할 것)
    
    floor_button.item = [sheetname, 1] # 엑셀파일의 'sp2'시트의 1번째 가로줄을 할당

    # objectname = itemobject(사진파일, 개체이름, x크기, y크기, x좌표, y좌표)
    # 활용 예시 (아래 참고)
    # box = itemobject('box.png', '박스', width, height, x, y)
    # box.item = [sheetname, 1] # sheetname은 미리 지정해야함 / 1은 1번째 가로줄을 의미

    # | 여기부터 자유롭게 추가 |
    holy = itemobject("light2.png", "빛", 100, 100, 200, 200) # 예시
    holy.item = [sheetname, 2] # 엑셀파일의 'sp2'시트의 2번째 가로줄을 할당

    test_button = button("테스트", 100, 50, 750, 400)
    run = True

    btn = button("SECURITY ROOM", 230, 30, (screen_width/2 + 195), (screen_height/2) - 180)
    btn.check()
    btn.textsize = (20)
    btn.color = (30, 30, 30)
    btn.size = (20)

    #sound.py모듈을 불러와 cynthia.mp3출력
    sound.play_cynthia_S()

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

        clicked = btn.clicking()
        
        # // All_event [이벤트창]

        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            run = False
        # // Mouse_click
        if event.type == pygame.MOUSEBUTTONDOWN:
            buttoncheck() # [삭제하면 안되는 것]
            itemcheck(holy)

        # if pygame.key.get_pressed()[pygame.K_q]:
        #     sp3.game_over()

        exploration = button("집중 탐사", 100, 50, 650, 500)
        exploration.color = (255,255,255)
        exploration.textcolor = (000,000,000)
        exploration.textsize = (20)
        exploration.draw()
        clicked5 = exploration.clicking()
        if clicked5 == True:
            setscr(1)

        see = button("바닥 보기", 100, 50, 850, 500)
        see.color = (255,255,255)
        see.textcolor = (000,000,000)
        see.textsize = (20)
        see.draw()
        see.check()
        clicked1 = see.clicking()
        if clicked1 == True:
            setscr(2)

        way = button("이동 목록", 100, 40, 750, 360)
        way.color = (255,255,255)
        way.textcolor = (000,000,000)
        way.textsize = (20)
        way.draw()
        way.check()
        clicked2 = button.on()

        if clicked2 == True:
            setscr(3)
            security_room.maprun()

        if pygame.key.get_pressed()[pygame.K_e]:
            # security_room.maprun()
            pass

        if pygame.key.get_pressed()[pygame.K_m]:
            Sound_controll.sound_controll()
        #fin [끝]
        # screen.blit(text_Title,((screen_width/2) + 195, (screen_height/2) - 200))
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

