void setup() {
  Serial.begin(115200); // Start serial communication at 115200 baud
  while (!Serial);      // Wait for the serial port to connect. Needed for native USB port only
}

void loop() {
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n');
    command.trim(); // Remove any extra whitespace

    if (command == "ping") {
      Serial.println("pong");
    }
  }
}
