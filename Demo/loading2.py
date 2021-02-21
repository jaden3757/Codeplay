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
import sp3

font1 = 'gulim.ttf'

pygame.init() 
screen = pygame.display.set_mode((1000, 600)) 

pygame.display.set_caption("Moon Side")

clock = pygame.time.Clock()
run = True
loading1 = True

def maprun():
    global run
    pygame.mixer.init()
    pygame.mixer.music.load('sounds\\Planets.mp3')
    pygame.mixer.music.play(-1)

    load_button = button("Play", 100, 50, 450, 275) # PLAY 써진 버튼 하나 생성

    ri = -2
    p = 0
    fade = 0

    play_button = imagebutton('images\\idle.png', 300, 150, 530, 280)

    # pygame.mixer.music.load("Planets.mp3")
    # pygame.mixer.music.play(-1)
    # sound.playsound('Planets.mp3')

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
        
        # main
        # ri += 1
        # if ri > 100:
        #     ri = 0
        # w = 0
        # while w <= 10:
        #     ri1 = ri + (w * 10)
        #     if ri1 > 100:
        #         ri1 -= 100
        #     pygame.draw.rect(screen, (100,100,100), [500 - (ri1 * 5), 300 - (ri1 * 3), ri1 * 10, ri1 * 6], 3)
        #     w += 1
        primg2('teaser-5.png', 0,0)
        # prtextm("Moon Side", 80, 500, 70)

        p += 1
        if p > 0:
            if ri < 15:
                ri += 1
            p = 0
        
        if play_button.check() == 0:
            ri = -2
        
        if ri == -2:
            play_button.changeimg('images\\idle.png')
        if ri == -1:
            play_button.changeimg('images\\p3.png')
        if ri == 0:
            play_button.changeimg('images\\p4.png')
        if ri == 1:
            play_button.changeimg('images\\p5.png')
        if ri == 2:
            play_button.changeimg('images\\p4.png')
        if ri == 3:
            play_button.changeimg('images\\p3.png')
        if ri == 4:
            play_button.changeimg('images\\p2.png')
        if ri == 5:
            play_button.changeimg('images\\p1.png')
        if ri == 6:
            play_button.changeimg('images\\p2.png')
        if ri == 7:
            play_button.changeimg('images\\p1.png')
        if ri == 8:
            play_button.changeimg('images\\p2.png')
        if ri == 9:
            play_button.changeimg('images\\idle.png')

        if play_button.check() == 1:
            primg('images\\txtbg.png', 300, 150, 530, 280)
        play_button.draw()
        # load_button.draw()

        if fade > 0:
            pygame.draw.rect(tsurface, (0,0,0,fade*2), [0,0,1000,600])
            fade += 6
            if fade > 125:
                b_hall.maprun()
        # //All event
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if load_button.check() == 1: #처음에 생성했던 로드 버튼이 눌렸는지 확인
                # import rooms
                start_room.maprun()
            if play_button.check() == 1:
                pygame.mixer.music.stop()
                play_button.off()
                fade = 1
        screen.blit(tsurface, (0,0))
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    maprun()