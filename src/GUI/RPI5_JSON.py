import json
import RPi.GPIO as GPIO

# GPIO setup
GPIO.setmode(GPIO.BCM)

# Define GPIO pins and their initial states
pins = {
    "1A": {"pin": 17, "state": False}, 
    "1B": {"pin": 18, "state": False},
    "2C": {"pin": 27, "state": False},
    "2D": {"pin": 22, "state": False},
    "1E": {"pin": 23, "state": False},
    "1F": {"pin": 24, "state": False},
    "2G": {"pin": 25, "state": False},
    "2H": {"pin": 4, "state": False}
}

# Setup GPIO pins as outputs
for thruster, config in pins.items():
    GPIO.setup(config["pin"], GPIO.OUT)
    GPIO.output(config["pin"], GPIO.LOW)  # Ensure pins are off by default

# Load the JSON payload (received from the GUI)
with open("thruster_states.json", "r") as file:
    thruster_states = json.load(file)

# Process thruster states to control GPIO pins
for thruster, state in thruster_states.items():
    config = pins.get(thruster)
    if config:
        # Update the GPIO state only if the thruster's "state" is True
        if config["state"]:  # Only allow state change if True
            GPIO.output(config["pin"], GPIO.HIGH if state == "ON" else GPIO.LOW)
        else:
            GPIO.output(config["pin"], GPIO.LOW)  # Force the pin to LOW if not active

print("GPIO states updated successfully.")
