# -*- coding: utf-8 -*-

import pygame
import sys
from module1 import *
from item import *
import game_over

pygame.init()
screen = pygame.display.set_mode((600, 800))
clock = pygame.time.Clock()

class button:
    color = (150,150,0)
    textcolor = (255,255,255)
    textsize = 25
    cool = 0
    count = 0
    onoff = 1
    font = 'gulim.ttf'
    item = ['main', 50]
    thick = 0
    def __init__(self, txt, sx, sy, x, y):
        self.txt = txt
        self.sx = sx
        self.sy = sy
        self.x = x
        self.y = y
    def draw(self):
        if self.onoff == 1:
            if self.check() == 0:
                pygame.draw.rect(screen, self.color, (self.x, self.y, self.sx, self.sy))
                if self.thick > 0:
                    pygame.draw.rect(screen, (100,150,100), (self.x, self.y, self.sx, self.sy), self.thick)
            else:
                pygame.draw.rect(screen, (self.color[0]/2,self.color[1]/2,self.color[2]/2), (self.x, self.y, self.sx, self.sy))
                pygame.draw.rect(screen, (255,255,255), (self.x, self.y, self.sx, self.sy), 3 - (self.clicking() * 2))
            self.prtext(self.txt, self.textsize, (self.x + self.sx / 2), (self.y + self.sy / 2))
        else:
            pass
    def check(self):
        if self.onoff == 1:
            if pygame.mouse.get_pos()[0] > self.x and pygame.mouse.get_pos()[0] < self.x + self.sx:
                if pygame.mouse.get_pos()[1] > self.y and pygame.mouse.get_pos()[1] < self.y + self.sy:
                    return 1
                else:
                    return 0
            else:
                return 0
        else:
            return 0
    def clicked(self):
        if self.onoff == 1:
            if pygame.mouse.get_pressed()[0]:
                if self.check() == 1:
                    if self.cool == 0:
                        self.cool = 1
                        return 1
                    else:
                        return 0
                else:
                    self.cool = 0
                    return 0
            else:
                self.cool = 0
                return 0
        else:
            return 0
    def clicking(self):
        if self.onoff == 1:
            if pygame.mouse.get_pressed()[0]:
                if self.check() == 1:
                    return 1
                else:
                    return 0
            else:
                return 0
        else:
            return 0
    def prtext(self, txt, sz, x, y):
        myFont = pygame.font.Font(self.font, sz)
        text_title = myFont.render(txt, False, self.textcolor)
        t_rect = text_title.get_rect()
        t_rect.centerx = x
        t_rect.centery = y
        screen.blit(text_title, t_rect)
    def on(self):
        self.onoff = 1
    def off(self):
        self.onoff = 0

