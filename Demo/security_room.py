# -*- coding: utf-8 -*-


# -*- coding: utf-8 -*-

import pygame
import sys
from tkinter import *
from module1 import *
from but import *
# from main1 import * #main
from item import *
from excel import *
# 방 import 하는 곳 (지도상에서 붙어있는 방 알아서 전부 import 해주길 바람)
import loading2
import sp3
import Sound_controll
import time

LIGHT_BLACK = (50, 50, 50)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DARK_WHITE = (180, 180, 180)
GREEN = (100, 255, 100)
RED = (255, 50, 50)
LIGHT_BLACK = (50, 50, 50)

screen_width = 1000
screen_height = 600
# 시작
pygame.init() 
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Moon Side")
clock = pygame.time.Clock()

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
        # if scr == i: # i번째 대사 (샘플)
        #   t1.reset("가장 위쪽에 나오는 대사(1번째 줄)")
        #   t1.next("그 다음줄 추가")
        ch = 0

#                       *중요*
# 1. sheetname을 파일 이름으로 예시) sp3.py 면 'sp3'
#    + itemo.xlsx에 파일 이름으로 시트를 추가해야함 (.py 빼고)
# 2. 방을 이어지게(파일 오가기) 하고 싶다면 알아서 임포트 하고
#    방이름(파일이름).maprun() 으로 다른 방으로 이동
# 3. 변수 선언은 반드시 maprun함수 안에 해야함(지역변수 문제 때문)
# 4. 대사 출력은 setscr(a), 대사들은 textls 안에 알아서 만들기
password = 19020

def maprun():
    global scr
    global ch
    global password

    sheetname = 'sp2' # 엑셀파일에 자신이 원하는 방의 이름을 시트로 추가 (건드려야할 것)
    floor_button.item = [sheetname, 1] # 엑셀파일의 'sp2'시트의 1번째 가로줄을 할당

    # | 여기부터 자유롭게 추가 |
    holy = itemobject("light2.png", "빛", 100, 100, 200, 200) # 예시
    holy.item = [sheetname, 2] # 엑셀파일의 'sp2'시트의 2번째 가로줄을 할당

    test_button = button("테스트", 100, 50, 750, 400)
    run = True

    # sound = ("Cynthia.mp3")
    # pygame.mixer.music.load(sound)
    # pygame.mixer.music.play(-1)

    run = True

    while run:
        # 세팅 [ 건드리지 말아야 할 것]
        screen.fill(pygame.color.Color(50, 50, 50))
        pygame.draw.rect(screen, (20,20,20), [20, 20, 560, 560])
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
            # screen.blit()
        # if pygame.key.get_pressed()[pygame.K_w]:
        #     sp3.maprun()
        
        if pygame.key.get_pressed()[pygame.K_m]:
            Sound_controll.sound_controll()

        goto_b = button("B-HALL", 230, 30, (screen_width/2 + 195), (screen_height/2) - 180)
        goto_b.draw()
        goto_b.check()
        goto_b_clicked = goto_b.clicking()

        btn = button("ENTER PASSWORD", 230, 30, (screen_width/2 + 195), (screen_height/2) - 130)
        btn.draw()
        btn.check()
        btn.textsize = (1)
        clicked = btn.clicking()

        if goto_b_clicked:
            sp3.maprun()

        if clicked == True:
            print("accepted clicking")
            time.sleep(0.2)

            root = Tk()
            root.title("GUI")
            # root.geometry("640x480")
            root.geometry("170x80+500+300") #가로 크기, 세로 크기, x좌표, y좌표
            root.resizable(False, False) #x(너비), y(높이) 값 변경 불가
            root.wm_attributes("-topmost", 1)
            label1 = Label(root, text="Enter password", bg="gray")
            
            label1.pack()
            e = Entry(root, width=20)
            e.pack()
            e.insert(0, "")

            def btncmd():
                global password
                value = e.get()
                value = int(value)

                # my_sound.play()

                if password == value:
                    print("Correct!!")
                    # door_effect.play()
                    root.destroy()
                else:
                    print("Worng!!")

                print(e.get())
                e.delete(0, END)

            btn = Button(root, fg = "black", bg = "gray" ,text="Enter", command=btncmd)
            btn.place(x = 100, y = 50)

            root.configure(bg='gray')
            root.mainloop()
        
        #fin [끝]
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

