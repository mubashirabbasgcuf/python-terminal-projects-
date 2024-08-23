import time
import sys
import win32com.client
import threading

speaker = win32com.client.Dispatch("SAPI.SpVoice")

def Typing_effect(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)

Typing_effect("Welcome to Drink water reminder!!!\n")
Typing_effect("Drink water ------> Stay Healthy\n")
Typing_effect("Program is running\n")
print ("THe program will remind you to drink water after (5 sec) \n Time can be set by user choice:")

glass_no = 1
reminder_no = 1

def speak_text(text):
    speaker.Speak(text)

def reminder():
    global glass_no
    global reminder_no
    text = "its time to drink water\nIts Your glass number:{}\nAlert reminder no:{}\n_________________________________".format(glass_no, reminder_no)
    Typing_effect(text)
    t = threading.Thread(target=speak_text, args=("its time to drink water. Its Your glass number {}. Alert reminder no {}.".format(glass_no, reminder_no),))
    t.start()
    glass_no += 1
    reminder_no += 1

i = 0

while i != 10:
    time.sleep(5)
    reminder()
    i = i + 1