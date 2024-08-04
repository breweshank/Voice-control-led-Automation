const int led1Pin = 13; // Pin for LED 1
const int led2Pin = 12; // Pin for LED 2
const int led3Pin = 11; // Pin for LED 3

void setup() {
  pinMode(led1Pin, OUTPUT); // Initialize LED 1 pin as an output
  pinMode(led2Pin, OUTPUT); // Initialize LED 2 pin as an output
  pinMode(led3Pin, OUTPUT); // Initialize LED 3 pin as an output
  Serial.begin(9600); // Start serial communication at 9600 baud rate
}

void loop() {
  if (Serial.available() > 0) { // Check if data is available to read
    String command = Serial.readStringUntil('\n'); // Read the command
    command.trim(); // Remove any leading/trailing whitespace

    if (command == "turn on led1") {
      digitalWrite(led1Pin, HIGH); // Turn LED 1 on
      Serial.println("LED 1 turned on");
    } else if (command == "turn off led1") {
      digitalWrite(led1Pin, LOW); // Turn LED 1 off
      Serial.println("LED 1 turned off");
    } else if (command == "turn on led2") {
      digitalWrite(led2Pin, HIGH); // Turn LED 2 on
      Serial.println("LED 2 turned on");
    } else if (command == "turn off led2") {
      digitalWrite(led2Pin, LOW); // Turn LED 2 off
      Serial.println("LED 2 turned off");
    } else if (command == "turn on led3") {
      digitalWrite(led3Pin, HIGH); // Turn LED 3 on
      Serial.println("LED 3 turned on");
    } else if (command == "turn off led3") {
      digitalWrite(led3Pin, LOW); // Turn LED 3 off
      Serial.println("LED 3 turned off");
    } else {
      Serial.println("Unknown command");
    }
  }
}
