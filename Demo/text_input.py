import pygame
import time

SIZE = width,height = 640,240
 
screen = pygame.display.set_mode(SIZE)
screen.fill((0,0,150))
pygame.init()
 
BLACK = (0,0,0)
C1_BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)
WHITE = (255,255,255)
# Text Editing
 
text1 = 'Text Editing, 텍스트 편집하기'
font1 = pygame.font.Font('pixel.ttf',35)
img1 = font1.render(text1,True,BLACK)
 
rect1 = img1.get_rect()
rect1.topleft = (40,50)
cursor1 = pygame.Rect(rect1.topright,(3,rect1.height))
print(cursor1)
 
running = True
 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                if len(text1)> 0:
                    text1 = text1[:-1]
                    print("x")
            else:
                text1 += event.unicode
                print("o")
            img1 = font1.render(text1,True,BLACK)
            rect1.size = img1.get_size()
            cursor1.topleft = rect1.topright
 
    screen.fill(C1_BLUE)
    screen.blit(img1,rect1)
    if time.time() % 1 > 0.5:
        pygame.draw.rect(screen, RED, cursor1)
    pygame.display.update()
 
pygame.quit()