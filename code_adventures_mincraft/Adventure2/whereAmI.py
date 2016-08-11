# Adventure 2: whereAmI.py

# From the book: "Adventures in Minecraft"
# written by David Whale and Martin O'Hanlon, Wiley, 2014
# http://eu.wiley.com/WileyCDA/WileyTitle/productCd-111894691X.html
#
# This program works out where you are in the Minecraft world.
# It prints a message on the Minecraft chat, with your coordinates.

# The Minecraft API has to be imported before it can be used
import mcpi.minecraft as minecraft

# To communicate with a running Minecraft game, 
# you need a connection to that game.
mc = minecraft.Minecraft.create()

# Ask the Minecraft game for the position of your player
pos = mc.player.getTilePos()

# Display the coordinates of the player’s position
mc.postToChat("x="+str(pos.x) + " y="+str(pos.y) +" z="+str(pos.z))

# END
