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
import loading2

WHITE = (255, 255, 255)
HEAVY_WHITE = (200, 200 ,200)

# 시작
pygame.init() 
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Moon Side")
clock = pygame.time.Clock()

# def maprun():
game_over_button = button("다시 시작 >>", 140, 30, 850, 20) # 하위 버튼 디자인
game_over_button.color = (70,70,70)
game_over_button.textcolor = (0,0,0)
game_over_button.textsize = 22
game_over_button.font = 'pixel.ttf'

sound.play_cynthia_S()

run = True

myFont = pygame.font.SysFont( "moon2.ttf", 250, True, False)
text_Title= myFont.render("Wasted...", True, HEAVY_WHITE)

while run:
    # 세팅 [ 건드리지 말아야 할 것]
    screen.fill(pygame.color.Color(50, 50, 50))
    # main [여기에 코드 입력] > 이미지 오브젝트, 텍스트(prtext) 등등
    # | 버튼 그리는 곳 |
    # game_over_button.off()

    game_over_button.draw()
    screen.blit(text_Title, (70, 210))

    # | 이벤트 관리소 |
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        run = False
    # // Mouse_click
    if event.type == pygame.MOUSEBUTTONDOWN:
        buttoncheck() # [삭제하면 안되는 것]
    
        if game_over_button.check() == 1:
            loading2.maprun()

    if pygame.key.get_pressed()[pygame.K_m]:
        Sound_controll.sound_controll()
    
    #fin [끝]
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

# if __name__ == '__main__':
#     maprun()