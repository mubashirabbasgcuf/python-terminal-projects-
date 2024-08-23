import win32com.client
import time
import sys
import hashlib
import getpass
speaker=win32com.client.Dispatch("SAPI.SpVoice")
def Typing_effect(text):
     for char in text:
          sys.stdout.write(char)
          sys.stdout.flush()
          time.sleep(0.05)
def encode(text,password):
    sha_signature=hashlib.sha256((text+password).encode()).hexdigest()
    return sha_signature
def encrption(a):
 encoded = encode(a,"password")
 print("Encrupted text:",encoded)

   
   

while 1:
    Typing_effect("An offline encrption Software by Mubashir Abbas\n")
    print("select your desire option 1:Encruption")
    user_choice=int(input("please Select from above option:"))
    if(user_choice==1):     
        a=input("Enter Your text:")
        wait=("Your Text is being encrpted")
        speaker.speak(wait)
        encrption(a)

    else:
        print("Invalid option")


     
