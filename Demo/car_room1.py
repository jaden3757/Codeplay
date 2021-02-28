# -*- coding: utf-8 -*-

import pygame
import sys
from module1 import *
from but import *
from main1 import * #main
from item import *
from excel import *
# 방 import 하는 곳 (지도상에서 붙어있는 방 알아서 전부 import 해주길 바람)
import time
import Sound_controll
import sound
import car_room
import car_room2
import ending1
import ending2

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
            t1.reset("> 우주선에 탑승하였습니다.")
            t1.next("[ 인벤토리 열기 : 우측 하단 I 버튼 ]")
        if scr == 1: # 1번째 대사
            t1.reset("이동목록을 표시중")
        if scr == 2: # 1번째 대사
            t1.reset("연료가 없습니다.")
        if scr == 3: # 1번째 대사
            t1.reset("아직 휴스턴을 처리하지 못했다.")

        
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

def maprun():
    global scr
    global ch
    global run
    # 버튼 만드는 곳
    # variable(버튼이름) = button(text, width, height, x좌표, y좌표)
    # variable.draw() // 버튼을 화면에 출력
    # variable.check() // 버튼 위에 마우스가 있다면 1, 아니면 0출력
    # variable.color = (R,G,B) // 버튼 색 설정
    # variable.textcolor = (R,G,B) // 텍스트 색 설정
    # variable.textsize = (텍스트사이즈)

    #                *버튼 활용법*
    # test_button.check() : 마우스가 위에 올려져 있으면 1을, 아니면 0을 리턴
    # test_button.on() : 버튼의 모든 활동 활성화
    # test_button.off() : 버튼의 모든 기능 비활성화 (draw, check 등)
    

    # objectname = itemobject(사진파일, 개체이름, x크기, y크기, x좌표, y좌표)
    # 활용 예시 (아래 참고)
    # box = itemobject('box.png', '박스', width, height, x, y)
    # box.item = [sheetname, 1] # sheetname은 미리 지정해야함 / 1은 1번째 가로줄을 의미

    
    # | 이 부분은 지우지는 말고 무조건 수정해야하는 부분 |
    firstsetting()
    buttonmode = 0
    setscr(0)
    sheetname = 'car_room' # 엑셀파일에 자신이 원하는 방의 이름을 시트로 추가 (건드려야할 것)
    floor_button.item = [sheetname, 1] # 엑셀파일의 'sp3'시트의 1번째 가로줄을 할당

    # | 여기부터 자유롭게 추가 또는 변경 |
    move_button = button("내리기", 100, 50, 650, 500)
    move_button.color = (255,255,255)
    move_button.textcolor = (0,0,0)
    move_button.textsize = 22
    move_button.font = 'pixel.ttf'

    go_button = button("지구로가자 ", 130, 50, 800, 500)
    go_button.color = (255,255,255)
    go_button.textcolor = (0,0,0)
    go_button.textsize = 22
    go_button.font = 'pixel.ttf'

    sound.play_cynthia_S()

    showing = 1
    fade = 0
    fading = 0
    fadewait = 0
    im = 0

    t_surface = screen.convert_alpha()
    t_surface.fill((0,0,0,0))

    while run:
        # 세팅 [ 건드리지 말아야 할 것]
        screen.fill(pygame.color.Color(50, 50, 50))
        pygame.draw.rect(screen, (20,20,20), [20, 20, 560, 560])
        # main [여기에 코드 입력] > 이미지 오브젝트, 텍스트(prtext) 등등
        if fade > 0:
            pygame.draw.rect(t_surface, (0,0,0,(fade/100)*255), [0,0,1000,600])
            screen.blit(t_surface, (0,0))

        
        if fading == 1:
            if fade < 100:
                if fadewait > 0:
                    fadewait -= 1
                else:
                    fade += 1
            else:
                fading = 2
                fadewait = 0
                im += 1
                if 'USB' in getitem():
                    ending1.maprun()
                else:
                    ending2.maprun()
        if fading == 2:
            if fade > 0:
                if fadewait > 0:
                    fadewait -= 1
                else:
                    fade -= 1
            else:
                fading = 0
        
        # | UI |
        prtext4("차고 | C-3", 'pixel.ttf', 20, 30, 30) # 여기는 바꿔도 됨
        drawui()
        textls()
        textprinting()

        # | 버튼 그리는 곳 |
        move_button.draw()
        go_button.draw()

        # | 이벤트 관리소 |
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            run = False
        # // Mouse_click
        if event.type == pygame.MOUSEBUTTONDOWN:
            buttoncheck() # [삭제하면 안되는 것]

            if move_button.check() == 1: # 예시입니다
                car_room.maprun()
            
            if go_button.check() == 1:
                # item_t.append('연료통')
                # secure['b_long'] = 0
                if '연료통' in getitem():
                    if secure['b_long'] == 0:
                        if 'USB' in getitem():
                            if showing == 1:
                                fading = 1
                                showing = 0
                        else:
                            if showing == 1:
                                fading = 1
                                showing = 0
                    else:
                        setscr(3)
                else:
                    setscr(2)


            # itemcheck(holy) # 이미지 오브젝트 예시
        if pygame.mouse.get_pressed()[0] == 1:
            pass

        # key

        if pygame.key.get_pressed()[pygame.K_m]:
            Sound_controll.sound_controll()
            pygame.mixer.music.stop()

        if pygame.key.get_pressed()[pygame.K_m]:
            Sound_controll.sound_controll()

        
        #fin [끝]
        screen.blit(t_surface, (0,0))
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    maprun()