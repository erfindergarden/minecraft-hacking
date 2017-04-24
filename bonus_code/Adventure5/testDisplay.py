# Adventure 5: testDisplay.py

# From the book: "Adventures in Minecraft"
# written by David Whale and Martin O'Hanlon, Wiley, 2014
# http://eu.wiley.com/WileyCDA/WileyTitle/productCd-111894691X.html
#
# This program shows how to write patterns to a 7-segment LED display.
# This works on Raspberry Pi, PC and Mac.

# Import necessary modules
import RPi.GPIO as GPIO  # use this for Raspberry Pi

# Define a list of GPIO numbers. The order here is important
LED_PINS = [10,22,25,8,7,9,11,15]  # Use this for Raspberry PI

#import anyio.GPIO as GPIO  # Use this for Arduino on PC/Mac
# Define a list of GPIO numbers. The order here is important
#LED_PINS = [7,6,14,16,10,8,9,15]  # Use this for Arduino on PC/Mac

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

# loop through all 8 GPIO's setting them to outputs.
for g in LED_PINS:
  GPIO.setup(g, GPIO.OUT)
  
# Make a list of on/off values, one value for each LED in the display.
# The True/False values in this list represent the segments of the display
# in the following order: [A, B, C, D, E, F, G, Dp]
pattern = [True, True, True, True, True, True, True, False] # ABCDEFG No Dp

# Loop through all 8 values in your pattern list
for g in range(8):
  # if the pattern for index 'g' is True, the LED needs to be on
  if pattern[g]:
    # Turn the LED on
    GPIO.output(LED_PINS[g], ON)
  else:
    # Turn the LED off
    GPIO.output(LED_PINS[g], not ON)
    
# Wait for the ENTER key to be pressed on the keyboard
# This is needed because the next GPIO.cleanup() will turn off all LEDs!
raw_input("finished?")

# Put all of the GPIO hardware in a safe state. This turns off all LEDs
GPIO.cleanup()

# END
