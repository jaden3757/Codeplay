# -*- coding: utf-8 -*-

import pygame
import sys
from module1 import *
from but import *
from main1 import * #main
from item import *
from tkinter import *


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
            t1.reset("> 샘플 맵입니다")
            t1.next("[ 인벤토리 열기 : 우측 하단 I 버튼 ]")
        if scr == 1: # 1번째 대사
            t1.reset("..")
        if scr == 2: # 2번째 대사 [이 아래에 더 추가 가능]
            t1.reset("..")
        ch = 0

holy = itemobject("light2.png", "빛", 100, 100, 200, 200)

class button:
    def __init__(self, x, y, w, h, button_cr, side_cr, changed_cr):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.button_cr = button_cr
        self.side_cr = side_cr
        self.changed_cr = changed_cr
    
    def draw(self):
        pygame.draw.rect(screen, self.button_cr, [self.x, self.y, self.w, self.h])
        pygame.draw.rect(screen, self.side_cr, [self.x, self.y, self.w, self.h], 2)

    def text_up(self):
        myFont = pygame.font.SysFont("microsoftphagspa", 15, True, False)
        text_Title_yes = myFont.render("UP", True, BLACK)
        screen.blit(text_Title_yes, (int(self.x+6), int(self.y+6)))

    def text_down(self):
        myFont = pygame.font.SysFont("microsoftphagspa", 15, True, False)
        text_Title_yes = myFont.render("DOWN", True, BLACK)
        screen.blit(text_Title_yes, (int(self.x+6), int(self.y+6)))

    def clicked_up(self):
        pygame.event.pump()
        mouse_pos = pygame.mouse.get_pos()
        mouse_buttons = pygame.mouse.get_pressed()

        if  mouse_pos[0] > self.x and mouse_pos[0] < self.x + self.w:
            if mouse_pos[1] > self.y and mouse_pos[1] < self.y + self.h:
                pygame.draw.rect(screen, self.changed_cr, [self.x, self.y, self.w, self.h])
                pygame.draw.rect(screen, self.side_cr, [self.x, self.y, self.w, self.h], 2)

                self.text_up()
                
                if mouse_buttons[0]:
                    v = pygame.mixer.music.get_volume()
                    pygame.mixer.music.set_volume(v + 0.1)
                    print("volume up")
                    time.sleep(0.2)

    def clicked_down(self):
        pygame.event.pump()
        mouse_pos = pygame.mouse.get_pos()
        mouse_buttons = pygame.mouse.get_pressed()

        if  mouse_pos[0] > self.x and mouse_pos[0] < self.x + self.w:
            if mouse_pos[1] > self.y and mouse_pos[1] < self.y + self.h:
                pygame.draw.rect(screen, self.changed_cr, [self.x, self.y, self.w, self.h])
                pygame.draw.rect(screen, self.side_cr, [self.x, self.y, self.w, self.h], 2)

                self.text_down()
                
                if mouse_buttons[0]:
                    v = pygame.mixer.music.get_volume()
                    pygame.mixer.music.set_volume(v - 0.1)
                    print("volume down")
                    time.sleep(0.2)

    def on_button(self):
        if pygame.mouse.get_pos()[0] > self.x and pygame.mouse.get_pos()[0] < self.x + self.w:
            if pygame.mouse.get_pos()[1] > self.y and pygame.mouse.get_pos()[1] < self.y + self.h:
                btn_1 = button(screen_width/2, screen_height/2, 80, 30, WHITE, BLACK, DARK_WHITE)

# myFont = pygame.font.SysFont( "microsoftphagspa", 30, True, False)
# text_Title= myFont.render("Pygame Text Test", True, BLACK)

while run:
    screen.fill(LIGHT_BLACK)

    # myFont = pygame.font.SysFont("microsoftphagspa", 15, True, False)
    # text_v_pause = myFont.render("Music pause : o ", True, BLACK)
    # text_v_unpause = myFont.render("Music unpause : p ", True, BLACK)
    # screen.blit(text_v_pause, (screen_width, screen_height))
    # screen.blit(text_v_unpause, (screen_width, screen_height))

    up_btn = button((screen_width/2 - 30), 100, 60, 30, WHITE, BLACK, DARK_WHITE)
    up_btn.draw()
    up_btn.text_up()
    up_btn.on_button()
    up_btn.clicked_up()

    down_btn = button((screen_width/2 - 30), 150, 60, 30, WHITE, BLACK, DARK_WHITE)
    down_btn.draw()
    down_btn.text_down()
    down_btn.on_button()
    down_btn.clicked_down()

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        run = False
    # // Mouse_click
    if event.type == pygame.MOUSEBUTTONDOWN:
        buttoncheck() # [삭제하면 안되는 것]
        itemcheck(holy)
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_o:
            pygame.mixer.music.pause()
            print("Pause")
            time.sleep(0.3)
        if event.key == pygame.K_p:
            pygame.mixer.music.unpause()
            print("Unpause")
        # screen.blit()
    if pygame.key.get_pressed()[pygame.K_e]:
        changemap(3)
    if pygame.key.get_pressed()[pygame.K_t]:
        root = Tk()
        root.title("GUI")
        # root.geometry("640x480")
        root.geometry("640x480+100+300") #가로 크기, 세로 크기, x좌표, y좌표

        root.resizable(False, False) #x(너비), y(높이) 값 변경 불가

        root.mainloop()


    pygame.display.flip()
    clock.tick(60)

pygame.quit()