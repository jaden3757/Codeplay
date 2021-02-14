# -*- coding: utf-8 -*-

import pygame
import sys
from module1 import *
from but import *
from main1 import *

font1 = 'gulim.ttf'

pygame.init() 
screen = pygame.display.set_mode((1000, 600)) 

pygame.display.set_caption("Moon Side")

clock = pygame.time.Clock()
run = True
loading1 = True

load_button = button("Play", 100, 50, 450, 275) # PLAY 써진 버튼 하나 생성

ri = 0

while run:
    scrclear = 1
    if scrclear == 1:
        screen.fill(pygame.color.Color(50, 50, 50))
        scrclear = 0
    
    # main
    ri += 1
    if ri > 100:
        ri = 0
    w = 0
    while w <= 10:
        ri1 = ri + (w * 10)
        if ri1 > 100:
            ri1 -= 100
        pygame.draw.rect(screen, (100,100,100), [500 - (ri1 * 5), 300 - (ri1 * 3), ri1 * 10, ri1 * 6], 3)
        w += 1
    prtextm("Moon Side", 80, 500, 70)
    load_button.draw()
    # //All event
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        run = False

    if event.type == pygame.MOUSEBUTTONDOWN:
        if load_button.check() == 1: #처음에 생성했던 로드 버튼이 눌렸는지 확인
            changemap(1) # main1.py 에 chagemap 함수를 참고하시오

    pygame.display.flip()
    clock.tick(60)

pygame.quit()