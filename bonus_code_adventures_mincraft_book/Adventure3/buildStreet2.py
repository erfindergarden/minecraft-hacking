# Adventure 3: buildStreet.py

# From the book: "Adventures in Minecraft"
# written by David Whale and Martin O'Hanlon, Wiley, 2014
# http://eu.wiley.com/WileyCDA/WileyTitle/productCd-111894691X.html
#
# This program builds a street of houses with random carpets.

# Import necessary modules
import mcpi.minecraft as minecraft
import mcpi.block as block

# A module to generate random numbers
import random

# Connect to Minecraft
mc = minecraft.Minecraft.create()

# A constant, that sets the size of your house
SIZE = 20

# define a new function, that builds a house
def house():
    # Calculate the midpoints of the front face of the house  
    midx = x+SIZE/2
    midy = y+SIZE/2

    # Build the outer shell of the house
    mc.setBlocks(x, y, z, x+SIZE, y+SIZE, z+SIZE, block.COBBLESTONE.id)
    
    # Carve the insides out with AIR      
    mc.setBlocks(x+1, y, z+1, x+SIZE-2, y+SIZE-1, z+SIZE-2, block.AIR.id)

    # Carve out a space for the doorway
    mc.setBlocks(midx-1, y, z, midx+1, y+3, z, block.AIR.id)

    # Carve out the left hand window
    mc.setBlocks(x+3, y+SIZE-3, z, midx-3, midy+3, z, block.GLASS.id)
    
    # Carve out the right hand window     
    mc.setBlocks(midx+3, y+SIZE-3, z, x+SIZE-3, midy+3, z, block.GLASS.id)

    # Add a wooden roof 
    mc.setBlocks(x, y+SIZE, z, x+SIZE, y+SIZE, z+SIZE, block.WOOD.id)
    
    # Add a woolen carpet, the colour is 14, which is red.
    mc.setBlocks(x+1, y-1, z+1, x+SIZE-2, y-1, z+SIZE-2, block.WOOL.id, 14)

    # Add a random carpet    
    c = random.randint(0, 15)
    mc.setBlocks(x+1, y+1, z+1, x+SIZE-1, y+1, z+SIZE-1, block.WOOL.id, c)
    
  
# Get the players position    
pos = mc.player.getTilePos()

# Decide where to start building the house, slightly away from player
x = pos.x + 2
y = pos.y
z = pos.z
  
# build 5 houses, for a whole street of houses
for h in range(5):
    # build one house
    house()
    # move x by the size of the house just built
    x = x + SIZE
    
# END


