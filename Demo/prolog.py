# -*- coding: utf-8 -*-

import pygame
import sys
from module1 import *
from but import *
from main1 import *
# 방 import 하는 곳 (지도상에서 붙어있는 방 알아서 전부 import 해주길 바람)

import start_room
import production_facility

import sp3
import b_hall
import start_room
import production_facility
import sp3
import b_long
import sound

font1 = 'gulim.ttf'

pygame.init() 
screen = pygame.display.set_mode((1000, 600)) 

pygame.display.set_caption("Moon Side")

clock = pygame.time.Clock()
run = True
loading1 = True
sound.play_Moodside_S()

def maprun():
    global run

    ri = -2
    p = 0
    fade = 0

    tsurface = screen.convert_alpha()
    tsurface.fill((0,0,0,0))
    
    screen.fill(pygame.color.Color(50, 50, 50))

    i = 0
    while i < 60:
        i += 1
        screen.blit(tsurface, (0,0))
        pygame.display.flip()
        clock.tick(60)
    
    while run:
        scrclear = 1
        if scrclear == 1:
            screen.fill(pygame.color.Color(50, 50, 50))
            scrclear = 0

        if fade > 0:
            pygame.draw.rect(tsurface, (0,0,0,fade*2), [0,0,1000,600])
            fade += 6
            if fade > 125:
                b_hall.maprun()

if __name__ == '__main__':
    maprun()