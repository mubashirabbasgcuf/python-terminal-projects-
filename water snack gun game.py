import time
import sys
import random
while True:
    print("W E L C O M E TO 'WATER'-----'SNAKE'-----'GUN GAME'" )
    print("Select from Following:")
    print("Snake ---- water------- Gun")

    choices=["water","gun","snake"]
    def get_user_choice():
        user_choice=input("please enter your choice:").lower()
        while user_choice not in choices:
            print("invalid input please try again ")   
        return user_choice 
            
    def get_cpu_choice():
        cpu_choice=random.choice(choices)
        return cpu_choice

    def determine_winner(user_choice,cpu_choice):
        if cpu_choice==user_choice:
            print("match Tie")
        elif user_choice=="water " and cpu_choice=="gun":
             print("you win")
        elif user_choice=="gun" and cpu_choice=="water":
            print("you win")
        elif user_choice=="snake" and cpu_choice=="water":
             print("you win")
        else:
         print("cpu win")

    user_choice=get_user_choice()
    cpu_choice=get_cpu_choice()
    print(f"you have choice== {user_choice}")
    print(f"cpu have choice== {cpu_choice}")
    determine_winner(user_choice,cpu_choice)