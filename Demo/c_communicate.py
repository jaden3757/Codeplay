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
import c_hall

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
            t1.reset("> 통신 장치실에 들어왔다.")
            t1.next("[ 인벤토리 열기 : 우측 하단 I 버튼 ]")
        if scr == 1: # 1번째 대사
            t1.reset("이동목록을 표시중")
        if scr == 2: # 2번째 대사 [이 아래에 더 추가 가능]
            t1.reset("통신 장치가 보인다.")
            if mode1['main_event'] < 2:
                t1.next('폭발에 의해 손상된 것 같다.')
            else:
                t1.next('고쳐진 상태이다.')
        if scr == 3:
            t1.reset("카드키가 필요하다.")
        if scr == 4:
            t1.reset("바닥에 전선이 있다.")
        if scr == 5:
            t1.reset('스페이스바로 넘기기')
        if scr == 6:
            t1.reset('스페이스바로 넘기기')
        # if scr == 5:
        #     t1.reset('나 : 혹시 뭐가 문제인지 알 것 같나요?')
        #     t1.next('휴스턴 : 한 번 전체적으로 봐야 할 것 같다네. 자네는 저기 있는 선좀 정리하고 있어 주게.')
        #     t1.next('나 : (무슨 꿍꿍이지..?)')
        #     t1.next('휴스턴 : 음.. 아무래도 이건 고치지 못할 것 같네. 우주선의 폭발물로 인해 완전히 수리가 불가능해.')
        #     t1.next('나 : (아무래도 에드워드 연구원의 자료와 연구노트에 있던 내용들이 사실인 것 같다. 우주선도 휴스턴 연구원이 터지게 한 것 같다...)')
        #     t1.next('나 : 그런가요? 그래도 한 번 제가 수리해 보죠.')
        #     t1.next('나 : (아무래도 더 있으면 위험해질 것 같다. 이륙장에 갔을때 보니까 차고에 1인 우주선이 있던데 지구와 통신을 하지 말고 휴스턴의 정부가 오기 전에 위험할 수 있지만 그걸 타고')
        #     t1.next('휴스턴의 정부보다 먼저 지구로 가야겠다.)')
        #     t1.next('< 스페이스바를 눌러서 다음으로 >')
        #     t1.md = 1
        # if scr == 6:
        #     t1.reset('나 : (하지만 탑승하기 전에 혹시 모르니 휴스턴에게 통신장치를 수리하기 위해 B창고에 있는 부품을 가져다 달라하고 말한 다음 시스템실에서 B구역을 보안모드로')
        #     t1.next('설정해야 겠다. 휴스턴을 B구역에 고립시켜둬야 겠어.)')
        #     t1.next('나 : 휴스턴씨, 통신실로 가보죠.')
        #     t1.next('휴스턴 : 통신실? 알겠다네.')
        #     t1.next('나 : 혹시 B창고에 통신장치를 수리하는데에 쓸만한 부품들을 모아서 가져와주실 수 있나요?')
        #     t1.next('휴스턴 : B창고? 흠.. 알겠네.')
        #     t1.next('나 : 저는 통신실에서 통신을 좀 시도해 보겠습니다.')
        #     t1.next('휴스턴 : 알겠네.')
        #     t1.next('< 스페이스바를 눌러서 종료 >')
        #     t1.md = 1
