from art import *
from termcolor import colored, cprint
import serialConnect

def options():
    print("Please select from the following:\n")
    print("1. Control Servos\n")
    print("2. Status\n")
    print("3. Test Arduino Connection\n")
    cprint("4. QUIT\n", "red", attrs=["bold"])

    selection = input(colored('Selection: ','magenta', attrs=["blink"]))

    return selection

    optionSelector()

    

def optionSelector(option):
    
    match option:
        case "1":
            print("Not Implemented Yet, Choose a different option")
        case "2":
            print("Hello")
        case "3": 
            cprint("Testing Serial Connection", "green", "on_white")
            serialConnect.serialConnection()
        case "4":
           print("Quitting Arduino Servo Controller...")
           return False
        case _:
            print("Try again")
    return True


def logo():
    print(text2art( #ascii art
    '''Arduino Servo Controller'''
    , font="small"
    )
    )

serialConnect.checkPort()
serialConnect.serialConnection() #first establishing connection

#option selection
while True:
    logo()
    op = options()
    if not optionSelector(op):
        break  


'''
TODO: 

1. when I disconnect the arduino, the code kills itself, I think that I need
to put an exception in serialConnect to where if the port is not available to connect, we have to start over the port searching process  

2. option 1. Testing servos, research how to connect using the Arduino IDE

3. option 2. 
    Ex) Arduino Status: online/offline
        Number of Servos Connected: "1-4"


'''



    




