# Adventure 3: dice.py

# From the book: "Adventures in Minecraft"
# written by David Whale and Martin O'Hanlon, Wiley, 2014
# http://eu.wiley.com/WileyCDA/WileyTitle/productCd-111894691X.html
#
# This program builds the face of a dice near your player.

# Import necessary modules
import mcpi.minecraft as minecraft
import mcpi.block as block

# Connect to the Minecraft game
mc = minecraft.Minecraft.create()

# Get the player position
pos = mc.player.getTilePos()

# Create 6 blocks in front of the player, that look like a dice
mc.setBlock(pos.x+3, pos.y,   pos.z,   block.STONE.id)
mc.setBlock(pos.x+3, pos.y+2, pos.z,   block.STONE.id)
mc.setBlock(pos.x+3, pos.y+4, pos.z,   block.STONE.id)
mc.setBlock(pos.x+3, pos.y,   pos.z+4, block.STONE.id)
mc.setBlock(pos.x+3, pos.y+2, pos.z+4, block.STONE.id)
mc.setBlock(pos.x+3, pos.y+4, pos.z+4, block.STONE.id)

# END

