# Adventure 2: rent.py

# From the book: "Adventures in Minecraft"
# written by David Whale and Martin O'Hanlon, Wiley, 2014
# http://eu.wiley.com/WileyCDA/WileyTitle/productCd-111894691X.html
#
# This program is a game using geo-fencing.
# You are challenged to collect objects from a field in the shortest
# time possible. All the time you are in the field you are charged
# rent. You have to collect/destroy blocks by spending the minimum
# amount of rent. If you stay in the field for too long, your player
# is catapulted up into the sky and out of the field, which makes the
# game harder to play and much more fun!

# Import necessary modules
import mcpi.minecraft as minecraft
import time

# Connect to the Minecraft game
mc = minecraft.Minecraft.create()

# Define constants for the 4 coordinates of the geo-fence
X1 = 10
Z1 = 10
X2 = 20
Z2 = 20

# Constants for the place to move through when catapulted!
HOME_X = X2 + 2
HOME_Y = 10 # up in the sky
HOME_Z = Z2 + 2

# A variable to keep a tally of how much rent you have been charged
rent = 0

# A variable to hold the number of seconds the player is in the field
inField = 0

# The main game loop ticks round once every second
while True:
    # Slow the program down a bit, this also helps with timing things
    time.sleep(1) # the loop runs once every second
    
    # Get the players position
    pos = mc.player.getTilePos()

    # If the player is in the field, charge him rent
    if pos.x>X1 and pos.x<X2 and pos.z>Z1 and pos.z<Z2:
        # Charge £1 rent every time round the loop (1sec per loop)
        rent = rent + 1
        # Tell player how much rent they owe
        mc.postToChat("You owe rent:" + str(rent))
        # Count number of seconds player is in the field (1sec per loop)
        inField = inField + 1
    else: 
        # Not inside the field...
        inField = 0 # ...so reset the counter to zero

    # If player in field for more that 3 seconds...
    if inField>3:
        mc.postToChat("Too slow!")
        # ...catapult player outside of the field
        mc.player.setPos(HOME_X, HOME_Y, HOME_Z)

# END
