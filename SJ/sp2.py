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
import sp5
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
            sp5.security_room()

        if pygame.key.get_pressed()[pygame.K_m]:
            root = Tk()
            root.title("MUSIC CONTROLL")

            root.geometry("180x220+500+300") #가로 크기, 세로 크기, x좌표, y좌표

            root.resizable(False, False) #x(너비), y(높이) 값 변경 불가
            def v_up():
                v = pygame.mixer.music.get_volume()
                pygame.mixer.music.set_volume(v + 0.1)
                print("volume up")
                time.sleep(0.2)

            def v_down():
                v = pygame.mixer.music.get_volume()
                pygame.mixer.music.set_volume(v - 0.1)
                print("volume down")
                time.sleep(0.2)

            btn_up = Button(root, width = 11, height = 2, text = "Volume Up", command = v_up)
            btn_up.place(x = 50, y = 20)

            btn_down = Button(root, width = 11, height = 2, text = "Volume Down", command = v_down)
            btn_down.place(x = 50, y = 70)

            mute = IntVar() #여기에 int형으로 값을 저장
            mute_button = Radiobutton(root, text="pause", value=1, variable=mute) # value 가 숫자면 variable의 상태가 Int으로 적어야함
            mute_button.place(x = 50, y = 130)
            mute_button = Radiobutton(root, text="unpause", value=2, variable=mute) # value 가 숫자면 variable의 상태가 Int으로 적어야함
            mute_button.place(x = 50, y = 170)

            mute_value = mute.get()
            print(mute_value)
            
            if mute_value == 1:
                pygame.mixer.music.pause()
                time.sleep(0.2)
            elif mute_value == 2:
                pygame.mixer.music.unpause()
                time.sleep(0.2)

            root.mainloop()
        
        #fin [끝]
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


room1()
