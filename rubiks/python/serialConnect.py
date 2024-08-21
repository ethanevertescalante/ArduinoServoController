import serial
import time
from termcolor import colored, cprint
import serial.tools.list_ports

def autoFindPort():
    """Lists available COM ports on Windows and macOS."""
    cprint("Seaching For Arduino Port...", "white", "on_blue")
    ports = serial.tools.list_ports.comports()
    arduino_port = []
    
    for port, desc, hwid in sorted(ports):
        if desc == "ROBOTIS ComPort":
            arduino_port.append(port)
            cprint(f"FOUND ARDUINO PORT ON {port}", 'white', "on_light_green")
            return port
       
    cprint("No Arduino port found, trying again in 5 seconds...", "white", "on_red")
    time.sleep(5)
    return autoFindPort() 
    
    
    

#Any command that will be sent to the aurduino will have to go through this step in order to make sure that the 
#connection is stable 

port = autoFindPort()
baud_rate = 115200  # Match this with the baud rate in your Arduino sketch


def quickStatus():
    return checkPort(False, "quick")

def send_message(message):
    ser = serial.Serial(port, baud_rate, timeout=1)
    time.sleep(0.2)
    ser.write((message + "\n").encode())  # Send the message
    response = ser.readline().decode('utf-8').strip()  # Read the response
    

def pingArduino():
    try:
        response = send_message("ping")
        cprint("Ping Successful", "green", attrs=["underline"])
        time.sleep(0.5)  # Wait 0.5 seconds before sending the next ping
        return response
    except serial.SerialException:
        cprint(f"Connection lost. Attempting to re-establish connection to {port}", "red",attrs=["underline"])
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
                cprint(f"Connection Established To {port}", "white", "on_blue")
            ErrorOccured = False   
            return ser   
        except serial.SerialException:
            if printData:
                cprint(f"Could not open port {port}. Retrying in 2 seconds...", "white", "on_red")
            if con == "quick":
                return "Offline"
            time.sleep(2)

def serialConnection():
    numResponses = 5
    counter = 0

    while counter < numResponses:
        try:
           response = send_message("ping")
           print(f"Received response: {response}")  # Debugging line

           if response == "pong":  # Check for "pong" instead of "Pong"
                counter += 1
           else:
                counter = 0  # Reset counter if the response is not "pong"
                pingArduino()
        except serial.SerialException:
            cprint(f"Connection lost. Attempting to re-establish connection to {port}", "red", attrs=["underline"]) 
            counter = 0  # Reset counter if connection is lost
            checkPort(True, "regular")

    cprint("Stable Connection To Arduino", "white", "on_green")
    

