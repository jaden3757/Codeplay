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
import time

WHITE = (255, 255, 255)
HEAVY_WHITE = (200, 200 ,200)

# 시작
pygame.init() 
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Moon Side")
clock = pygame.time.Clock()

# def maprun():
game_over_button = button("게임 종료", 140, 30, 850, 20) # 하위 버튼 디자인
game_over_button.color = (70,70,70)
game_over_button.textcolor = (0,0,0)
game_over_button.textsize = 22
game_over_button.font = 'pixel.ttf'

pygame.mixer.music.stop()

run = True

myFont = pygame.font.SysFont( "moon2.ttf", 250, True, False)
text_Title= myFont.render("Wasted...", True, HEAVY_WHITE)

t_surface = screen.convert_alpha()
t_surface.fill((0,0,0,0))

fade = 100

while run:
    # 세팅 [ 건드리지 말아야 할 것]
    screen.fill(pygame.color.Color(0, 0, 0))
    # main [여기에 코드 입력] > 이미지 오브젝트, 텍스트(prtext) 등등
    prtextm2('Game Over', 140, 500, 300, (255,255,255, True), ft='moon.otf')
    if fade > 0:
        pygame.draw.rect(t_surface, (0,0,0,(fade/100)*255), [0,0,1000,1000])
        screen.blit(t_surface, (0,0))
    else:
        game_over_button.draw()
    fade -= 2
    if fade < 0:
        fade = 0
    # | 버튼 그리는 곳 |
    # game_over_button.off()

    # | 이벤트 관리소 |
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        run = False
    # // Mouse_click
    if event.type == pygame.MOUSEBUTTONDOWN:
        buttoncheck() # [삭제하면 안되는 것]
    
        if game_over_button.check() == 1:
            pygame.quit()

    if pygame.key.get_pressed()[pygame.K_m]:
        Sound_controll.sound_controll()
    
    #fin [끝]
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

# if __name__ == '__main__':
#     maprun()