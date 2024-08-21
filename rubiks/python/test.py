import serial.tools.list_ports

def list_com_ports():
    """Lists available COM ports on Windows and macOS."""
    ports = serial.tools.list_ports.comports()
    available_ports = []
    
    for port, desc, hwid in sorted(ports):
        available_ports.append(port)
        print(f"Port: {port}, Description: {desc}, HWID: {hwid}")
        
    if desc == "ROBOTIS ComPort":
        print(f"found correct com: {port} ")
    
    if not available_ports:
        print("No COM ports found.")
    
    return available_ports

# Example usage
if __name__ == "__main__":
    print("Scanning for available COM ports...")
    ports = list_com_ports()
    if ports:
        print("Available COM ports:")
        for port in ports:
            print(port)
    else:
        print("No COM ports detected.")
