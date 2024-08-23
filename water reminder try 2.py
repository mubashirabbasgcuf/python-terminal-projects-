import time
import sys
import win32com.client

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

def reminder():
    global glass_no
    global reminder_no
    speaker.Speak("its time to drink water")
    Typing_effect("its time to drink water \n")
    speaker.Speak("Its Your glass number:{}".format(glass_no))
    print("Its Your glass no:{}".format(glass_no))
    print("Alert reminder no:{}".format(reminder_no))
    print("_________________________________")
    glass_no += 1
    reminder_no += 1
i = 0

while i != 10:
    time.sleep(5)
    reminder()
    i = i + 1
