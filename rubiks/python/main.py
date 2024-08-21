from art import *
from termcolor import colored, cprint
import serialConnect
import Status

def options():
    print("Please select from the following:\n")
    print("1. Control Servos\n")
    print("2. Status\n")
    print("3. Test Arduino Connection\n")
    cprint("4. QUIT\n", "red", attrs=["bold"])

    selection = input(colored('Selection: ','magenta', attrs=["blink"]))

    return selection

    

def optionSelector(option):
    
    match option:
        case "1":
            print("Not Implemented Yet, Choose a different option")
        case "2":
            Status.fullStatus()
        case "3": 
            cprint("Testing Serial Connection", "green", "on_white")
            serialConnect.serialConnection()
        case "4":
           print("Quitting Arduino Servo Controller...")
           return False
        case _:
            print("No option with that number, try again")
    return True


def logo():
    print(text2art( #ascii art
    '''Arduino Servo Controller'''
    , font="small"
    )
    )

serialConnect.serialConnection() #first establishing connection

#option selection
while True:
    logo()
    op = options()
    if not optionSelector(op):
        break  


'''
TODO: 

2. option 1. Testing servos, research how to connect using the Arduino IDE

3. option 2. 
    Ex) Arduino Status: online/offline
        Number of Servos Connected: "1-4"


'''



    




