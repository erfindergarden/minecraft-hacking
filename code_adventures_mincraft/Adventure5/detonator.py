# Adventure 5: detonator.py

# From the book: "Adventures in Minecraft"
# written by David Whale and Martin O'Hanlon, Wiley, 2014
# http://eu.wiley.com/WileyCDA/WileyTitle/productCd-111894691X.html
#
# This program creates a big red detonator button.
# When the button is pressed, there is a countdown 4,3,2,1,0
# on the 7-Segment LED display, then the bomb goes off and a huge
# crater appears in Minecraft. You can use this to clear lots of
# space in the world to make it easier to build things.
# This works on Raspberry Pi, PC and Mac.

# Import necessary modules

import mcpi.minecraft as minecraft
import mcpi.block as block
import time

# The anyio.seg7 module is written by David, and provided for free
# It makes it really easy to display any pattern on a 7-Segment display
# Get it from here:
#   https://github.com/whaleygeek/anyio/blob/master/anyio/seg7.py
import anyio.seg7 as display

import RPi.GPIO as GPIO  # use this for Raspberry Pi
# Define a list of GPIO numbers. The order here is important
LED_PINS = [10,22,25,8,7,9,11,15]  # Use this for Raspberry Pi
BUTTON = 4 # Button connected to GPIO4

#import anyio.GPIO as GPIO  # Use this for Arduino on PC/Mac
# Define a list of GPIO numbers. The order here is important
#LED_PINS = [7,6,14,16,10,8,9,15]  # Use thsi for Arduino on PC/Mac
#BUTTON = 4 # Button connected to GPIO4

# Use Broadcom pin numbering (GPIO numbers, not connector pin numbers)
GPIO.setmode(GPIO.BCM)

# Setup the button GPIO to be an input (so you can read it's voltage)
GPIO.setup(BUTTON, GPIO.IN)

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

# Connect to the Minecraft game
mc = minecraft.Minecraft.create()

# Define a function that places and detonates a bomb
# You can reuse this function in other programs
# x,y,z are variables that indicate the coordinates for the bomb
def bomb(x, y, z):
  # Place a block of TNT
  mc.setBlock(x+1, y, z+1, block.TNT.id)
  
  # Count 6 numbers (from 0 to 5)
  for t in range(6):
    # Display the number sequence 5,4,3,2,1,0 on the 7-Seg display
    display.write(str(5-t))
    # Wait so that you can see the number
    time.sleep(1)
    
  mc.postToChat("BANG!")
  # Just like clearSpace.py, clear a "crater" around the player
  # The crater is centered around your player
  mc.setBlocks(x-10, y-5, z-10, x+10, y+10, z+10, block.AIR.id)
  
# game loop
try: # if this code fails, jumps to "finally"
  while True:
    # Read the switch 10 times per second (0.1 of a second delay)
    time.sleep(0.1)
    if GPIO.input(BUTTON) == False:
      # If the input reads false (0V) the button is pressed
      # Get the position of the player
      pos = mc.player.getTilePos()
      
      # Drop a bomb where the player is standing
      bomb(pos.x, pos.y, pos.z)
      
finally: # Gets here if the above program fails (e.g. you pressed CTRL-C)
  # Put all of the GPIO hardware in a safe state. This turns off the LEDs
  GPIO.cleanup()

# END
