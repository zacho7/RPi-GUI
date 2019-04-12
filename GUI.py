from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

rled = LED(18)
gled = LED(15)
bled = LED(14)

win = Tk()
win.title("LED Toggle")
myFont = tkinter.font.Font(family = "Helvetica", size = 12, weight = "bold")

def rledToggle():
    if rled.is_lit:
        rled.off()
        rledButton["text"] = "Turn red LED on"
    else:
        rled.on()
        rledButton["text"] = "Turn red LED off"

def gledToggle():
    if gled.is_lit:
        gled.off()
        gledButton["text"] = "Turn greem LED on"
    else:
        gled.on()
        gledButton["text"] = "Turn green LED off"
        
def bledToggle():
    if bled.is_lit:
        bled.off()
        bledButton["text"] = "Turn blue LED on"
    else:
        bled.on()
        bledButton["text"] = "Turn LED off"
        
def close():
    GPIO.cleanup()
    win.destroy()

rledButton = Button(win, text = "Turn red LED on", font = myFont, command = rledToggle, bg = "red", height = 1, width = 24)
rledButton.grid(row = 0, column = 1)

gledButton = Button(win, text = "Turn green LED on", font = myFont, command = gledToggle, bg = "green", height = 1, width = 24)
gledButton.grid(row = 1, column = 1)

bledButton = Button(win, text = "Turn blue LED on", font = myFont, command = bledToggle, bg = "blue", height = 1, width = 24)
bledButton.grid(row = 2, column = 1)

win.protocol("WM_DELETE_WINDOW", close)

win.mainloop()