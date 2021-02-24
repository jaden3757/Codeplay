# -*- coding: utf-8 -*-

import pygame
import sys
from module1 import *
from but import *
from main1 import *
# 방 import 하는 곳 (지도상에서 붙어있는 방 알아서 전부 import 해주길 바람)

import sp3
import b_hall
import start_room
import production_facility
import b_long
import sound
import time

sound.play_cynthia_S()

class Fade(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.rect = pygame.display.get_surface().get_rect()
        self.image = pygame.Surface(self.rect.size, flags=pygame.SRCALPHA)
        self.alpha = 0
        self.direction = 1

    def update(self, events):
        self.image.fill((0, 0, 0, self.alpha))
        self.alpha += self.direction

        if self.alpha > 255 or self.alpha < 0:
            self.direction *= -1
            self.alpha += self.direction

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
            t1.reset("테스트")
            t1.next("바이러스를 막아라")
        if scr == 1: # 1번째 대사
            t1.reset("정부의 계획을 찾아라")
        if scr == 2: # 2번째 대사 [이 아래에 더 추가 가능]
            t1.reset("스파이의 계획을 찾아라")

        ch = 0

def main():
    global scr
    global ch
    global run
    setscr(0)
    pygame.init()
    screen = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption("Moon Side")
    sprites = pygame.sprite.Group(Fade())
    clock = pygame.time.Clock()
    while True:
        # textls()
        # textprinting()

        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                return

        sprites.update(events)
        primg2("images/hole.jpg", 0, 0)
        sprites.draw(screen)
        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    main()