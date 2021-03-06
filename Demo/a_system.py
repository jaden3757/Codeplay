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
import a_security2
import a_system1
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
            t1.reset("> 시스템실에 들어왔다.")
            t1.next("[ 인벤토리 열기 : 우측 하단 I 버튼 ]")
            if mode1['main_event'] == 1:
                t1.next('\'통신장치실로 이동하자.\'')
            if mode1['main_event'] == 2:
                t1.next('\'휴스턴을 B구역에 가두고 우주선을 타자.\'')
            t1.md = 0
            t1.mode = 0
        if scr == 1: # 1번째 대사
            t1.reset("이동목록을 표시중")
        if scr == 2: # 2번째 대사 [이 아래에 더 추가 가능]
            t1.reset("중앙컴퓨터가 있다.")
        if scr == 3:
            t1.reset("카드키가 없습니다")
        if scr == 4:
            t1.reset("전기가 공급되지 않고 있다.")
        if scr == 5:
            t1.reset("중앙 컴퓨터 전원을 켰다")
        if scr == 6:
            t1.reset("이미 켜져 있다.")
        if scr == 7:
            t1.reset("전원이 아직 꺼져 있다.")
        if scr == 8:
            t1.reset('스페이스바를 눌러서 넘기기')
        if scr == 9:
            t1.reset('스페이스바를 눌러서 넘기기')
        # if scr == 8:
        #     t1.reset('나 : (사람이다..!)')
        #     t1.next('나 : (생존자인가..?)')
        #     t1.next('휴스턴 : 오오 반갑구만! 자네도 살아있었는가?')
        #     t1.next('나 : 당신도 살아있었군요.')
        #     t1.next('나 : (에드워드의 자료에 있던 휴스턴 연구원이다..)')
        #     t1.next('휴스턴 : 대원들이 전부 사망한줄 알았는데 자네가 살아있을 줄은 몰랐다네!')
        #     t1.next('나 : 두고온 키카드를 가지러 가고있었는데 우주선이 폭발하더군요. 당신은 어떻게 살아있는 거죠?')
        #     t1.next('휴스턴 : 나는 그러니까... 음.. 알약을 잘못 먹어 수면제를 먹는 바람에.. 우주선으로 가지 못하고 내 침실 D방에서 자버리고 말았다네!')
        #     t1.next('나 : (수상해 보인다.. 휴스턴 연구원이 우주선을 폭발 시킨 것 같다..)')
        #     t1.next('< 스페이스바를 눌러서 다음으로 >')
        #     t1.md = 1
        # if scr == 9:
        #     t1.reset('나 : 아.. 그렇군요.')
        #     t1.next('휴스턴 : 자네 혹시 연구실.. 아.. 아니라네.')
        #     t1.next('휴스턴 : 자네 나와 같이 동행하지!')
        #     t1.next('나 : (동행을 하게 된다면 위험하고 무슨 일이 일어날지 모르지만 그래도 통신장치를 고치는데에는 도움이 될지도..?)')
        #     t1.next('나 : 그러시죠. 혹시 통신이 안돼서 통신장치를 수리해야 할 것 같은데 도움을 주실 수 있나요?')
        #     t1.next('휴스턴 : 아아 물론이지.')
        #     t1.next('나 : 그런데 C구역으로 가는 길이 비밀번호로 막혔는데..')
        #     t1.next('휴스턴 : 허허 걱정말게. 나는 보안모드가 발생될 경우를 대비해 비밀번호를 외워둔다네. 이전까지 한 번도 보안모드가 발생된 적이')
        #     t1.next('없어서 외우고 있는 비밀번호 아직 유효할 것이네.')
        #     t1.next('휴스턴 : 통신장치실로 가시게!')
        #     t1.next('< 스페이스바를 눌러서 종료 >')
        #     t1.md = 1
        if scr == 10:
          t1.reset("당신은 아직 이 컴퓨터를 사용하면 안될 것 같다")
          if mode1['main_event'] == 1:
            t1.next("통신장치를 수리하고 오자")
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
    sheetname = 'a_system' # 엑셀파일에 자신이 원하는 방의 이름을 시트로 추가 (건드려야할 것)
    floor_button.item = [sheetname, 1] # 엑셀파일의 'sp3'시트의 1번째 가로줄을 할당

    # | 여기부터 자유롭게 추가 또는 변경 |
    # holy = itemobject("light2.png", "빛", 100, 100, 200, 200) # 예시
    # holy.item = [sheetname, 2] # 엑셀파일의 'sp3'시트의 2번째 가로줄을 할당

    time2 = 0
    if mode1['main_event'] == 0 and [mode1['seenote'], mode1['edward'], mode1['tryconnect']] == [1,1,1]:
        mode1['main_event'] = 1
        time2 = 1
        setscr(8)

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

    security_button = button("A 보안실2", 300, 40, 650, 200) # 하위 버튼 디자인
    security_button.color = (0,0,0)
    security_button.textsize = 20
    security_button.font = 'pixel.ttf'

    communication_button = button("통신실", 300, 40, 650, 250) # 하위 버튼 디자인
    communication_button.color = (0,0,0)
    communication_button.textsize = 20
    communication_button.font = 'pixel.ttf'

    onoff_button = button("전원 키기", 300, 40, 650, 200) # 하위 버튼 디자인
    onoff_button.color = (0,0,0)
    onoff_button.textsize = 20
    onoff_button.font = 'pixel.ttf'

    control_button = button("문 제어 장치", 300, 40, 650, 250) # 하위 버튼 디자인
    control_button.color = (0,0,0)
    control_button.textsize = 20
    control_button.font = 'pixel.ttf'

    cctv_button = button("CCTV", 300, 40, 650, 300) # 하위 버튼 디자인
    cctv_button.color = (0,0,0)
    cctv_button.textsize = 20
    cctv_button.font = 'pixel.ttf'

    bgimg = pygame.image.load('images/a_system.png')
    bgimg = pygame.transform.scale(bgimg, (560, 560))

    t_surface = screen.convert_alpha()
    t_surface.fill((0,0,0,0))
    
    # mode1['system'] = True
    while run:
        # 세팅 [ 건드리지 말아야 할 것]
        screen.fill(pygame.color.Color(50, 50, 50))
        pygame.draw.rect(screen, (20,20,20), [20, 20, 560, 560])
        screen.blit(bgimg, (20, 20))
        # main [여기에 코드 입력] > 이미지 오브젝트, 텍스트(prtext) 등등
        
        # | UI |
        prtext4("시스템실 | A-5", 'pixel.ttf', 20, 30, 30) # 여기는 바꿔도 됨
        drawui()
        textls()
        textprinting()
        if time2 == 1:
            primg2('images/talk1.png', 20, 20)
        if time2 == 2:
            primg2('images/talk2.png', 20, 20)
        # | 버튼 그리는 곳 |
        find_button.off()
        security_button.off()
        communication_button.off()
        onoff_button.off()
        control_button.off()
        cctv_button.off()
        if buttonmode == 1: # 이동목록 켜진 경우
            move_button.txt = '< 뒤로'
            security_button.on()
            communication_button.on()
        elif buttonmode == 2:
            move_button.txt = '< 뒤로'
            onoff_button.on()
            control_button.on()
        else: # 꺼진 경우
            move_button.txt = '이동목록'
            find_button.on()

        move_button.draw()
        find_button.draw()
        security_button.draw()
        communication_button.draw()
        onoff_button.draw()
        control_button.draw()
        cctv_button.draw()

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
                buttonmode = 2
            if security_button.check() == 1:
                if '카드키' in getitem():
                    a_security2.maprun()
                else:
                    setscr(3)
            if communication_button.check() == 1:
                if '카드키' in getitem():
                    a_communication.maprun()
                else:
                    setscr(3)
            # 2
            if onoff_button.check() == 1:
                if [mode1['electric'],mode1['wire1']] == [True,True]:
                    if mode1['system'] == False:
                        setscr(5)
                        mode1['system'] = True
                    else:
                        setscr(6)
                else:
                    setscr(4)
            if control_button.check() == 1:
                if mode1['system'] == True:
                    if mode1['main_event'] == 2:
                        a_system1.maprun()
                    else:
                        setscr(10)
                else:
                    setscr(7)
        if pygame.mouse.get_pressed()[0] == 1:
            pass
        # key

        if pygame.key.get_pressed()[pygame.K_m]:
            Sound_controll.sound_controll()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if time2 == 1:
                    time2 += 1
                    setscr(9)
                elif time2 == 2:
                    time2 = 0
                    t1.md = 0
                    t1.mm = 0
                    setscr(0)
        
        #fin [끝]
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    maprun()