class itemobject:
    color = (150,150,0)
    textcolor = (255,255,255)
    textsize = 15
    cool = 0
    count = 0
    onoff = 1
    font = 'gulim.ttf'
    item = ['main', 50]
    item_list = []
    finding_time = 0
    offwait = 0
    def __init__(self, name, txt, sx, sy, x, y):
        self.txt = txt
        self.sx = sx
        self.sy = sy
        self.x = x
        self.y = y
        self.name = name
        self.img = pygame.image.load(self.name)
        self.img = pygame.transform.scale(self.img, (self.sx, self.sy))
    def draw(self):
        if pygame.mouse.get_pressed()[0] == 0 or self.check() == 0:
            self.finding_time = 0
        if self.onoff == 1:
            if self.name != 'images/none.png':
                screen.blit(self.img, [self.x, self.y])
            #primg2(self.name, self.x, self.y)
            if self.check() == 0 or itemui.clicking == 1:
                pass
            else:
                t_surface = screen.convert_alpha()
                t_surface.fill((0,0,0,0))
                if itemui.isinv != 'inv' and type(itemui.isinv) != int:
                    if itemui.isinv.txt == self.txt and itemui.onoff == 1:
                        pygame.draw.rect(t_surface, (0,150,0,100), (pygame.mouse.get_pos()[0]-40, pygame.mouse.get_pos()[1]-30, 80, 20))
                    else:
                        pygame.draw.rect(t_surface, (0,0,0,100), (pygame.mouse.get_pos()[0]-40, pygame.mouse.get_pos()[1]-30, 80, 20))
                else:
                    pygame.draw.rect(t_surface, (0,0,0,100), (pygame.mouse.get_pos()[0]-40, pygame.mouse.get_pos()[1]-30, 80, 20))
                screen.blit(t_surface, (0,0))
                self.prtext("살펴보기", self.textsize, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1] - 20)
        else:
            pass
    def check(self):
        if self.onoff == 1:
            if pygame.mouse.get_pos()[0] > self.x and pygame.mouse.get_pos()[0] < self.x + self.sx:
                if pygame.mouse.get_pos()[1] > self.y and pygame.mouse.get_pos()[1] < self.y + self.sy:
                    return 1
                else:
                    return 0
            else:
                return 0
        else:
            return 0
    def clicked(self):
        if self.onoff == 1:
            if pygame.mouse.get_pressed()[0]:
                if self.check() == 1:
                    if self.cool == 0:
                        self.cool = 1
                        return 1
                    else:
                        return 0
                else:
                    self.cool = 0
                    return 0
            else:
                self.cool = 0
                return 0
        else:
            return 0
    def clicking(self):
        if self.onoff == 1:
            if pygame.mouse.get_pressed()[0]:
                if self.check() == 1:
                    return 1
                else:
                    return 0
            else:
                return 0
        else:
            return 0
    def prtext(self, txt, sz, x, y):
        myFont = pygame.font.Font(self.font, sz)
        text_title = myFont.render(txt, False, self.textcolor)
        t_rect = text_title.get_rect()
        t_rect.centerx = x
        t_rect.centery = y
        screen.blit(text_title, t_rect)
    def on(self):
        self.onoff = 1
    def off(self):
        self.onoff = 0

class imagebutton:
    color = (150,150,0)
    textcolor = (255,255,255)
    textsize = 15
    cool = 0
    count = 0
    onoff = 1
    font = 'gulim.ttf'
    item = ['main', 50]
    item_list = []
    mode = 0
    getted = 0
    seetxt = "살펴보기"
    def __init__(self, name, sx, sy, x, y):
        self.sx = sx
        self.sy = sy
        self.x = x
        self.y = y
        self.name = name
        self.img = pygame.image.load(self.name)
        self.img = pygame.transform.scale(self.img, (self.sx, self.sy))
    def draw(self):
        if self.onoff == 1:
            if self.name != 'images/none.png':
                screen.blit(self.img, [self.x, self.y])
            if self.check() == 0 or itemui.clicking == 1:
                pass
            else:
                if self.mode == 0:
                    t_surface = screen.convert_alpha()
                    t_surface.fill((0,0,0,0))
                    pygame.draw.rect(t_surface, (0,0,0,100), (pygame.mouse.get_pos()[0]-40, pygame.mouse.get_pos()[1]-30, 80, 20))
                    screen.blit(t_surface, (0,0))
                    self.prtext(self.seetxt, self.textsize, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1] - 20)
        else:
            pass
    def check(self):
        if self.onoff == 1:
            if pygame.mouse.get_pos()[0] > self.x and pygame.mouse.get_pos()[0] < self.x + self.sx:
                if pygame.mouse.get_pos()[1] > self.y and pygame.mouse.get_pos()[1] < self.y + self.sy:
                    return 1
                else:
                    return 0
            else:
                return 0
        else:
            return 0
    def clicked(self):
        if self.onoff == 1:
            if pygame.mouse.get_pressed()[0]:
                if self.check() == 1:
                    if self.cool == 0:
                        self.cool = 1
                        return 1
                    else:
                        return 0
                else:
                    self.cool = 0
                    return 0
            else:
                self.cool = 0
                return 0
        else:
            return 0
    def clicking(self):
        if self.onoff == 1:
            if pygame.mouse.get_pressed()[0]:
                if self.check() == 1:
                    return 1
                else:
                    return 0
            else:
                return 0
        else:
            return 0
    def prtext(self, txt, sz, x, y):
        myFont = pygame.font.Font(self.font, sz)
        text_title = myFont.render(txt, False, self.textcolor)
        t_rect = text_title.get_rect()
        t_rect.centerx = x
        t_rect.centery = y
        screen.blit(text_title, t_rect)
    def on(self):
        self.onoff = 1
    def off(self):
        self.onoff = 0
    def changeimg(self, nm):
        self.img = pygame.image.load(nm)
        self.img = pygame.transform.scale(self.img, (self.sx, self.sy))


