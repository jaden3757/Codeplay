# -*- coding: utf-8 -*-

import pygame
import sys
from module1 import *
from item import *

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
        if self.onoff == 1:
            screen.blit(self.img, [self.x, self.y])
            #primg2(self.name, self.x, self.y)
            if self.check() == 0 or itemui.clicking == 1:
                pass
            else:
                t_surface = screen.convert_alpha()
                t_surface.fill((0,0,0,0))
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
            screen.blit(self.img, [self.x, self.y])
            #primg2(self.name, self.x, self.y)
            # if self.check() == 0 or itemui.clicking == 1:
            #     pass
            # else:
            #     t_surface = screen.convert_alpha()
            #     t_surface.fill((0,0,0,0))
            #     pygame.draw.rect(t_surface, (0,0,0,100), (pygame.mouse.get_pos()[0]-40, pygame.mouse.get_pos()[1]-30, 80, 20))
            #     screen.blit(t_surface, (0,0))
            #     self.prtext("살펴보기", self.textsize, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1] - 20)
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

itemmode_button = button("보기방식", 80, 30, 470, 550)
itemmode_button.textsize = 15
itemmode_button.color = (20,20,20)

floor_button = button("버려진 아이템", 100, 30, 370, 470)
floor_button.textsize = 15
floor_button.color = (20,20,20)
floor_button.thick = 0
floor_button.onoff = 0

itemui = showitems()
itemui.floornm = floor_button

def mapdraw():
    if [itemui.intro2[0], itemui.intro2[1]]== ['지도', 1]:
        t_surface = screen.convert_alpha()
        t_surface.fill((0,0,0,0))
        pygame.draw.rect(t_surface, (0, 0, 0, 150), [20, 20, 560, 560])
        screen.blit(t_surface, (0,0))
        primg("map560.png", 560, 560, 20, 20)

def drawui():
    global hunger
    global hunger_cool
    if itemui.onoff == 1:
        itemmode_button.on()
        item_button.y = 470
        itemmode_button.y = 470
        floor_button.on()
    else:
        itemmode_button.off()
        item_button.y = 550
        itemmode_button.y = 550
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
        pass
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
            if 580 > pygame.mouse.get_pos()[0] > 20 and 500 > pygame.mouse.get_pos()[1] > 20:
                drawrect("바닥에 버리기", 540, 480, 300, 260, (0,80,0,150))
            else:
                drawrect("바닥에 버리기", 540, 480, 300, 260, (0,0,0,150))
        else:
            if itemui.storage + itemui.clicking_i_a > 100:
                drawrect("인벤토리에 공간이 부족합니다", 540, 480, 300, 260, (100,0,0,150))
            else:
                if 580 > pygame.mouse.get_pos()[0] > 20 and 500 > pygame.mouse.get_pos()[1] > 20:
                    drawrect("인벤토리에 넣기", 540, 480, 300, 260, (0,80,0,150))
                else:
                    drawrect("인벤토리에 넣기", 540, 480, 300, 260, (0,0,0,150))
    itemui.draw()
    pygame.draw.rect(screen, (50,50,50), [0, 0, 20, 600])
    pygame.draw.rect(screen, (50,50,50), [580, 0, 420, 600])
    pygame.draw.rect(screen, (255,255,255), [599.5, 20, 1, 560])
    item_button.draw()
    itemmode_button.draw()
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
    if itemmode_button.check() == 1:
        if itemui.mode == 1:
            itemui.mode = 0
        else:
            itemui.mode = 1

def getmassitem():
    if itemui.massitem == 0:
        return 0
    else:
        return itemui.massitem
        itemui.massitem = 0

def drawrect(txt, sx, sy, x, y, *col):
    t_surface = screen.convert_alpha()
    t_surface.fill((0,0,0,0))
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