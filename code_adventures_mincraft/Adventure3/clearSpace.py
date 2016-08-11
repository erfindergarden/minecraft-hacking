# Adventure 3: clearSpace.py

# From the book: "Adventures in Minecraft"
# written by David Whale and Martin O'Hanlon, Wiley, 2014
# http://eu.wiley.com/WileyCDA/WileyTitle/productCd-111894691X.html
#
# This program clears some space near your player.
# This is so that it is then easier for you to build other things.

# Import necessary modules
import mcpi.minecraft as minecraft
import mcpi.block as block

# Connect to the Minecraft game
mc = minecraft.Minecraft.create()

# Get the player position
pos = mc.player.getTilePos()

# Ask the user how big a space to clear
size = int(raw_input("size of area to clear? "))

# Clear a space size by size*size*size, by setting it to AIR
mc.setBlocks(pos.x, pos.y, pos.z, pos.x+size, pos.y+size, pos.z+size,
             block.AIR.id)

# END