item_button = button("I", 30, 30, 550, 550)
item_button.color = (100, 0, 0)

# itemmode_button = button("보기 모드", 80, 30, 470, 550)
# itemmode_button.textsize = 15
# itemmode_button.color = (20,20,20)

floor_button = button("버려진 아이템 보기", 150, 30, 400, 440)
floor_button.textsize = 15
floor_button.color = (20,20,20)
floor_button.thick = 0
floor_button.onoff = 0

itemui = showitems()
itemui.floornm = floor_button
itemui.mode = 1

t_surface = screen.convert_alpha()
t_surface.fill((0,0,0,0))

itemusing = 580
itemon = 0
nowitem = ''

hunger = 100
hunger_cool = 0

bookn = 0
prev_button = imagebutton('images/none.png', 100, 100, 100, 300)
next_button = imagebutton('images/none.png', 100, 100, 400, 300)
usingitem = ''

def hungeradd(a):
    global hunger
    hunger += a
    if hunger > 100:
        hunger = 100


def mapdraw(): # 아이템 상호작용
    global itemusing
    global nowitem
    global bookn
    global usingitem
    itemon = 0
    # event = pygame.event.poll()
    if pygame.key.get_pressed()[pygame.K_x]:
        itemui.intro2[1] = 0
    if [itemui.intro2[0], itemui.intro2[1]] == ['지도', 1]:
        # pygame.draw.rect(t_surface, (0, 0, 0, 150), [20, 20, 560, 560])
        # screen.blit(t_surface, (0,0))
        # primg2("map560.png", 20, 20)
        itemon = 1
        nowitem = 'map560.png'
    prev_button.off()
    next_button.off()
    if [itemui.intro2[0], itemui.intro2[1]] == ['만화책', 1]:
        itemon = 1
        nowitem = 'map560.png'
        prev_button.on()
        next_button.on()
        if prev_button.clicking() == 1:# previous
            pass
        if next_button.clicking() == 1:# next
            pass
    
    if [itemui.intro2[0], itemui.intro2[1]] == ['카드키', 1]:
        itemon = 1
        nowitem = 'images/cardkey.png'
    if [itemui.intro2[0], itemui.intro2[1]] == ['연구노트', 1]:
        itemon = 1
        nowitem = 'images/labbook.png'
        mode1['seenote'] = 1
    if [itemui.intro2[0], itemui.intro2[1]] == ['손전등', 1]:
        mode1['light'] = True
        itemui.use()
        actionbar.print('손전등을 장착했다')
    # [ 이 아래로는 건드리지 마시오 ]
    if [itemui.intro2[0], itemui.intro2[1]] == ['빵', 1]:
        itemui.intro2[1] = 0
        itemui.use()
        hungeradd(20)
    if itemon == 1:
        if itemui.intro2[1] == 1:
            itemusing -= itemusing/8 + 1
            if itemusing < 20:
                itemusing = 20
            if usingitem != itemui.intro2[0]:
                usingitem = itemui.intro2[0]
                itemusing = 580
    else:
        if itemui.intro2[1] == 0:
            itemusing += (580-itemusing)/8 + 1
            if itemusing > 580:
                itemusing = 580
    
    if itemusing < 580:
        pygame.draw.rect(t_surface, (0, 0, 0, (1-itemusing/580)*200), [20, 20, 560, 560])
        screen.blit(t_surface, (0,0))
        primg2(nowitem, 20, itemusing)
        if itemusing == 20:
            prtextm2('Press X to exit', 25, 300, 560, (255,255,255), ft='moon.otf')
        # buttondraw
        prev_button.draw()
        next_button.draw()

