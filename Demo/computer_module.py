import pygame
import sys
from module1 import *

pygame.init()
screen = pygame.display.set_mode((600, 800))
clock = pygame.time.Clock()

def mousechange_cp():
    pygame.mouse.set_visible(False)
    if pygame.mouse.get_pressed()[0] == 1:
        primg2('images\\cp_cursor_c.png', pygame.mouse.get_pos()[0]-10, pygame.mouse.get_pos()[1]-10)
    else:
        primg2('images\\cp_cursor.png', pygame.mouse.get_pos()[0]-10, pygame.mouse.get_pos()[1]-10)

class computer_object:
    def __init__(self, name, sx, sy, x, y):
        self.sx = sx
        self.sy = sy
        self.x = x
        self.y = y
        self.name = name
        self.img = pygame.image.load(self.name)
        self.img = pygame.transform.scale(self.img, (self.sx, self.sy))
    def draw(self):
        screen.blit(self.img, [self.x, self.y])



a_loading_dot1 = computer_object('images\\cp_loading_dot1.png', 13, 13, 227, 300)
a_loading_dot2 = computer_object('images\\cp_loading_dot1.png', 13, 13, 242, 300)
a_loading_dot3 = computer_object('images\\cp_loading_dot1.png', 13, 13, 257, 300)
a_loading_dot4 = computer_object('images\\cp_loading_dot1.png', 13, 13, 272, 300)
a_loading_dot5 = computer_object('images\\cp_loading_dot1.png', 13, 13, 287, 300)
a_loading_dot6 = computer_object('images\\cp_loading_dot1.png', 13, 13, 302, 300)
a_loading_dot7 = computer_object('images\\cp_loading_dot1.png', 13, 13, 317, 300)
a_loading_dot8 = computer_object('images\\cp_loading_dot1.png', 13, 13, 332, 300)
a_loading_dot9 = computer_object('images\\cp_loading_dot1.png', 13, 13, 347, 300)
a_loading_dot10 = computer_object('images\\cp_loading_dot1.png', 13, 13, 362, 300)
a_loading_dot = (a_loading_dot1, a_loading_dot2, a_loading_dot3, a_loading_dot4, a_loading_dot5, a_loading_dot6, a_loading_dot7, a_loading_dot8, a_loading_dot9, a_loading_dot10)

b_loading_dot1 = computer_object('images\\cp_loading_dot2.png', 5, 5, 327, 335)
b_loading_dot2 = computer_object('images\\cp_loading_dot2.png', 5, 5, 337, 335)
b_loading_dot3 = computer_object('images\\cp_loading_dot2.png', 5, 5, 347, 335)


def computer_loading(computer_loading_count):

    if computer_loading_count > 60:
        a_loading_dot[0].draw()
    if computer_loading_count > 120:
        a_loading_dot[1].draw()
    if computer_loading_count > 180:
        a_loading_dot[2].draw()
    if computer_loading_count > 240:
        a_loading_dot[3].draw()
    if computer_loading_count > 300:
        a_loading_dot[4].draw()
    if computer_loading_count > 360:
        a_loading_dot[5].draw()
    if computer_loading_count > 420:
        a_loading_dot[6].draw()
    if computer_loading_count > 480:
        a_loading_dot[7].draw()
    if computer_loading_count > 540:
        a_loading_dot[8].draw()
    if computer_loading_count > 600:
        a_loading_dot[9].draw()
    if computer_loading_count > 660:
        b_loading_dot1.draw()
        b_loading_dot2.draw()
        b_loading_dot3.draw() 
    elif computer_loading_count % 60 < 20:
        b_loading_dot1.draw()
    elif computer_loading_count % 60 < 40:
        b_loading_dot1.draw()
        b_loading_dot2.draw()
    elif computer_loading_count % 60 < 59:
        b_loading_dot1.draw()
        b_loading_dot2.draw()
        b_loading_dot3.draw() 

    