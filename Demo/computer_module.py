import pygame
import sys
from module1 import *
from but import *
import reference_room
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

class computer_icon:
    color = (150,150,0)
    textcolor = (255,255,255)
    textsize = 15
    cool = 0
    count = 0
    onoff = 1
    font = 'gulim.ttf'
    item = ['main', 50]
    item_list = []
    finding_time = 0
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
                if itemui.isinv != 'inv' and type(itemui.isinv) != int:
                    if itemui.isinv.txt == self.txt and itemui.onoff == 1:
                        pygame.draw.rect(t_surface, (0,150,0,100), (pygame.mouse.get_pos()[0]-40, pygame.mouse.get_pos()[1]-30, 80, 20))
                    else:
                        pygame.draw.rect(t_surface, (0,0,0,100), (pygame.mouse.get_pos()[0]-40, pygame.mouse.get_pos()[1]-30, 80, 20))
                else:
                    pygame.draw.rect(t_surface, (0,0,0,100), (pygame.mouse.get_pos()[0]-40, pygame.mouse.get_pos()[1]-30, 80, 20))
                screen.blit(t_surface, (0,0))
                self.prtext(self.txt, self.textsize, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1] - 20)
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

loading_logo_40 = computer_object('images\\black_widow_40.png', 500, 500, 50, -50)
loading_logo_60 = computer_object('images\\black_widow_60.png', 500, 500, 50, -50)
loading_logo_100 = computer_object('images\\black_widow_100.png', 500, 500, 50, -50)

computer_desktop = computer_object('images\\computer_desktop.png', 1200, 1000, -250, -200)
computer_txt = computer_object('images\\computer_txt.png', 1200, 1000, -250, -200)
desktop_bar = computer_object('images\\desktop_bar.jpg', 333, 30, 137, 350)
txt_icon = computer_icon('images\\txt_icon.png', "andigh.txt", 35, 35, 145, 300)
txt_icon_clicked = computer_icon('images\\txt_icon_clicked.png', "andigh.txt", 35, 35, 145, 300)

def computer_loading(computer_loading_count):
    loading_logo_40.draw()
    if computer_loading_count > 60:
        a_loading_dot[0].draw()
        loading_logo_40.draw()
    if computer_loading_count > 120:
        a_loading_dot[1].draw()
        loading_logo_60.draw()
    if computer_loading_count > 180:
        a_loading_dot[2].draw()
        loading_logo_100.draw()
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
        b_loading_dot3.draw() 

def computer_run(clicked_count):
    if clicked_count != 3:
        computer_desktop.draw()
    elif clicked_count == 3:
        computer_txt.draw()   
    desktop_bar.draw()
    if pygame.mouse.get_pos()[0] > 142 and pygame.mouse.get_pos()[1] > 352:
            if pygame.mouse.get_pos()[0] < 216 and pygame.mouse.get_pos()[1] < 375:
                if pygame.mouse.get_pressed()[0] == 1:
                    reference_room.maprun()
def icondraw(clicked_count):
    if clicked_count == 1:
        txt_icon.draw()
    elif clicked_count == 2:
        txt_icon_clicked.draw()
