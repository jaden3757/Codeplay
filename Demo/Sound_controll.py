import pygame
import sys
from module1 import *
from but import *
from main1 import * #main
from tkinter import *
import time
# from sp3 import *

def sound_controll():
    root = Tk()
    root.title("MUSIC CONTROLL")
    root.geometry("120x220+500+300") #가로 크기, 세로 크기, x좌표, y좌표
    root.wm_attributes("-topmost", 1)
    root.resizable(False, False) #x(너비), y(높이) 값 변경 불가
    # root.overrideredirect(True)

    def v_up():
        v = pygame.mixer.music.get_volume()
        pygame.mixer.music.set_volume(v + 0.1)
        print("volume up")
        time.sleep(0.2)

    def v_down():
        v = pygame.mixer.music.get_volume()
        pygame.mixer.music.set_volume(v - 0.1)
        print("volume down")
        time.sleep(0.2)

    btn_up = Button(root, width = 11, height = 2, fg = "black", bg = "gray", text = "Volume Up", command = v_up)
    btn_up.place(x = 19, y = 20)

    btn_down = Button(root, width = 11, height = 2, fg = "black", bg = "gray", text = "Volume Down", command = v_down)
    btn_down.place(x = 19, y = 70)

    mute = IntVar() #여기에 int형으로 값을 저장
    mute_button = Radiobutton(root, fg = "black", bg = "gray", text="pause", value=1, variable=mute) # value 가 숫자면 variable의 상태가 Int으로 적어야함
    mute_button.place(x = 20, y = 130)
    mute_button = Radiobutton(root, fg = "black", bg = "gray", text="unpause", value=2, variable=mute) # value 가 숫자면 variable의 상태가 Int으로 적어야함
    mute_button.place(x = 20, y = 170)

    mute_value = mute.get()
    print(mute_value)
                
    if mute_value == 1:
        pygame.mixer.music.pause()
        time.sleep(0.2)
    elif mute_value == 2:
        pygame.mixer.music.unpause()
        time.sleep(0.2)

    root.configure(bg='gray')
    root.mainloop()