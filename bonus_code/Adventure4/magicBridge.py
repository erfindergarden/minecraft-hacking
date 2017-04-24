# Adventure 4: MagicBridge.py

# From the book: "Adventures in Minecraft"
# written by David Whale and Martin O'Hanlon, Wiley, 2014
# http://eu.wiley.com/WileyCDA/WileyTitle/productCd-111894691X.html
#
# This program builds a bridge under your feet as you walk around.

# Import necessary modules
import mcpi.minecraft as minecraft
import mcpi.block as block

# Connect to the Minecraft game
mc = minecraft.Minecraft.create()

# Define a function to build a bridge if your feet are not safe
# This function will be reusable in other programs
def buildBridge():
  # Get the players position
  pos = mc.player.getTilePos()
  
  # Get the block directly below your player
  b = mc.getBlock(pos.x, pos.y-1, pos.z)
  # Is the player unsafe?
  if b == block.AIR.id or b == block.WATER_FLOWING.id or b==block.WATER_STATIONARY.id:
    # If unsafe, build a glass block directly under the player
    mc.setBlock(pos.x, pos.y-1, pos.z, block.GLASS.id)

# Game loop
while True:
  # There is no delay here, this loop needs to run really fast
  # otherwise your bridge might not build quick enough and you will fall off
  buildBridge()

# END


