# -*- coding: utf-8 -*-

import pygame
import sys
from module1 import *
from but import *
from main1 import * #main
from item import *
from tkinter import *


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

def security_room():
    password = 18392
    while run:
        # 세팅 [ 건드리지 말아야 할 것]
        screen.fill(LIGHT_BLACK)
        # // All_event [이벤트창]

        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            run = False
        # // Mouse_click
        if pygame.key.get_pressed()[pygame.K_w]:
            sp2.room1()

        if pygame.key.get_pressed()[pygame.K_q]:
            sp3.game_over()

        if pygame.key.get_pressed()[pygame.K_e]:
            sp5.security_room()

        btn = button("ENTER PASSWORD", 240, 40, (screen_width/2 - 90), (screen_height/2) - 100)
        btn.draw()
        btn.check()
        btn.textsize = (2)
        clicked = btn.clicking()

        if clicked == True:
            print("accepted clicking")
            time.sleep(0.2)

            root = Tk()
            root.title("GUI")
            # root.geometry("640x480")
            root.geometry("170x80+500+300") #가로 크기, 세로 크기, x좌표, y좌표

            root.resizable(False, False) #x(너비), y(높이) 값 변경 불가

            label1 = Label(root, text="Enter password", bg="gray")
            
            label1.pack()
            e = Entry(root, width=20)
            e.pack()
            e.insert(0, "")

            def btncmd():
                global password
                value = e.get()

                value = int(value)

                if password == value:
                    print("Correct!!")
                    root.destroy()
                else:
                    print("Worng!!")

                print(e.get())
                e.delete(0, END)

            btn = Button(root, fg = "white", bg = "gray" ,text="Enter", command=btncmd)
            btn.place(x = 100, y = 50)

            root.configure(bg='gray')
            root.mainloop()

        #fin [끝]
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()