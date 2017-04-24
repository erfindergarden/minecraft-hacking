# Adventure 5: testLED.py

# From the book: "Adventures in Minecraft"
# written by David Whale and Martin O'Hanlon, Wiley, 2014
# http://eu.wiley.com/WileyCDA/WileyTitle/productCd-111894691X.html
#
# This program tests that you can flash an LED connected to your computer.
# This works on Raspberry Pi, PC and Mac.

# Import necessary modules
import time
import RPi.GPIO as GPIO     # use this for Raspberry Pi
#import anyio.GPIO as GPIO  # use this for Arduino on PC/Mac

# This is the GPIO number that the LED is attached to
# It's not the same as the pin number on the connector though!
LED = 15

# Use Broadcom pin numbering (GPIO numbers, not connector pin numbers)
GPIO.setmode(GPIO.BCM)

# Configure the LED GPIO to be an output, so that you can
# change the voltage on it and thus turn the LED on and off
GPIO.setup(LED, GPIO.OUT)

# Define a function that flashes the LED once
# The 't' variable holds the time to flash for
def flash(t):
  # True puts 3.3 Volts on the pin connected to the LED, the LED goes on
  GPIO.output(LED, True)
  time.sleep(t)
  
  # False puts 0 Volts on the pin connected to the LED, the LED goes off
  GPIO.output(LED, False)
  time.sleep(t)

# Game loop
try: # Try to run this code, jump to "finally" if it fails
  while True:
    # Flash your LED 0.5 seconds ON, 0.5 seconds OFF
    flash(0.5)
    
finally: # always gets here if your code fails (e.g. you CTRL-C the program)
  # Always use this function, to leave the GPIO hardware in a safe state
  GPIO.cleanup()
  
# END

  
