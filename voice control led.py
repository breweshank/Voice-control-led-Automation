import serial
import time
import speech_recognition as sr
import pyaudio
# Configure the serial connection to the Arduino
arduino = serial.Serial('COM12', 9600, timeout=0)  # Replace 'COM3' with your Arduino's COM port
time.sleep(1)  # Wait for the serial connection to initialize

# Initialize the recognizer
recognizer = sr.Recognizer()

def listen_for_command():
    with sr.Microphone() as source:
        print("Sun raha hu....")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"Recognized command: {command}")

        if "turn on led 1" in command:
            arduino.write(b'turn on led1\n')
            print("Command sent: turn on led1")
        elif "turn off led 1" in command:
            arduino.write(b'turn off led1\n')
            print("Command sent: turn off led1")
        elif "turn on led 2" in command:
            arduino.write(b'turn on led2\n')
            print("Command sent: turn on led2")
        elif "turn off led 2" in command:
            arduino.write(b'turn off led2\n')
            print("Command sent: turn off led2")
        elif "turn on led 3" in command:
            arduino.write(b'turn on led3\n')
            print("Command sent: turn on led3")
        elif "turn off led 3" in command:
            arduino.write(b'turn off led3\n')
            print("Command sent: turn off led3")
        elif "turn off all led" in command:
            arduino.write(b'turn off led3\n')
            arduino.write(b'turn off led2\n')
            arduino.write(b'turn off led1\n')
            print("Command sent: turn off ")
        elif "turn on all led" in command:
            arduino.write(b'turn on led3\n')
            arduino.write(b'turn on led2\n')
            arduino.write(b'turn on led1\n')
            print("Command sent; turn on all led")
        else:
            print("thik se bol")
    except sr.UnknownValueError:
        print("Could not understand the command")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")

while True:
    listen_for_command()