def drawui():
    global hunger
    global hunger_cool
    if itemui.onoff == 1:
        # itemmode_button.on()
        item_button.y = 440
        floor_button.on()
    else:
        # itemmode_button.off()
        item_button.y = 550
        floor_button.off()
    # print(itemui.storage + itemui.clicking_i_a)

    # | hunger system / 배고픔 시스템 |
    pygame.draw.rect(screen, (150,0,0), [30, 55, 200, 30])
    pygame.draw.rect(screen, (255,255,255), [30, 55, hunger * 2, 30])
    # pygame.draw.rect(screen, (255,255,0), [30, 55, hunger * 2 - hunger_cool/240 * hunger * 2, 30])
    prtextm2(str(hunger) + '/100', 30, 130, 70, (0,0,0), ft = 'pixel.ttf')

    hunger_cool += 1
    if hunger_cool > 240:
        hunger_cool = 0
        hunger -= 1
    if hunger < 1: # game over
        hunger = 0
        game_over.maprun()

    if itemui.intro2[0] in item_f:
        if type(item_f[itemui.intro2[0]]) == int:
            hunger += item_f[itemui.intro2[0]]
            itemui.use()
            itemui.intro2 = ['None', 0, 0]
    if hunger > 100:
        hunger = 100
    
    #item trash
    if itemui.clicking == 1:
        if itemui.isinv == 'inv':
            if 580 > pygame.mouse.get_pos()[0] > 20 and 470 > pygame.mouse.get_pos()[1] > 20:
                drawrect("바닥에 버리기", 540, 480, 300, 260, (0,80,0,150))
            else:
                drawrect("바닥에 버리기", 540, 480, 300, 260, (0,0,0,150))
        else:
            if itemui.storage + itemui.clicking_i_a > 100:
                drawrect("인벤토리에 공간이 부족합니다", 540, 480, 300, 260, (100,0,0,150))
            else:
                if 580 > pygame.mouse.get_pos()[0] > 20 and 470 > pygame.mouse.get_pos()[1] > 20:
                    drawrect("인벤토리에 넣기", 540, 480, 300, 260, (0,80,0,150))
                else:
                    drawrect("인벤토리에 넣기", 540, 480, 300, 260, (0,0,0,150))
    itemui.draw()
    pygame.draw.rect(screen, (50,50,50), [0, 0, 20, 600])
    pygame.draw.rect(screen, (50,50,50), [580, 0, 420, 600])
    pygame.draw.rect(screen, (255,255,255), [599.5, 20, 1, 560])
    item_button.draw()
    actionbar.draw()
    # itemmode_button.draw()
    msitem = getmassitem()
    itemui.massitem = 0
    floor_button.draw()

    if msitem == 0:
        pass
    else:
        # floor_button.item.append(msitem)
        addxllist(floor_button.item[0], floor_button.item[1], msitem)
        msitem = 0
    # if itemui.clicking == 1:
    #     if itemui.isinv == 'inv':
    #         drawrect("바닥에 버리기", 540, 480, 300, 260)
    #     else:
    #         drawrect("인벤토리에 넣기", 540, 480, 300, 260)
    mapdraw()
    # primg2('images/cursor.png', pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
map_onoff = 0

def itemcheck(buttonnm): # buttonnm : 버튼이름 / 이미지오브젝트 이름
    if buttonnm.check() == 1:
        if itemui.onoff == 0:
            itemui.mode = 1
            itemui.on()
        else:
            if itemui.isinv == buttonnm:
                itemui.off()
        itemui.itemlist = getxllist(buttonnm.item[0], buttonnm.item[1]) # 엑셀에서 가져오기
        itemui.itemlist.pop(0)
        itemui.mousex = 0
        itemui.reseted = 1
        itemui.isinv = buttonnm

