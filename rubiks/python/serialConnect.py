import serial
import time
from termcolor import colored, cprint


#Any command that will be sent to the aurduino will have to go through this step in order to make sure that the 
#connection is stable 

port = 'COM5'  # Replace with your actual port
baud_rate = 115200  # Match this with the baud rate in your Arduino sketch
def quickStatus():
    return checkPort(False, "quick")

def send_message(message):
    ser = serial.Serial(port, baud_rate, timeout=1)
    ser.write((message + '\n').encode())  # Send the message
    response = ser.readline().decode('utf-8').strip()  # Read the response
    return response

def pingArduino():
    try:
        response = send_message("ping")
        cprint("Ping Successful", "green", attrs=["underline"])
        time.sleep(0.5)  # Wait 0.5 seconds before sending the next ping
        return response
    except serial.SerialException:
        cprint("Connection lost. Attempting to re-establish connection to port", "red",attrs=["underline"])
        checkPort(True, "regular")
        return "No response"


def checkPort(printData, con):
    ErrorOccured = True
    while ErrorOccured:
        try:
            ser = serial.Serial(port, baud_rate, timeout=1)
            #time.sleep(2)  # Wait for the connection to establish
            if con == "quick":
                return "Online"
            if printData:
                cprint("Connection Established To Port", "white", "on_blue")
            ErrorOccured = False
             
            return ser   
        except serial.SerialException:
            if printData:
                cprint(f"Could not open port {port}. Retrying in 2 seconds...", "white", "on_red")
            if con == "quick":
                return "Offline"
            time.sleep(2)

def serialConnection():
    checkPort(True, "regular")
    numResponses = 5
    counter = 0

    response = send_message("ping")

    while counter < numResponses :
        if response != "Pong":
            try:
                pingArduino()
                counter += 1
            except serial.SerialException:
                counter = 0
                cprint("Connection lost. Attempting to re-establish connection to port", "red",attrs=["underline"])
                checkPort(True, "regular")
                return "No response"
     
    cprint("Stable Connection To Arduino", "white", "on_green")
    
    


