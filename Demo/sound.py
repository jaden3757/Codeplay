import pygame
import time

pygame.init() 

pygame.mixer.init()
screen_width = 1000
screen_height = 750
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((screen_width, screen_height))

def play_plants_S():
    #screen setting
    sound = ("Planets.mp3")
    pygame.mixer.music.load(sound)
    pygame.mixer.music.play(-1)

def play_cynthia_S():
    #screen setting
    sound = ("sounds/Cynthia.mp3")
    pygame.mixer.music.load(sound)
    pygame.mixer.music.play(-1)

def play_Moodside_S():
    #screen setting
    sound = ("Moon_side_1_completed.mp3")
    pygame.mixer.music.load(sound)
    pygame.mixer.music.play(-1)

def play_check():
    sound = pygame.mixer.Sound("sounds/Check.wav")
    sound.play()

def play_typing():
    sound = pygame.mixer.Sound("sounds/Typing.wav")
    sound.play()

def play_error():
    sound = pygame.mixer.Sound("sounds/Error.wav")
    sound.play()

def play_warning():
    sound = pygame.mixer.Sound("sounds/Warning.wav")
    sound.play()