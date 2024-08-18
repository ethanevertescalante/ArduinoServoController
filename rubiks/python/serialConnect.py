import serial
import time


#Any command that will be sent to the aurduino will have to go through this step in order to make sure that the 
#connection is stable 

port = 'COM5'  # Replace with your actual port
baud_rate = 115200  # Match this with the baud rate in your Arduino sketch

def send_message(message):
    ser = serial.Serial(port, baud_rate, timeout=1)
    ser.write((message + '\n').encode())  # Send the message
    response = ser.readline().decode('utf-8').strip()  # Read the response
    return response

def pingArduino():
    response = send_message("ping")
    print("Received:", response)
    time.sleep(0.5)  # Wait 5 seconds before sending the next ping

def checkPort():
    ErrorOccured = True
    while ErrorOccured:
        try:
            ser = serial.Serial(port, baud_rate, timeout=1)
            time.sleep(2)  # Wait for the connection to establish
            print("Connection Established To Port")
            ErrorOccured = False 
            return ser   
        except serial.SerialException:
            print(f"Could not open port {port}. Retrying in 2 seconds...")
            time.sleep(2)

def serialConnection():
    numResponses = 5
    counter = 0

    response = send_message("ping")

    while counter < 5:
        if response != "Pong":
            pingArduino()
            counter += 1
        
    print("Stable Connection To Arduino")
    


