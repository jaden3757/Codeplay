# -*- coding: utf-8 -*-

import pygame
import sys
from module1 import *
from but import *
from main1 import * #main
from item import *
from excel import *
# 방 import 하는 곳 (지도상에서 붙어있는 방 알아서 전부 import 해주길 바람)
import loading2

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
            t1.reset("이동목록을 표시중")
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

    sheetname = 'b_hall' # 엑셀파일에 자신이 원하는 방의 이름을 시트로 추가 (건드려야할 것)
    floor_button.item = [sheetname, 1] # 엑셀파일의 'sp2'시트의 1번째 가로줄을 할당

    # | 여기부터 자유롭게 추가 |
    holy = itemobject("light2.png", "빛", 100, 100, 200, 200) # 예시
    holy.item = [sheetname, 2] # 엑셀파일의 'sp2'시트의 2번째 가로줄을 할당

    box1 = itemobject('images\\box.png', '상자1', 100, 100, 300, 300)
    box1.item = [sheetname, 3]
    box2 = itemobject('images\\box.png', '상자2', 100, 100, 123, 290)
    box2.item = [sheetname, 4]
    box3 = itemobject('images\\box.png', '상자3', 100, 100, 400, 100)
    box3.item = [sheetname, 5]
    box4 = itemobject('images\\box.png', '상자4', 100, 100, 150, 330)
    box4.item = [sheetname, 6]
    box5 = itemobject('images\\box.png', '상자5', 100, 100, 200, 400)
    box5.item = [sheetname, 7]

    move_button = button("이동목록", 100, 50, 750, 500)
    move_button.color = (255,255,255)
    move_button.textcolor = (0,0,0)
    move_button.textsize = 22
    move_button.font = 'pixel.ttf'

    security_button = button("보안실", 300, 40, 650, 200)
    security_button.color = (0,0,0)
    security_button.textsize = 20
    security_button.font = 'pixel.ttf'

    bedroom_button = button("침실", 300, 40, 650, 250)
    bedroom_button.color = (0,0,0)
    bedroom_button.textsize = 20
    bedroom_button.font = 'pixel.ttf'

    warehouse_button = button("B창고", 300, 40, 650, 300)
    warehouse_button.color = (0,0,0)
    warehouse_button.textsize = 20
    warehouse_button.font = 'pixel.ttf'

    manage_button = button("관리실", 300, 40, 650, 350)
    manage_button.color = (0,0,0)
    manage_button.textsize = 20
    manage_button.font = 'pixel.ttf'

    movelist = False

    while run:
        # 세팅 [ 건드리지 말아야 할 것]
        screen.fill(pygame.color.Color(50, 50, 50))
        pygame.draw.rect(screen, (20,20,20), [20, 20, 560, 560])
        # main [여기에 코드 입력] > 이미지 오브젝트, 텍스트(prtext) 등등
        box1.draw()
        box2.draw()
        box3.draw()
        box4.draw()
        box5.draw()

        # UI
        prtext4("ROOMNUM | ROOMCODE", 'pixel.ttf', 20, 30, 30) # 여기는 바꿔도 됨
        drawui()
        textls()
        textprinting()

        # 버튼 그리는 곳
        if movelist == True:
            move_button.txt = '< 뒤로'
            security_button.on()
            bedroom_button.on()
            warehouse_button.on()
            manage_button.on()
        else:
            move_button.txt = '이동목록'
            security_button.off()
            bedroom_button.off()
            warehouse_button.off()
            manage_button.off()

        move_button.draw()
        security_button.draw()
        bedroom_button.draw()
        warehouse_button.draw()
        manage_button.draw()

        # // All_event [이벤트창]
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            run = False
        # // Mouse_click
        if event.type == pygame.MOUSEBUTTONDOWN:
            buttoncheck() # [삭제하면 안되는 것]
            if move_button.check() == 1: # 예시입니다
                if movelist == True:
                    setscr(0)
                    movelist = False
                elif movelist == False:
                    setscr(1)
                    movelist = True
            # itemcheck(holy) # 이미지 오브젝트 예시
            itemcheck(box1)
            itemcheck(box2)
            itemcheck(box3)
            itemcheck(box4)
            itemcheck(box5)
        
        if pygame.key.get_pressed()[pygame.K_m]:
            Sound_controll.sound_controll()
            pygame.mixer.music.stop()

        if pygame.key.get_pressed()[pygame.K_m]:
            Sound_controll.sound_controll()
        
        #fin [끝]
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    maprun()