# -*- coding: utf-8 -*-

import pygame
import sys
from module1 import *
from main1 import *
from but import *

font1 = 'gulim.ttf'

pygame.init() 
screen = pygame.display.set_mode((1000, 600)) 

pygame.display.set_caption("Moon Side")

clock = pygame.time.Clock()
run = True
myFont = pygame.font.Font(font1, 25)

def get_rend(txt, sz):
    myFont = pygame.font.Font(font1, sz)
    text_title = myFont.render(txt, False, (255, 255, 255))
    t_rect = text_title.get_rect()
    return t_rect.width

class button1:
    color = (150,150,0)
    textcolor = (255,255,255)
    textsize = 25
    cool = 0
    count = 0
    onoff = 1
    font = 'gulim.ttf'
    item = []
    checkon = 1
    def __init__(self, txt, sx, sy, x, y, fuse):
        self.txt = txt
        self.sx = sx
        self.sy = sy
        self.x = x
        self.y = y
        self.fuse = fuse
    def draw(self):
        if self.onoff == 1:
            # t_surface = screen.convert_alpha()
            # t_surface.fill((0,0,0,0))
            if self.check() == 0:
                # pygame.draw.rect(t_surface, (0,0,0,0), (self.x, self.y, self.sx, self.sy))
                pass
            else:
                # pygame.draw.rect(t_surface, (0,0,0,0), (self.x, self.y, self.sx, self.sy))
                if 580 > pygame.mouse.get_pos()[0] > 20 and 580 > pygame.mouse.get_pos()[1] > 20 and self.checkon == 1:
                    pygame.draw.rect(screen, (255 - self.clicking() * 100,255 - self.clicking() * 100,255), (self.x, self.y, self.sx, self.sy), 2 - (self.clicking() * 1))
                # prtextm("클릭", 10, self.x + self.sx / 2, self.y + self.sy / 2)
            self.prtext(self.txt, self.textsize, (self.x + self.sx / 2), (self.y + self.sy / 2))
        else:
            pass
    def check(self):
        if self.onoff == 1 and self.fuse == 0:
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
        if self.onoff == 1 and self.fuse == 0:
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
        if self.onoff == 1 and self.fuse == 0:
            if pygame.mouse.get_pressed()[0]:
                if self.check() == 1:
                    return 1
                else:
                    return 0
            else:
                return 0
        else:
            return 0
    def clicking2(self):
        if self.onoff == 1 and self.fuse == 0:
            if pygame.mouse.get_pressed()[2]:
                if self.check() == 1:
                    return 1
                else:
                    return 0
            else:
                return 0
        else:
            return 0
    def prtext(self, txt, sz, x, y):
        # myFont = pygame.font.Font(font1, sz)
        text_title = myFont.render(txt, False, self.textcolor)
        t_rect = text_title.get_rect()
        t_rect.centerx = x
        t_rect.centery = y
        screen.blit(text_title, t_rect)
    def on(self):
        self.onoff = 1
    def off(self):
        self.onoff = 0

