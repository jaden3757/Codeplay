import pygame
import time

pygame.init() 

screen_width = 1000
screen_height = 750
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


def sound_play():
    #screen setting
    screen = pygame.display.set_mode((screen_width, screen_height))
    sound = ("Planets.mp3")
    pygame.mixer.music.load(sound)
    pygame.mixer.music.play(-1)
