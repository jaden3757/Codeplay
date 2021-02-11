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
            t1.reset('2030년 이전부터 정부A는 지속적인 달 탐사, 달기지 확장 등의 목적을 위해 달로 사람들을 보내왔다.')
            t1.next('!wait')
            t1.next('그리고 2030년, ') 
            t1.next('!!wait')
            t1.next('연구원A를 포함한 탐사원들이 달로 보내졌다')
        if scr == 1: # 1번째 대사
            t1.reset("..")
            t1.wait = 20
            t2.reset("..")
        if scr == 2: # 2번째 대사 [이 아래에 더 추가 가능]
            t1.reset("..")
            t2.reset("..")
        ch = 0

# 버튼 만드는 곳
# variable(버튼이름) = button(text, width, height, x좌표, y좌표)
# variable.draw() // 버튼을 화면에 출력
# variable.check() // 버튼 위에 마우스가 있다면 1, 아니면 0출력
# variable.color = (R,G,B) // 버튼 색 설정
# variable.textcolor = (R,G,B) // 텍스트 색 설정
# variable.textsize = (텍스트사이즈)

# objectname = itemobject(사진파일, 개체이름, x크기, y크기, x좌표, y좌표)
holy = itemobject("light2.png", "빛", 100, 100, 200, 200)

while run:
    # 세팅 [ 건드리지 말아야 할 것]
    screen.fill(pygame.color.Color(50, 50, 50))
    pygame.draw.rect(screen, (0,0,0), [20, 20, 560, 560])
    prtext2("ROOMNAME | ROOMCODE", 20, 30, 30)
    drawui()
    textls()
    # textprinting()
    # main [여기부터 코드 입력]
    t_surface = screen.convert_alpha()
    t_surface.fill((0,0,0,0))
    pygame.draw.rect(t_surface, (0, 0, 0, 180), [0, 0, 1000, 600])
    screen.blit(t_surface, [0,0])
    textprinting2()

    # // All_event [이벤트창]
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        run = False
    # // Mouse_click
    if event.type == pygame.MOUSEBUTTONDOWN:
        buttoncheck() # [삭제하면 안되는 것]
    if pygame.key.get_pressed()[pygame.K_SPACE]:
        scr += 1
        ch = 1
    #fin [끝]
    pygame.display.flip()
    clock.tick(60)

pygame.quit()