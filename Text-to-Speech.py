from tkinter import *
from gtts import gTTS
import pygame
import os
import random
import string

# Initialize pygame mixer
pygame.mixer.init()

################### Initialized window ####################

root = Tk()
root.geometry('350x300')
root.resizable(0, 0)
root.config(bg='ghost white')
root.title('Text-to-Speech Application')

##heading
Label(root, text='TEXT_TO_SPEECH', font='arial 20 bold', bg='white smoke').pack()
Label(root, text='Text-to-Speech App', font='arial 15 bold', bg='white smoke').pack(side=BOTTOM)

# label
Label(root, text='Enter Text', font='arial 15 bold', bg='white smoke').place(x=20, y=60)

##text variable
Msg = StringVar()

# Entry
entry_field = Entry(root, textvariable=Msg, width='50')
entry_field.place(x=20, y=100)

################### define function ##############################

def generate_filename():
    """Generate a random filename for the mp3 file."""
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6)) + ".mp3"

def Text_to_speech():
    Message = entry_field.get()
    filename = generate_filename()
    speech = gTTS(text=Message)
    speech.save(filename)
    
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    # Remove the file after it finishes playing
    while pygame.mixer.music.get_busy():
        continue
    os.remove(filename)

def Exit():
    root.destroy()

def Reset():
    Msg.set("")

# Button
Button(root, text="PLAY", font='arial 15 bold', command=Text_to_speech, width=4).place(x=25, y=140)
Button(root, text='EXIT', font='arial 15 bold', command=Exit, bg='OrangeRed1').place(x=100, y=140)
Button(root, text='RESET', font='arial 15 bold', command=Reset).place(x=175, y=140)

# Infinite loop to run program
root.mainloop()
