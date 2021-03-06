# -*- coding: utf-8 -*-

import pygame
import sys
from module1 import *
from but import *
from main1 import * #main
from item import *
from excel import *
import sound
import Sound_controll
# 방 import 하는 곳 (지도상에서 붙어있는 방 알아서 전부 import 해주길 바람)
import loading2
import a_communication
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
            t1.reset("중요한 건 없는 것 같다.")
        if scr == 3:
            t1.reset("드라이버가 필요하다")
        if scr == 4:
            t1.reset("일자 드라이버가 필요하다")
        if scr == 5:
            t1.reset("이미 켜져있다")
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
    sheetname = 'a_communication' # 엑셀파일에 자신이 원하는 방의 이름을 시트로 추가 (건드려야할 것)
    floor_button.item = [sheetname, 1] # 엑셀파일의 'sp3'시트의 1번째 가로줄을 할당

    # | 여기부터 자유롭게 추가 또는 변경 |
    open_button = imagebutton('images/none.png', 560, 560, 20,20)

    b1 = imagebutton('images/bolt1.png', 30, 30, 60, 140)
    b1.seetext = '제거하기'
    b2 = imagebutton('images/bolt2.png', 30, 30, 470, 90)
    b2.seetext = '제거하기'
    b3 = imagebutton('images/bolt2.png', 30, 30, 130, 530)
    b3.seetext = '제거하기'
    b4 = imagebutton('images/bolt1.png', 30, 30, 530, 470)
    b4.seetext = '제거하기'

    move_button = button("이동목록", 100, 50, 650, 500)
    move_button.color = (255,255,255)
    move_button.textcolor = (0,0,0)
    move_button.textsize = 22
    move_button.font = 'pixel.ttf'

    find_button = button("집중탐사", 100, 50, 850, 500)
    find_button.color = (255,255,255)
    find_button.textcolor = (0,0,0)
    find_button.textsize = 22
    find_button.font = 'pixel.ttf'

    lower_button = button("킨다", 300, 40, 650, 200) # 하위 버튼 디자인
    lower_button.color = (0,0,0)
    lower_button.textsize = 20
    lower_button.font = 'pixel.ttf'

    lower2_button = button("키지 않는다", 300, 40, 650, 250) # 하위 버튼 디자인
    lower2_button.color = (0,0,0)
    lower2_button.textsize = 20
    lower2_button.font = 'pixel.ttf'

    bgimg = pygame.image.load('images/commu1.png')
    bgimg = pygame.transform.scale(bgimg, (560, 560))

    bgimg2 = pygame.image.load('images/commu2.png')
    bgimg2 = pygame.transform.scale(bgimg2, (560, 560))
    
    while run:
        # 세팅 [ 건드리지 말아야 할 것]
        screen.fill(pygame.color.Color(50, 50, 50))
        pygame.draw.rect(screen, (20,20,20), [20, 20, 560, 560])
        if mode1['dduopen'] == False:
            screen.blit(bgimg, (20, 20))
        else:
            screen.blit(bgimg2, (20, 20))
        # main [여기에 코드 입력] > 이미지 오브젝트, 텍스트(prtext) 등등
        if mode1['ddu'] == [1,1,1,1]:
            open_button.on()
        else:
            open_button.off()
        open_button.draw()
        b1.off()
        b2.off()
        b3.off()
        b4.off()
        if mode1['ddu'][0] == 0:
            b1.on()
        if mode1['ddu'][1] == 0:
            b2.on()
        if mode1['ddu'][2] == 0:
            b3.on()
        if mode1['ddu'][3] == 0:
            b4.on()
        b1.draw()
        b2.draw()
        b3.draw()
        b4.draw()
        # | UI |
        drawui()
        textls()
        textprinting()

        # | 버튼 그리는 곳 |
        find_button.off()
        lower_button.off()
        lower2_button.off()
        if buttonmode == 1: # 이동목록 켜진 경우
            move_button.txt = '< 뒤로'
            lower_button.on()
            lower2_button.on()
        else: # 꺼진 경우
            move_button.txt = '< 뒤로'

        move_button.draw()
        lower_button.draw()
        lower2_button.draw()

        # | 이벤트 관리소 |
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            run = False
        # // Mouse_click
        if event.type == pygame.MOUSEBUTTONDOWN:
            if move_button.check() == 1: # 예시입니다
                a_communication.maprun()
            if b1.check() == 1:
                if '일자 드라이버' in getitem():
                    mode1['ddu'][0] = 1
                else:
                    setscr(4)
            if b2.check() == 1:
                if '드라이버' in getitem():
                    mode1['ddu'][1] = 1
                else:
                    setscr(3)  
            if b3.check() == 1:
                if '드라이버' in getitem():
                    mode1['ddu'][2] = 1
                else:
                    setscr(3)  
            if b4.check() == 1:
                if '일자 드라이버' in getitem():
                    mode1['ddu'][3] = 1
                else:
                    setscr(4)
            if open_button.check() == 1:
                if mode1['dduopen'] == False:
                    mode1['dduopen'] = True
                else:
                    if mode1['car'] == False:
                        buttonmode = 1
                    else:
                        setscr(5)
            if lower_button.check() == 1:
                mode1['car'] = True
                actionbar.print('차고가 열렸습니다')
                buttonmode = 0
            if lower2_button.check() == 1:
                buttonmode = 0
        if pygame.mouse.get_pressed()[0] == 1:
            pass
        # key

        if pygame.key.get_pressed()[pygame.K_m]:
            Sound_controll.sound_controll()
        #fin [끝]
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    maprun()