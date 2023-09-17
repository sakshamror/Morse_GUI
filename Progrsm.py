from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
window=Tk()
GPIO.setup(11,GPIO.OUT)
Font=tkinter.font.Font(family='Helvetica',size=13,weight="bold")
Morse= { 'A':'.-', 'B':'-...',
   'C':'-.-.', 'D':'-..', 'E':'.',
   'F':'..-.', 'G':'--.', 'H':'....',
   'I':'..', 'J':'.---', 'K':'-.-',
   'L':'.-..', 'M':'--', 'N':'-.',
   'O':'---', 'P':'.--.', 'Q':'--.-',
   'R':'.-.', 'S':'...', 'T':'-',
   'U':'..-', 'V':'...-', 'W':'.--',
   'X':'-..-', 'Y':'-.--', 'Z':'--..',
   '1':'.----', '2':'..---', '3':'...--',
   '4':'....-', '5':'.....', '6':'-....',
   '7':'--...', '8':'---..', '9':'----.',
   '0':'-----', ', ':'--..--', '.':'.-.-.-',
   '?':'..--..', '/':'-..-.', '-':'-....-',
   '(':'-.--.', ')':'-.--.-'
}
def dot():
    GPIO.output(11,GPIO.HIGH)
    time.sleep(0.6)
    GPIO.output(11,GPIO.LOW)
    time.sleep(0.6)
def dash():
    GPIO.output(11,GPIO.HIGH)
    time.sleep(1.8)
    GPIO.output(11,GPIO.LOW)
    time.sleep(1.8)
def convert():
    input=user_input.get()
    for letter in input:
        for symbol in Morse[letter.upper()]:
            if symbol=='.':
                dot()
            elif symbol=='-':
                dash()
            else:
                time.sleep(0.5)
            
user_input=Entry(window,font=Font,width=24,bg='white')
user_input.grid(row=0,column=0)

button=Button(window,text='convert',font=Font,command=convert,bg='grey',height=1,width=10)
button.grid(row=1,column=0)