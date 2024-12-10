import json
import RPi.GPIO as GPIO

# GPIO setup
GPIO.setmode(GPIO.BCM)

# These are the GPIO Peripherals Specifically not the actual Pins of the RPI5

pins = {"1A": 17, "1B": 18, "2C": 27, "2D": 22, "1E": 23, "1F": 24, "2G": 25, "2H": 4}
for pin in pins.values():
    GPIO.setup(pin, GPIO.OUT)

# Load the JSON payload (received from the GUI)
with open("thruster_states.json", "r") as file:
    thruster_states = json.load(file)

# Process thruster states to control GPIO pins
for thruster, state in thruster_states.items():
    pin = pins.get(thruster)
    if pin:
        GPIO.output(pin, GPIO.HIGH if state == "ON" else GPIO.LOW)

print("GPIO states updated successfully.")