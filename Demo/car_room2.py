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
import car_room1



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
            t1.reset(". . . . . . . . . .")
        if scr == 1: # 0번째 대사(시작시 무조건 출력)
            t1.reset("그렇게 나는 차고에 있던 1인 우주선을 타고 지구에 도착할 수 있었다.")
        if scr == 2:
            t1.reset("지상에 올라오고 잠깐의 시간이 흐르자 군인들과 마주할 수 있었다.")
        if scr == 3:
            t1.reset("다행히 휴스턴의 정부로 온 것은 아니여서 그들에게 달 기지에서 있었던일들을 자료와 함께 설명할 수 있었고 이후 달 기지에서 있었던사실들을 군에서도 알게되어 위로 빠르게 알려져 다행히 휴스턴의 정부의돌아오는 우주선을 막을 수 있었다.")
        if scr == 4:
            t1.reset("비밀리에 진행되었던 부칸의계획과 연구시설은 뒤집혔고 모두가 이 사실들을 알게되었다.")
        if scr == 5:
            t1.reset("주변 국가들은 휴스턴의 정부를 압박하게 되었고 휴스턴의 정부는 압박을 견디지못해 결국 내부에 분쟁이 일어나게 되었고 자멸했다.")
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
    a = 0

    sheetname = 'car_room' # 엑셀파일에 자신이 원하는 방의 이름을 시트로 추가 (건드려야할 것)
    floor_button.item = [sheetname, 1] # 엑셀파일의 'sp3'시트의 1번째 가로줄을 할당

    # | 여기부터 자유롭게 추가 또는 변경 |
    abutton1 = button("다음", 100, 50, 650, 500)
    abutton1.color = (255,255,255)
    abutton1.textcolor = (0,0,0)
    abutton1.textsize = 22
    abutton1.font = 'pixel.ttf'
    
    abutton2 = button("다음", 100, 50, 650, 500)
    abutton2.color = (255,255,255)
    abutton2.textcolor = (0,0,0)
    abutton2.textsize = 22
    abutton2.font = 'pixel.ttf'
    
    abutton3 = button("다음", 100, 50, 650, 500)
    abutton3.color = (255,255,255)
    abutton3.textcolor = (0,0,0)
    abutton3.textsize = 22
    abutton3.font = 'pixel.ttf'
    
    abutton4 = button("다음", 100, 50, 650, 500)
    abutton4.color = (255,255,255)
    abutton4.textcolor = (0,0,0)
    abutton4.textsize = 22
    abutton4.font = 'pixel.ttf'
    
    abutton5 = button("다음", 100, 50, 650, 500)
    abutton5.color = (255,255,255)
    abutton5.textcolor = (0,0,0)
    abutton5.textsize = 22
    abutton5.font = 'pixel.ttf'


    sound.play_cynthia_S()

    while run:
        # 세팅 [ 건드리지 말아야 할 것]
        screen.fill(pygame.color.Color(50, 50, 50))
        pygame.draw.rect(screen, (20,20,20), [20, 20, 560, 560])
        # main [여기에 코드 입력] > 이미지 오브젝트, 텍스트(prtext) 등등
        # holy.draw()

        # | UI |
        prtext4("차고 | C-3", 'pixel.ttf', 20, 30, 30) # 여기는 바꿔도 됨
        drawui()
        textls()
        textprinting()

        # | 버튼 그리는 곳 |
        abutton1.draw()
        abutton2.draw()
        abutton3.draw()
        abutton4.draw()
        abutton5.draw()

        abutton2.off()
        abutton3.off()
        abutton4.off()
        abutton5.off()
        
        if a == 1:
            setscr(1)
        
        if a ==2:
            abutton2.on()
            abutton1.off()
            setscr(2)
        if a ==3:
            abutton3.on()
            abutton1.off()
            setscr(3)
        if a ==4:
            abutton4.on()
            abutton1.off()
            setscr(4)
        if a ==5:
            abutton5.on()
            abutton1.off()
            setscr(5)
        # | 이벤트 관리소 |
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            run = False

        # // Mouse_click
        if event.type == pygame.MOUSEBUTTONDOWN:
            buttoncheck() # [삭제하면 안되는 것]

            if abutton1.check() == 1: # 예시입니다
                a = 1
            if abutton2.check() == 1: # 예시입니다
                a = 2
            if abutton3.check() == 1: # 예시입니다
                a = 3
            if abutton4.check() == 1: # 예시입니다
                a = 4
            if abutton5.check() == 1: # 예시입니다
                a = 5



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
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    maprun()