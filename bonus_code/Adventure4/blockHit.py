# Adventure 4: blockHit.py

# From the book: "Adventures in Minecraft"
# written by David Whale and Martin O'Hanlon, Wiley, 2014
# http://eu.wiley.com/WileyCDA/WileyTitle/productCd-111894691X.html
#
# This program senses that a block has been hit.

# Import necessary modules
import mcpi.minecraft as minecraft
import mcpi.block as block
import time

# Connect to the Minecraft game
mc = minecraft.Minecraft.create()

# Work out the position of the player
diamond_pos = mc.player.getTilePos()

# Move the diamond slightly away from the player position
diamond_pos.x = diamond_pos.x + 1

# Build a diamond treasure block
mc.setBlock(diamond_pos.x, diamond_pos.y, diamond_pos.z, block.DIAMOND_BLOCK.id)

# Define a function that checks if the diamond treasure has been hit
# You can reuse this function in other programs
def checkHit():
  # Get a list of hit events that have happened
  events = mc.events.pollBlockHits()
  
  # Process each event in turn
  for e in events:
    # Get the coordinate that the hit happened at
    pos = e.pos
    
    # If the diamond was hit
    if pos.x == diamond_pos.x and pos.y == diamond_pos.y and pos.z == diamond_pos.z:     
      mc.postToChat("HIT")

# Game loop
while True:
  # Run the game loop once every second
  # Don't run it too fast or your computer might crash
  time.sleep(1)
  
  # Check to see if the diamond treasure has been hit
  checkHit()

# END

