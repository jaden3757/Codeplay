import pygame

def playsound(a):
    sound = a
    pygame.mixer.music.load('sounds\\'+sound)
    pygame.mixer.music.play(-1)