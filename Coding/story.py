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
            t1.reset('2030년 이전부터 정부A는 지속적인 달 탐사, 달기지 확장 등의 목적을 위해 달로 사람들을 보내왔다. 주인공네 팀이 달에 가기 이전, 정부A의 연구원A가 있는 팀이 달에 갔었다. 연구원A는 달탐사 도중 일반적인 돌과 다르게 생긴 돌이 여러곳에 떨어져있는 것을 보고 돌을 몇개 샘플로 챙겨 달 기지로 복귀한다. 지구로 가져온 이후 자세한 분석과 실험 이후 정부A는 인간에게 치명적인 바이러스가 존재하는 돌인 것을 알게된다. 정부A는 바이러스가 존재하는 돌로 생화확 무기를 대량 생산하기 위해 2030년에 달 기지로 가는 주인공팀에 연구원A를 함께 보내 임무를 수행시키기 위해 다시 달로 보낸다. 달 기지로 가게된 주인공의 팀중 한명인 연구원A는 정부A의 명령대로 혼자 달 탐사를 하게 될 때 여러곳에 떨어져있는 바이러스가 존재하는 돌을 많이 수집한다. 이후 연구원A는 지구에서 가져온 정부의 계략과 연구자료가 적힌 연구노트에다가 연구실에서 돌을 추가로 더 연구하여 기록한다. 지구 복귀 9시간 전, 연구원B는 짐 정리를 위해 꺼내놓은 연구원A가 갖고있던 연구노트를 우연히 읽게된다. 연구원 B는 정부A의 계략을 알게되고 전쟁을 막기 위해 연구원A를 설득한다. 연구원 A는 설득당한 척을 하게 된다. 하지만 연구원A는 지구 복귀 시간이 다가오자, 통신실에서 정부A와 통신을 하여 연구원B가 진실을 말하지 못하게 하기 위하여 사람들이 탑승한 우주선을 폭발시키고 자신은 지하기지에서 정부A의 구조를 기다리기로 통신실에서 명령을 받게 된다. 연구원 A는 정부A의 명령대로 우주선을 폭발 시키기 위해 설계를 하고 연구원 A의 계략대로 사람들이 탑승한 후 폭발 시키는 것에 성공한다. 그리고 주인공은 두고온 키카드를 가지러 침실로 가던 도중 우주선은 폭발하게 되며 이를 B홀을 통해 보게 된다.')
            t1.md = 1
        if scr == 1: # 1번째 대사
            t1.reset("이후..")
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
        scr = 1
        ch = 1
    #fin [끝]
    pygame.display.flip()
    clock.tick(60)

pygame.quit()