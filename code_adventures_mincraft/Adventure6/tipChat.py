# Adventure 6: tipChat.py

# From the book: "Adventures in Minecraft"
# written by David Whale and Martin O'Hanlon, Wiley, 2014
# http://eu.wiley.com/WileyCDA/WileyTitle/productCd-111894691X.html
#
# This program posts random hints and tips to the Minecraft chat.
# It reads those hits and tips from a separate text file.

# Import necessary modules
import mcpi.minecraft as minecraft
import time
import random

# Connect to the Minecraft game
mc = minecraft.Minecraft.create()

# Set a constant for the filename, so that you can easily change it 
# to read a different file later
FILENAME = "tips.txt"

# Open the file in read mode
f = open(FILENAME, "r")

# Read all lines from the file into a list called 'tips'
tips = f.readlines()

# Close the file when you have finished with it.
f.close()

# Game loop
while True:
  # Wait a random time between 3 and 7 seconds
  time.sleep(random.randint(3, 7))
  
  # Choose a random message from the 'tips' list
  msg = random.choice(tips)
  
  # Give the tip to the player. strip() strips out unwanted newlines
  mc.postToChat(msg.strip())
  
# END