class showitems():
    itemmode = 0
    buttonlist = []
    mode = 1
    # itemclass
    onoff = 0
    mousex = 0
    itemall = 0
    lx = 0
    o = 0
    itemlist = []
    reseted = 0 # 1일 경우 초기화
    il = 0
    fuse = 1
    clicking_i = ""
    clicking_i_a = 0
    clicking = 0
    plpl = ""
    plpl2 = ""
    plpl3 = ""
    isinv = 0
    i = 0
    buttonnum = 0
    massitem = 0
    floornm = ''
    intro = 0 # 현재 클릭중인 거 표현
    storage = 0
    intro2 = ['None', 0, 0] # [가장 최근에 클릭된 아이템, 온오프, 번호]
    def reseted1(self):
        if self.reseted == 1:
            self.intro2 = ['None', 0]
            # for item in self.buttonlist:
            #     del item
            self.buttonlist = []
            for item in self.itemlist:
                self.buttonlist.append(button1(item, get_rend(item, 25) + 10, 50, 0,580-50, self.mode))
            self.reseted = 0
    def __init__(self):
        pass
    def getbutton(self):
        pass
    
    def draw(self):
        if self.onoff == 1:
            if pygame.mouse.get_pressed()[0]:
                if self.check() == 1 and self.mode == 1:
                    if self.o == 1:
                        self.mousex += pygame.mouse.get_pos()[0] - self.lx
            # if self.mousex > 0:
            #     self.mousex = 0
            t_surface = screen.convert_alpha()
            t_surface.fill((0,0,0,0))
            t_surface2 = screen.convert_alpha()
            t_surface2.fill((0,0,0,0))
            pygame.draw.rect(t_surface, (0,0,0,200), [20, 530, 560, 50])
            pygame.draw.rect(t_surface, (0,0,0,200), [20, 500, 560, 30])
            pygame.draw.rect(t_surface, (255,255,255,100), [20, 530, 560, 1])
            pygame.draw.rect(t_surface, (255,255,255,100), [20, 500, 560, 1])
            screen.blit(t_surface, (0,0))
            self.i = 0
            self.il = 40
            self.reseted1() # 리셋 확인
            self.plpl3 = "" 
            self.intro = 0
            self.storage = 0
            if pygame.mouse.get_pressed()[2] == False:
                self.introtiming = 0
            for item in item_t:
                self.storage += item_y[item]
            # buttonlist
            for item in self.buttonlist:
                item.checkon = 1
                if self.clicking == 1:
                    self.intro2[1] = 0
                    if item == self.clicking_i:
                        pass
                    else:
                        item.checkon = 0
                item.fuse = self.mode
                item.x = self.il + self.mousex
                self.il += item.sx + 20
                if 580 > pygame.mouse.get_pos()[0] > 20 and 580 > pygame.mouse.get_pos()[1] > 20 and self.clicking == 1:
                    self.clicking_i.x = pygame.mouse.get_pos()[0] - self.clicking_i.sx / 2
                    self.clicking_i.y = pygame.mouse.get_pos()[1] - 20
                else:
                    item.y = 580 - 50
                if 580 > pygame.mouse.get_pos()[0] > 20 and 580 > pygame.mouse.get_pos()[1] > 20 and item.check() == 1 and self.mode == 0:
                    try:
                        self.plpl3 = item.txt + "[" + str(item_y[item.txt]) + "]" + " : " + item_s[item.txt]
                    except:
                        self.plpl3 = item.txt + "[" + str(item_y[item.txt]) + "]"
                if 580 > pygame.mouse.get_pos()[0] > 20 and 580 > pygame.mouse.get_pos()[1] > 20 and item.clicking2() == 1 and self.mode == 0:
                    self.intro = item.txt
                    if self.introtiming == 0:
                        if self.intro2[0] == item.txt and self.intro2[2] == self.i:
                            if self.intro2[1] == 0:
                                if self.clicking == 0:
                                    self.intro2[1] = 1
                            else:
                                self.intro2[1] = 0
                        else:
                            self.intro2 = [item.txt, 1, self.i]
                    self.introtiming = 1
                if 580 > pygame.mouse.get_pos()[0] > 20 and 580 > pygame.mouse.get_pos()[1] > 20 and self.mode == 0 and item.clicking() == 1 and self.clicking == 0:
                    self.clicking_i = item
                    self.clicking_i_a = item_y[item.txt]
                    self.clicking = 1
                    self.buttonnum = self.i
                if pygame.mouse.get_pressed()[0] == 0:
                    if self.clicking == 1:
                        if 580 > pygame.mouse.get_pos()[0] > 20 and 500 > pygame.mouse.get_pos()[1] > 20:
                            if self.isinv == 'inv':
                                self.massitem = self.clicking_i.txt
                                del self.buttonlist[self.buttonnum]
                                del item_t[self.buttonnum]
                            else:
                                if self.storage + self.clicking_i_a <= 100:
                                    self.massitem = self.clicking_i.txt
                                    del self.buttonlist[self.buttonnum]
                                    delxllist(self.isinv.item[0], self.isinv.item[1], self.buttonnum)
                                    # del self.isinv.item[self.buttonnum]
                        self.clicking_i_a = 0
                    self.clicking = 0
                item.draw()
                if item.clicking() == 0:
                    pygame.draw.rect(t_surface2, (255,255,255,70), [item.x + item.sx + 10, 535, 1, 40])
                    pygame.draw.rect(t_surface2, (255,255,255,70), [item.x - 10, 535, 1, 40])
                self.i += 1
            # button fin
            # trash or getitem
            if self.massitem == 0:
                pass
            else:
                if self.isinv == 'inv':
                    pass
                else:
                    item_t.append(self.massitem)
                    self.massitem = 0

            if self.mode == 1:
                self.plpl = "좌우 드래그로 살펴보기"
            else:
                self.plpl = "좌클릭 : 아이템 이동 / 우클릭 : 상호작용"
            if self.isinv == 'inv':
                self.plpl2 = "소지품 " + str(self.storage) + "/100"
            else:
                self.plpl2 = self.isinv.txt
            if len(self.plpl3) == 0:
                prtext2(self.plpl2 + " | " + self.plpl + " | " + self.plpl3, 15, 40, 510)
            else:
                prtext2(self.plpl3, 15, 40, 510)
            if len(self.buttonlist) == 0:
                prtextm('비어 있습니다, 다른 오브젝트를 찾으십시오.', 20, 300, 555)

            self.lx = pygame.mouse.get_pos()[0]
            self.o = 1
            if pygame.mouse.get_pressed()[0] == 0:
                self.o = 0
                if self.mousex > 0:
                    self.mousex -= self.mousex / 5 + 1
                    if self.mousex < 2:
                        self.mousex = 0
                if self.il > 560:
                    if 560 - self.mousex > self.il:
                        self.mousex += (560 - self.mousex - self.il) / 5 + 1
                        if self.mousex > 560 - self.il - 2:
                            self.mousex = 560 - self.il - 2
                        # self.mousex = 560 - get_rend(il, 25) - 20
                else:
                    if self.mousex < 0:
                        self.mousex += -self.mousex / 5 + 1
                        if self.mousex > -2:
                            self.mousex = 0
                        # self.mousex = 0
            screen.blit(t_surface2, (0,0))
                        
    def check(self):
        if pygame.mouse.get_pos()[0] > 20 and pygame.mouse.get_pos()[0] < 580:
            if pygame.mouse.get_pos()[1] > 530 and pygame.mouse.get_pos()[1] < 580:
                return 1
            else:
                return 0
        else:
            return 0
    def on(self):
        self.onoff = 1
        self.mousex = 0
        self.o = 0
    def off(self):
        self.onoff = 0
        self.mousex = 0
        self.o = 0
        self.intro2 = ['None', 0, 0]
    def itemset(self, pp):
        self.itemlist = pp
    def drawrect(self, txt, sx, sy, x, y):
            t_surface = screen.convert_alpha()
            t_surface.fill((0,0,0,0))
            lll = pygame.Rect(0, 0, sx, sy)
            lll.centerx = x
            lll.centery = y
            pygame.draw.rect(t_surface, (0,0,0,200), lll)
            screen.blit(t_surface, (0,0))
            prtextm(txt, 20, x, y)
    def use(self):
        del self.buttonlist[self.intro2[2]]
        if self.isinv == 'inv':
            item_t.pop(self.intro2[2])
        else:
            delxllist(self.isinv.item[0], self.isinv.item[1], self.intro2[2])
