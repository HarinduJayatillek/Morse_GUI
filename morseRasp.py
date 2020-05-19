from tkinter import *
import time
import RPi.GPIO as GPIO
import tkinter.font
from gpiozero import LED

led = LED(21)

def morseBlink(val):

        val = str(val)
        print(val)
        val = val.split()


        for char in val:
            for c in char:
                if c == '.':
                    led.on()
                    time.sleep(0.3)
                    led.off()
                    time.sleep(0.3)
                else:
                    led.on()
                    time.sleep(1)
                    led.off()
                    time.sleep(0.3)

def morseConvert():

    mWord = word.get()


    CODE = {'A': '.-',    'B': '-...',   'C': '-.-.',
            'D': '-..',    'E': '.',      'F': '..-.',
            'G': '--.',    'H': '....',   'I': '..',
            'J': '.---',   'K': '-.-',    'L': '.-..',
            'M': '--',     'N': '-.',     'O': '---',
            'P': '.--.',   'Q': '--.-',   'R': '.-.',
            'S': '...',    'T': '-',      'U': '..-',
            'V': '...-',   'W': '.--',    'X': '-..-',
            'Y': '-.--',   'Z': '--..'}

    testWord = str(mWord)
    word.delete(0,tkinter.END)
    testWord = testWord.split()

    morseVal = " "

    for char in testWord:
        for c in char:
            """print(CODE['A'])"""
            testC = CODE[c.upper()]
            print(testC)
            morseVal = morseVal + str(testC)

    print("Test : ",testWord)
    morseBlink(morseVal)

win = Tk()
win.title("MorseConverter")
myFont = tkinter.font.Font(family = "Helvetica", size = 12 , weight = "bold")

tkinter.Label(win, text = "Test your Word").grid(row=0)

word = tkinter.Entry()
word.grid(row=0 , column =1)

enterButton = Button(win , text = "Convert" , font = myFont , command = morseConvert, height = 1 , width= 8 , bg = "light blue")
enterButton.grid(row=1, column = 1)

exitButton = tkinter.Button(win , text="Exit" , command = win.quit , bg = "red")
exitButton.grid(row=1 , column=0)


win.mainloop()
