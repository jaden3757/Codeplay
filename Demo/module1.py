# -*- coding: utf-8 -*-

import pygame
import sys

font1 = 'gulim.ttf'
screen = pygame.display.set_mode((600, 800)) 

def prtext(txt, sz, y):
    myFont = pygame.font.Font(font1, sz)
    text_title = myFont.render(txt, False, (255, 255, 255))
    t_rect = text_title.get_rect()
    t_rect.left = 600
    t_rect.top = 20 + y
    screen.blit(text_title, t_rect)

def prtext2(txt, sz, x, y):
    myFont = pygame.font.Font(font1, sz)
    text_title = myFont.render(txt, False, (255, 255, 255))
    screen.blit(text_title, [x, y])

def prtext4(txt, ft, sz, x, y): # choose font
    myFont = pygame.font.Font(ft, sz)
    text_title = myFont.render(txt, False, (255, 255, 255))
    screen.blit(text_title, [x, y])

def prtext5(txt, ft, sz, x, y, *col): # choose font
    myFont = pygame.font.Font(ft, sz)
    text_title = myFont.render(txt, False, col)
    screen.blit(text_title, [x, y])

def prtextm(txt, sz, x, y):
    myFont = pygame.font.Font(font1, sz)
    text_title = myFont.render(txt, False, (255, 255, 255))
    t_rect = text_title.get_rect()
    t_rect.centerx = x
    t_rect.centery = y
    screen.blit(text_title, t_rect)

def prtextm2(txt, sz, x, y, *col, ft):
    myFont = pygame.font.Font(ft, sz)
    text_title = myFont.render(txt, False, col)
    t_rect = text_title.get_rect()
    t_rect.centerx = x
    t_rect.centery = y
    screen.blit(text_title, t_rect)

def primg(name, sclx, scly, x, y):
    img = pygame.image.load(name)
    #screen.blit(img, (x, y))

    img = pygame.transform.scale(img, (sclx, scly)) # 스케일 변환

    screen.blit(img, (x, y))

def primg2(name, x, y):
    img = pygame.image.load(name)
    #screen.blit(img, (x, y))
    screen.blit(img, (x, y))

class prtext3:
    done = 0
    wait = 0
    line2 = 0
    txt = []
    leng = 0
    p = 0
    l = 0
    io = 0
    p2 = 0
    p3 = 0
    waiti = 0
    mm = 0
    md = 0
    mode = 0
    def __init__(self, txt, sz, speed):
        self.w = 0
        self.t = 0
        self.ppppp = txt
        self.sz = sz
        self.speed = speed
    def printing(self, line, mode):
        if self.wait <= 0:
            self.leng = 0
            for i in self.txt:
                if i == '!wait' or i == '!!wait':
                    self.leng += 20
                else:
                    self.leng += len(i)
            if self.md == 1:
                self.t = self.leng
            self.w += 1
            if self.w > self.speed:
                if self.t < self.leng:
                    self.t += 1
                self.w = 0
            
            if self.t <= self.leng:
                self.prtext(self.txt, sz = self.sz, line=line, mode=mode)
            if self.t == self.leng:
                self.done = 1
        else:
            self.wait -= 1
        
    def prtext(self, txt, sz, line, mode):
        font1 = 'gulim.ttf'
        if self.mode == 1:
            font1 = 'pixel.ttf'
        coo = self.mode*255*0
        myFont = pygame.font.Font(font1, sz+self.mode*3) #TmoneyRoundWindExtraBold.ttf
        # text_title = myFont.render(txt, False, (255, 255, 255))
        # t_rect = text_title.get_rect()
        # t_rect.left = 620 - mode * 600
        # t_rect.top = 20 + (line * 25)
        # screen.blit(text_title, t_rect)
        self.p2 = 0
        self.p = 0
        self.l = 0
        self.io = 0
        self.p3 = 0
        self.waiti = 0
        self.mm = 0
        text_title = myFont.render(txt[-1][self.io:self.p], False, (255-coo, 255-coo, 255-coo))
        t_rect = text_title.get_rect()
        for text in txt:
            if self.p2 < self.t:
                if text == '!wait':
                    self.p3 = 0
                    self.waiti = 1
                    while self.p2 < self.t and self.p3 < 20:
                        self.p2 += 1
                        self.p3 += 1
                    # a = 0
                    # while a < 60:
                    #     if self.p2 < self.t:
                    #         self.p2 += 1
                    #     a += 1
                    # print(self.t)
                elif text == '!!wait':
                    self.p3 = 0
                    self.waiti = 1
                    while self.p2 < self.t and self.p3 < 20:
                        self.p2 += 1
                        self.p3 += 1
                    # a = 0
                    # while a < 60:
                    #     if self.p2 < self.t:
                    #         self.p2 += 1
                    #     a += 1
                    # print(self.t)
                    self.l -= 1
                else:
                    self.p = 0
                    self.io = 0
                    while self.p < len(text) and self.p2 < self.t:
                        self.waiti = 0
                        text_title = myFont.render(text[self.io:self.p], False, (255-coo, 255-coo, 255-coo))
                        t_rect = text_title.get_rect()
                        if t_rect.width > 340 + mode * 600 + self.mode*180:
                            t_rect.left = 620 - mode * 600 - self.mode*580
                            if txt[self.mm-1] == '!!wait':
                                text_title1 = myFont.render(txt[self.mm-2]+' ', False, (255-coo, 255-coo, 255-coo))
                                t_rect1 = text_title1.get_rect()
                                t_rect.left += t_rect1.width
                            t_rect.top = 20 + (line * 25) + self.l * 25 + self.mode*20
                            screen.blit(text_title, t_rect)
                            self.io = self.p
                            self.l += 1
                        self.p += 1
                        self.p2 += 1
                    text_title = myFont.render(text[self.io:self.p], False, (255-coo, 255-coo, 255-coo))
                    t_rect = text_title.get_rect()
                    t_rect.left = 620 - mode * 600 - self.mode*580
                    t_rect.top = 20 + (line * 25) + self.l * 25 + self.mode*20
                    if txt[self.mm-1] == '!!wait':
                        text_title1 = myFont.render(txt[self.mm-2], False, (255-coo, 255-coo, 255-coo))
                        t_rect1 = text_title1.get_rect()
                        t_rect.left += t_rect1.width
                    screen.blit(text_title, t_rect)
                    self.l += 1
            self.mm += 1
        # text_title = myFont.render(txt[-1][self.io:self.p], False, (255, 255, 255))
        # t_rect = text_title.get_rect()
        # t_rect.left = 620 - mode * 600
        # t_rect.top = 20 + (line * 25) + (self.l-1) * 25
        if self.t > 0 and self.t < self.leng and self.waiti == 0:
            cursor1 = pygame.Rect((t_rect.right - 20, t_rect.top), (20, t_rect.height))
            #print((t_rect.top - 20, t_rect.right))
            pygame.draw.rect(screen, (255-coo, 255-coo, 255-coo), cursor1)
    
    def reset(self, text):
        self.txt = []
        self.txt.append(text)
        self.w = 0
        self.t = 0
        self.done = 0
        self.ln = 0
        self.wait = 0
        self.md = 0

    def next(self, text):
        self.txt.append(text)


#primg2(이미지이름, x좌표, y좌표)