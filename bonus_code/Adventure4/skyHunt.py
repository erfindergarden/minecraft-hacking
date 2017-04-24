# Adventure 4: skyHunt.py

# From the book: "Adventures in Minecraft"
# written by David Whale and Martin O'Hanlon, Wiley, 2014
# http://eu.wiley.com/WileyCDA/WileyTitle/productCd-111894691X.html
#
# This program is a treasure hunt game.
# It places treasure randomly near your player in the sky.
# You have to find this treasure in the fewest moves possible,
# because as you move you leave a trail of gold behind you.
# Each block of gold costs you points from your score.
# When you find the treasure, the gold trail melts away leaving
# holes in the ground for you to fall down, and another block
# of treasure is placed at a random location.

# Import necessary modules
import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import random # used generate random numbers

# Connect to the Minecraft game
mc = minecraft.Minecraft.create()

# Create a variable to keep track of your score
score = 0

# Create a constant that sets how far away to create the treasure
RANGE = 5

# There is no treasure yet, but create the global variables to use later
# Set these to None as they have no value yet, but the variables need
# to be created here to prevent an error later
treasure_x = None
treasure_y = None
treasure_z = None


# Define a function that places a new piece of treasure
# It will place the treasure at a random location
# but this location will be close to your player
def placeTreasure():
  # This function will change the values in these global variables
  # so you must list them as global here
  global treasure_x, treasure_y, treasure_z
  
  # Get the position of the player
  pos = mc.player.getTilePos()
  
  # Calculate a random position for the treasure
  # This is within 'RANGE' blocks from the player position
  # and also always slightly higher up in the sky
  # Note how the treasure_ variables are given a new value here
  # which means they no longer have 'None' stored in them.
  # This signals to the main loop that the treasure is now placed
  treasure_x = random.randint(pos.x,   pos.x+RANGE)
  treasure_y = random.randint(pos.y+2, pos.y+RANGE)
  treasure_z = random.randint(pos.z,   pos.z+RANGE)
  
  # Place the treasure in the world at the new position
  mc.setBlock(treasure_x, treasure_y, treasure_z, block.DIAMOND_BLOCK.id)
  
  
# Define a function that checks if the diamond treasure has been hit
# You wrote this function in an earlier program, it is similar
def checkHit():
  # This function will change the values in these global variables
  # so you must list them as gloal here
  global score
  global treasure_x
  
  # Get a list of hit events that have happened
  events = mc.events.pollBlockHits()
  
  # Process each event in turn
  for e in events:
    # Get the coordinate that the hit happened at
    pos = e.pos
    
    # If the diamond treasure was hit
    if pos.x == treasure_x and pos.y == treasure_y and pos.z == treasure_z:
      mc.postToChat("HIT!")
      # Increase the score
      score = score + 10
      
      # Delete the treasure so it disappears
      mc.setBlock(treasure_x, treasure_y, treasure_z, block.AIR.id)
      
      # Set treasure_x to None so that the game loop knows that there
      # is no longer any treasure, and it will place a new block of
      # treasure when it is ready
      treasure_x = None
  

# Create a timer variable that counts 10 loops of the game loop  
TIMEOUT = 10
timer = TIMEOUT

# Define a function that displays the homing beacon on the Minecraft chat
def homingBeacon():
  # This function changes the value in the timer variable
  # so it must be listed as global here
  global timer
  
  # Treasure will be present in the sky if the treasure_x variable
  # has a value. If it has no value (None), then there is no treasure.
  # Check to see if a piece of treasure has been placed
  if treasure_x != None:
    # There is a piece of treasure in the world somewhere
    
    # You only want to update the homing beacon every 10 times
    # round the game loop, so count down from 10
    timer = timer - 1
    if timer == 0:
      # Once you have counted 10 game loops, 1 second has passed
      # re-set the timer so that it starts counting another 10 game loops
      timer = TIMEOUT
      
      # Get the position of the player
      pos = mc.player.getTilePos()
      
      # Calculate a rough number that estimates distance to the treasure
      diffx = abs(pos.x - treasure_x)
      diffy = abs(pos.y - treasure_y)
      diffz = abs(pos.z - treasure_z)
      diff = diffx + diffy + diffz
      
      # Display score and estimate to treasure location on the Minecraft chat
      mc.postToChat("score:" + str(score) + " treasure:" + str(diff))  


# Just like in your vanishingBridge.py program, create an empty bridge list
# there are no blocks in the bridge yet
bridge = []

# Define a function to build a bridge of gold blocks
# This is similar to the one you wrote in vanishingBridge.py
def buildBridge():
  # This function will change the value in the score variable
  # so it has to be listed as global here
  global score
  
  # Get the position of the player
  pos = mc.player.getTilePos()
  
  # Get the id of the block directly below the player
  b = mc.getBlock(pos.x, pos.y-1, pos.z)

  # Has the treasure been found and deleted?
  if treasure_x == None:
    # Are there still blocks remaining in the gold bridge?
    if len(bridge) > 0:
      # Remove the last coordinate of the bridge from the bridge list
      coordinate = bridge.pop()
      
      # Delete that block of the bridge by setting it to AIR
      mc.setBlock(coordinate[0], coordinate[1], coordinate[2], block.AIR.id)
      
      # Display a helpful countdown message on the Minecraft chat
      mc.postToChat("bridge:" + str(len(bridge)))
      
      # Delay for a while, so that the bridge disappears slowly
      time.sleep(0.25)

  elif b != block.GOLD_BLOCK.id:
    # There is treasure, and you are not already standing on gold
    # build another gold block below your player
    mc.setBlock(pos.x, pos.y-1, pos.z, block.GOLD_BLOCK.id)
    
    # Remember the coordinate of this new gold block...
    coordinate = [pos.x, pos.y-1, pos.z]
    # ...by adding it to the end of the bridge list
    bridge.append(coordinate)

    # You loose one point for each block of the bridge that is built
    score = score - 1
 
# Main game loop
while True:
  # Run the loop 10 times every second
  # It needs to run quite fast so that the program responds well
  time.sleep(0.1)

  # If there is no treasure placed yet,
  # and if a bridge has not yet been built
  if treasure_x == None and len(bridge) == 0:
    # Place a new treasure block randomly
    placeTreasure()

  # Perform any bridge-building activities
  buildBridge()
  
  # Perform any homing-beacon activitites
  homingBeacon()
  
  # Perform any hit-checking activities
  checkHit()
  
# END