## B구역의 보안모드를 해제하려 할 경우 ("B구역 보안모드는 해제하면 위험해.") 출력 후 B구역 보안모드 해제 불가능
## "나 : (어서 시스템실에서 B구역을 보안모드로 설정하고 1인용 우주선에 탑승하자.)" 출력
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
    sheetname = 'c_communicate' # 엑셀파일에 자신이 원하는 방의 이름을 시트로 추가 (건드려야할 것)
    floor_button.item = [sheetname, 1] # 엑셀파일의 'sp3'시트의 1번째 가로줄을 할당

    # | 여기부터 자유롭게 추가 또는 변경 |
    # holy = itemobject("light2.png", "빛", 100, 100, 200, 200) # 예시
    # holy.item = [sheetname, 3] # 엑셀파일의 'sp3'시트의 2번째 가로줄을 할당
    time2 = 0
    if mode1['main_event'] == 1:
        mode1['main_event'] = 2
        time2 = 1
        setscr(5)

    wire = imagebutton('images/wire.png', 150, 150, 170, 400)
    if mode1['gettedwire'] == True:
        wire.off()

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

    hall_button = button("C 홀", 300, 40, 650, 200) # 하위 버튼 디자인
    hall_button.color = (0,0,0)
    hall_button.textsize = 20
    hall_button.font = 'pixel.ttf'

    getwire_button = button("전선 얻기", 300, 40, 650, 200) # 하위 버튼 디자인
    getwire_button.color = (0,0,0)
    getwire_button.textsize = 20
    getwire_button.font = 'pixel.ttf'

    if mode1['main_event'] > 0:
        bgimg = pygame.image.load('images/c_communicate.png')
    else:
        bgimg = pygame.image.load('images/c_communicate.png')
    
    bgimg = pygame.transform.scale(bgimg, (560, 560))

    sound.play_cynthia_S()

    while run:
        # 세팅 [ 건드리지 말아야 할 것]
        screen.fill(pygame.color.Color(50, 50, 50))
        pygame.draw.rect(screen, (20,20,20), [20, 20, 560, 560])
        screen.blit(bgimg, (20, 20))
        # main [여기에 코드 입력] > 이미지 오브젝트, 텍스트(prtext) 등등
        wire.draw()

        # | UI |
        prtext4("통신 장치실 | C", 'pixel.ttf', 20, 30, 30) # 여기는 바꿔도 됨
        drawui()
        textls()
        textprinting()
        if time2 == 1:
            primg2('images/talk3.png', 20, 20)
        if time2 == 2:
            primg2('images/talk4.png', 20, 20)
        # | 버튼 그리는 곳 |
        find_button.off()
        hall_button.off()
        getwire_button.off()
        if buttonmode == 1: # 이동목록 켜진 경우
            move_button.txt = '< 뒤로'
            hall_button.on()
        elif buttonmode == 2:
            move_button.txt = '< 뒤로'
            getwire_button.on()
        else: # 꺼진 경우
            move_button.txt = '이동목록'
            find_button.on()

        move_button.draw()
        find_button.draw()
        hall_button.draw()
        getwire_button.draw()

        # | 이벤트 관리소 |
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            run = False
        # // Mouse_click
        if event.type == pygame.MOUSEBUTTONDOWN:
            buttoncheck() # [삭제하면 안되는 것]
        
            if move_button.check() == 1: # 예시입니다
                if buttonmode == 0:
                    setscr(1)
                    buttonmode = 1
                else:
                    setscr(0)
                    buttonmode = 0
            if find_button.check() == 1:
                setscr(2)
            if hall_button.check() == 1:
                if '카드키' in getitem():
                    # c_hall.maprun()
                    pass
                else:
                    setscr(3)
            if wire.check() == 1:
                if mode1['gettedwire'] == False:
                    setscr(4)
                    buttonmode = 2
                else:
                    pass
            if getwire_button.check() == 1:
                if mode1['gettedwire'] == False:
                    wire.off()
                    mode1['gettedwire'] = True
                    item_t.append('전선')
                    itemui.refresh()
                    buttonmode = 0
                    setscr(0)
            if hall_button.check() == 1:
                c_hall.maprun()
        if pygame.mouse.get_pressed()[0] == 1:
            pass
            # itemcheck2(holy) # 오브젝트 예시
        # key

        if pygame.key.get_pressed()[pygame.K_m]:
            Sound_controll.sound_controll()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if time2 == 1:
                    time2 += 1
                    setscr(6)
                elif time2 == 2:
                    time2 = 0
                    t1.md = 0
                    t1.mm = 0
                    setscr(0)
        #fin [끝]
        mousechange()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    maprun()