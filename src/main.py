"""Vibe Mesh Test."""

# Import the Pin class from the machine module to interact with GPIO pins
# Import the time module for adding delays (e.g., for debouncing)
import time

from machine import Pin

# Define the GPIO pin number we'll be using.
# IMPORTANT: Pin numbering can vary between MicroPython boards.
# "G41" usually refers to GPIO41. If this doesn't work,
# you might need to use just the number 41 or a specific Pin.board name.
BUTTON_PIN_NUMBER: int = 41

# --- Pin Setup ---
# Configure the button pin as an input pin.
# Pin.IN: Sets the pin as an input.
# Pin.PULL_UP: Enables the internal pull-up resistor.
# This means the pin will be HIGH (1) when the button is not pressed,
# and LOW (0) when the button is pressed (connecting it to ground).
try:
    button_pin = Pin(BUTTON_PIN_NUMBER, Pin.IN, Pin.PULL_UP)
    print(f"Successfully configured GPIO{BUTTON_PIN_NUMBER} as an input with pull-up.")
except Exception as e:
    print(f"Error configuring GPIO{BUTTON_PIN_NUMBER}: {e}")
    print("Please check your MicroPython board's documentation for correct pin numbering.")
    # Exit or halt if pin setup fails, as the rest of the script depends on it.
    # For simplicity, we'll just let it try to run, but in a real app, handle this robustly.

# --- Main Loop ---
# This loop will run forever, constantly checking the button's state.
print(f"Listening for button presses on GPIO{BUTTON_PIN_NUMBER}...")

# Variable to store the previous state of the button
# We initialize it to the current state to avoid an immediate trigger if already pressed
# or to correctly detect the first press.
# Assuming button is not pressed at start, so pin is HIGH (1) due to PULL_UP.
previous_button_state: int = 1
if "button_pin" in locals():  # Check if button_pin was successfully initialized
    previous_button_state = button_pin.value()

while True:
    if "button_pin" in locals():  # Proceed only if button_pin exists
        # Read the current state of the button pin.
        # .value() returns 0 if the button is pressed (LOW) and 1 if not pressed (HIGH).
        current_button_state: int = button_pin.value()

        # Check if the button has just been pressed
        # This means the previous state was HIGH (1) and the current state is LOW (0).
        if previous_button_state == 1 and current_button_state == 0:
            print("CLICK")
            # Simple debounce: wait a short period to avoid multiple triggers
            # from a single mechanical button press (bouncing).
            time.sleep_ms(100)  # Wait for 100 milliseconds

        # Update the previous state for the next iteration
        previous_button_state = current_button_state

    # Add a small delay to prevent the loop from running too fast and consuming all CPU.
    # This also helps with debouncing if not handled explicitly after the print.
    time.sleep_ms(20)  # Check every 20 milliseconds