def itemcheck2(buttonnm): # buttonnm : 버튼이름 / 이미지오브젝트 이름
    if buttonnm.check() == 1 and itemui.clicking == 0:
        if buttonnm.finding_time < 61:
            pygame.draw.rect(screen, (250,0,0), [pygame.mouse.get_pos()[0]-40, pygame.mouse.get_pos()[1]-40, (60-buttonnm.finding_time)/60*80, 10])
        if buttonnm.finding_time < 61:
            buttonnm.finding_time += 1
        if itemui.onoff == 0:
            if buttonnm.finding_time == 60:
                itemui.mode = 1
                itemui.on()
            buttonnm.offwait = 0
        else:
            if itemui.isinv == buttonnm and buttonnm.finding_time < 60:
                buttonnm.offwait += 1
                if buttonnm.offwait > 1:
                    itemui.off()
        if buttonnm.finding_time == 60:
            itemui.itemlist = getxllist(buttonnm.item[0], buttonnm.item[1]) # 엑셀에서 가져오기
            itemui.itemlist.pop(0)
            itemui.mousex = 0
            itemui.reseted = 1
            itemui.isinv = buttonnm
    else:
        buttonnm.offwait = 0

def buttoncheck():
    if item_button.check() == 1:
        if itemui.onoff == 0:
            itemui.mode = 1
            itemui.on()
        else:
            if itemui.itemlist == getitem():
                itemui.off()
        itemui.itemlist = getitem()
        itemui.mousex = 0
        itemui.reseted = 1
        itemui.isinv = 'inv'
    itemcheck(floor_button)
    # if itemmode_button.check() == 1:
    #     if itemui.mode == 1:
    #         itemui.mode = 0
    #     else:
    #         itemui.mode = 1

def getmassitem():
    if itemui.massitem == 0:
        return 0
    else:
        return itemui.massitem
        itemui.massitem = 0

def drawrect(txt, sx, sy, x, y, *col):
    # t_surface = screen.convert_alpha()
    # t_surface.fill((0,0,0,0))
    lll = pygame.Rect(0, 0, sx, sy)
    lll.centerx = x
    lll.centery = y
    pygame.draw.rect(t_surface, col, lll)
    screen.blit(t_surface, (0,0))
    prtextm(txt, 20, x, y)

# variable(버튼이름) = button(text, width, height, x좌표, y좌표)
# variable.draw() // 버튼을 화면에 출력
# variable.check() // 버튼 위에 마우스가 있다면 1, 아니면 0출력
# variable.color = (R,G,B) // 버튼 색 설정
# variable.textcolor = (R,G,B) // 텍스트 색 설정
# variable.textsize = (텍스트사이즈)
# variable.item // 버튼의 고유 아이템

# 아이템 모듈
# itemui.intro // 현재 상호작용중인 아이템 이름
# itemcheck(버튼이름) // 버튼에 해당하는 아이템 보기

t1 = prtext3("", 20, 1)

def textprinting(): # 텍스트 출력
    t1.printing(0, 0)

def textprinting2(): # 텍스트 출력
    t1.printing(0, 1)

def firstsetting():
    itemui.off()
    itemui.intro2 = ['None', 0, 0]
    t1.mode = 0
    pygame.mouse.set_visible(True)

def mousechange():
    # pygame.mouse.set_visible(False)
    # if pygame.mouse.get_pressed()[0] == 1:
    #     primg2('images/cursor2.png', pygame.mouse.get_pos()[0]-10, pygame.mouse.get_pos()[1]-10)
    # else:
    #     primg2('images/cursor.png', pygame.mouse.get_pos()[0]-10, pygame.mouse.get_pos()[1]-10)
    pass
