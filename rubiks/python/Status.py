
from serialConnect import quickStatus
from termcolor import colored
import time 
def arduinoCheck():
    
    #print(f"Arduino Status: {initial}", end='\r')  # Print "Checking..." and stay on the same line
    
      # Simulate the checking process

    if quickStatus() == "Offline":
        newStatus = colored("Offline", "red", attrs=["underline"])
    elif quickStatus() == "Online":
        newStatus = colored("Online", "green", attrs=["underline"])

    return newStatus

    #print(f"\r{' ' * (len('Arduino Status: ') + len(initial))}", end='')  # Clear the entire line
    #print(f"\rArduino Status: {newStatus}")

def numServosConnected():
    servos = 0
    


def fullStatus():
    final_status = arduinoCheck()  # Call arduinoCheck to get the current status
    
    # Prepare the lines for the status menu
    lines = [
        colored("Arduino Status Menu", "white", "on_yellow"),
        "-------------------",
        f"Status: {final_status}",

    ]
    
    for line in lines:
        print(line)
4

