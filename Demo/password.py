from tkinter import *
import pygame
import b_long

def enter_password():
    root = Tk()
    root.title("GUI")
    root.geometry("170x80+500+300") #가로 크기, 세로 크기, x좌표, y좌표
    root.resizable(False, False) #x(너비), y(높이) 값 변경 불가
    root.wm_attributes("-topmost", 1)
    label1 = Label(root, text="Enter password", bg="gray")
    root.overrideredirect(True)
            
    label1.pack()
    e = Entry(root, width=20)
    e.pack()
    e.insert(0, "")

    def btncmd():
        password = 198206

        value = e.get()
        value = int(value)

        if password == value:
            print("Correct!!")
            root.destroy()
        else:
            print("Worng!!")

        print(e.get())
        e.delete(0, END)
    def esc():
        root.destroy()
        b_long.maprun()
        
    btn = Button(root, fg = "black", bg = "gray" ,text="Enter", command=btncmd)
    btn.place(x = 119, y = 50)

    btn = Button(root, fg = "black", bg = "gray" ,text="ESC", command=esc)
    btn.place(x = 80, y = 50)

    root.configure(bg='gray')
    root.mainloop()