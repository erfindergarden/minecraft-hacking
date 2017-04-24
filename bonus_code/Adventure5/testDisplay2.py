# Adventure 5: testDisplay2.py

# From the book: "Adventures in Minecraft"
# written by David Whale and Martin O'Hanlon, Wiley, 2014
# http://eu.wiley.com/WileyCDA/WileyTitle/productCd-111894691X.html
#
# This program shows how to write patterns to a 7-Segment LED display.
# It uses a display module written by David, that makes the use
# of different patterns for different letters and numbers and symbols
# very easy to generate.
# This works on Raspberry Pi, PC and Mac.

# Import necessary modules

# The anyio.seg7 module is written by David, and provided for free
# It makes it really easy to display any pattern on a 7-Segment display
# Get it from here:
#   https://github.com/whaleygeek/anyio/blob/master/anyio/seg7.py

import anyio.seg7 as display
import time

import RPi.GPIO as GPIO  # use this for Raspberry Pi
# Define a list of GPIO numbers. The order here is important
LED_PINS = [10,22,25,8,7,9,11,15]  # Use this for Raspberry Pi

#import anyio.GPIO as GPIO  # Use this for Arduino on PC/Mac
# Define a list of GPIO numbers. The order here is important
#LED_PINS = [7,6,14,16,10,8,9,15]  # Use thsi for Arduino on PC/Mac

# Use Broadcom pin numbering (GPIO numbers, not connector pin numbers)
GPIO.setmode(GPIO.BCM)

# The suggested display is common-anode
# This means all the positive sides of the LEDs are connected together
# and thus you set the output to False (0V) to turn the LED on.
# A common-anode display has its common pin connected to 3.3V

# If you set this to True, it drives a common-cathode display
# This means all the negative sides of the LEDs are connected together
# and thus you set the output to True (3.3V) to turn the LED on.
# A common-cathode display has its common pin connected to 0V

ON = False # False=common-anode. Set to True for a common-cathode display

# Setup the display module by giving it access to your GPIOs,
# giving it a list of the pin numbers to use for each segment of the display,
# and telling it whether you are using common-anode or common-cathode
display.setup(GPIO, LED_PINS, ON)

# Game loop
try: # if this code fails, jumps to "finally"
  while True:
    # Count from 0 to 9
    for d in range(10):
      # The display module turns the numbers 0..9 into patters
      # and turns the LEDs on and off for you
      display.write(str(d))
      # Slow the program down so you can see it counting on the display
      time.sleep(0.5)
finally: # Gets here if the above program fails (e.g. you press CTRL-C)
  # Put all of the GPIO hardware in a safe state. This turns off all the LEDs
  GPIO.cleanup()
  
# END
