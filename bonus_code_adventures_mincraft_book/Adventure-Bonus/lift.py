# Adventure Bonus: lift.py

# From the book: "Adventures in Minecraft"
# written by David Whale and Martin O'Hanlon, Wiley, 2014
# http://eu.wiley.com/WileyCDA/WileyTitle/productCd-111894691X.html
#
# This program builds a fully functional passenger lift.
# The lift is a footplate that moves up and down a lift shaft.
# You can press hardware buttons on a breadboard to choose which
# floor to travel to and it takes your player with you.
# You can also climb outside of the lift and hit one of many
# diamond "request blocks" on each floor, to request the lift to come
# to that floor to greet you.
# This program works on Raspberry Pi, PC and Mac.

# Import necessary modules
import mcpi.minecraft as minecraft
import mcpi.block as block
import time

# This module is needed to drive the 7-segment display
import anyio.seg7 as display

# Used on the Raspberry Pi
import RPi.GPIO as GPIO
# GPIO numbers of the 4 buttons
FLOOR_GPIO   = [4, 14, 23, 24] # the order is important
# GPIO numbers of the 8 LEDs inside the 7-seg display
DISPLAY_GPIO = [10, 22, 25, 8, 7, 9, 11, 15] # the order is important
# What type of display do you have?
ON           = False # True=common-cathode, False=common-anode

# Used on the Arduino on PC/Mac
#import anyio.GPIO as GPIO
# GPIO numbers of the 4 buttons
#FLOOR_GPIO   = [4, 5, 2, 3] # the order is important
# GPIO numbers of the 8 LEDs inside the 7-seg display
#DISPLAY_GPIO = [7, 6, 14, 16, 10, 8, 9, 15] # the order is important
# What type of display do you have?
#ON           = False # True=common-cathode, False=common-anode

# Create some constants for the floors.
# This will make it easier to add more floors later, or make the
# floors further apart or nearer to each other depending on the
# height of your building
NUM_FLOORS   = len(FLOOR_GPIO)
FLOOR_HEIGHT = 10 

# Create constants for the 3 different states that the lift can be in
STOPPED      = 0
GOING_DOWN   = 1
GOING_UP     = 2

# Connect to the Minecraft game
mc           = minecraft.Minecraft.create()

# Get the player position
pos          = mc.player.getTilePos()

# Create some constants for the lift position
# The position is moved slightly in the x and z dimensions
# This is so that it is not built on top of the players head
# This will build the lift at a position relative to your player
# If you want the lift at an absolute position (always at the
# same position regardless of where the player is), you can set
# these 3 constants to the x,y,z coordinates of the insides of
# your building, so the lift never gets relocated elsewhere
LIFT_X       = pos.x+3
LIFT_Y       = pos.y
LIFT_Z       = pos.z+3

# The lift starts off stopped, right at the bottom
lift_state   = STOPPED
lift_y       = LIFT_Y

# These 4 Boolean variables keep track of which floors have a request
# outstanding, such as when the player has pressed one of the
# hardware buttons, or has hit one of the diamond request blocks
# outside the lift entrance at each floor
lift_requests = [False, False, False, False]

# Define a function that creates the lift
# It carves out a lift shaft using AIR, so that if you build your lift
# inside a building or mountain, you will have a long column of AIR
# that the lift can go up and down. It puts diamond blocks outside
# of the entrance to the lift at each floor, so you know where to
# attach the floors of your building to.
def createLift():
  # loop for each floor
  for floor in range(NUM_FLOORS):
    # calculate the y coordinate of the height of this floor
    y = LIFT_Y + floor*FLOOR_HEIGHT
    # carve out a cube of air for the lift shaft for this whole floor
    mc.setBlocks(LIFT_X-2, y, LIFT_Z-2, LIFT_X+2, y+FLOOR_HEIGHT, LIFT_Z+2,
                 block.AIR.id)
    # place 3 diamond blocks at the entrance to the lift on this floor
    mc.setBlocks(LIFT_X+2, y, LIFT_Z-1, LIFT_X+2, y, LIFT_Z+1,
                 block.DIAMOND_BLOCK.id)
        
        
# Define a function that draws the lift at a certain height,
# using a certain block id number.
# A lift in this simple program is just a slab you can stand on
# called the footplate. There are no walls or ceiling or doors.
# y - the height that the lift needs drawing at
# blockid - the blockid to use for the footplate of the lift
def drawLift(y, blockid):
    mc.setBlocks(LIFT_X-1, y, LIFT_Z-1, LIFT_X+1, y, LIFT_Z+1, blockid)

# Define a function that works out if the player is in the lift or not.
# This geo-fences the whole lift shaft and works out if the player
# is in that area or not. This is a bit of a cheat, as it doesn't
# mean they are actually in the lift, but it's good enough.
def playerInLift():
  # Get the player position
  pos = mc.player.getTilePos()
  
  # Check if the player is within the lift shaft or not
  if pos.x >= LIFT_X-1 and pos.x <= LIFT_X+1 and pos.z >= LIFT_Z-1 and pos.z <= LIFT_Z+1:
    return True # They are in the lift
  return False # They are not in the lift


# Define a function that moves the lift up by one block
# It does this by un-building and re-building the footplate slab
# withPlayer - True if the player needs to move with the lift
def moveUp(withPlayer):
  # This function will change the value in the lift_y variable
  # so it must be listed as global here
  global lift_y
  
  # If the lift is moving with the player on the slab
  if withPlayer:
    # Move the player up by one block
    # This prevents the new lift slab being built on top of their feet
    mc.player.setPos(LIFT_X, lift_y+2, LIFT_Z)

  # build a new footplate 1 block higher than the existing footplate
  drawLift(lift_y+1, block.STONE.id)
  
  # delete the old footplate that is below the new footplate
  drawLift(lift_y, block.AIR.id)
  
  # Move the player up again
  # On slow computers, sometimes the player falls down before the
  # new footplate is built, so this prevents them from falling
  # down the whole lift shaft, by moving them up one block again
  if withPlayer:
    mc.player.setPos(LIFT_X, lift_y+2, LIFT_Z)

  # The lift has moved up by one block, so adjust the lift_y variable
  # so that it always holds the y coordinate of the lift
  lift_y = lift_y+1


# Define a function that moves the lift down by one block
# It does this by un-building and re-building the footplate slab
# withPlayer - True if the player needs to move with the lift
def moveDown(withPlayer):
  # This function will change the value in the lift_y variable
  # so it must be listed as global here
  global lift_y

  # Build a new footplate below the existing one
  drawLift(lift_y-1, block.STONE.id)
  
  # Delete the existing footplate
  drawLift(lift_y, block.AIR.id)
  
  # If the player is in the lift
  if withPlayer:
    # Make sure they move down with the lift
    # The player will naturally fall by gravity
    # but if flying is enabled, this forces them to move down
    mc.player.setPos(LIFT_X, lift_y+1, LIFT_Z)
    
  # The lift has moved down by one block, so adjust the lift_y variable
  # so that it always holds the y coordinate of the lift
  lift_y = lift_y-1

  
# Define a function that calculates the floor number for a y position
# y - the y position to calculate the floor number of
# This uses knowledge of the size of the lift shaft and number of floors
# to calculate the floor number
def getFloor(y):
  # Divide the height up the lift shaft by the height of the floors
  # and check if there is any remainder after that division
  remainder = (y-LIFT_Y) % FLOOR_HEIGHT

  # If there is no remainder, the lift is at a floor
  if remainder == 0:
    # Calculate the actual floor number
    return (y-LIFT_Y) / FLOOR_HEIGHT
    
  # The lift is not at a floor, so return "None" (no value)
  return None

# Define a function that looks for new requests for the lift
# A request can come from a hardware button, or a diamond hit event
def checkRequests():
  # This function changes the value of lift_requests
  # so it has to be listed as global here
  global lift_requests
  
  # CHECK FOR ANY DIAMOND HITS
  
  # loop through any hit events that have happened
  for e in mc.events.pollBlockHits():
    pos = e.pos
    
    # Work out the floor number of the y coordinate of this hit
    # Note how the getFloor() function is used in multiple places
    # inside this program, for different purposes
    floor = getFloor(pos.y)
    
    # If the lift is at a floor
    if floor != None:
      # Set the appropriate Boolean in the lift_requests
      # This remembers that there is a request for this floor
      # which will be processed elsewhere in this program
      lift_requests[floor] = True


  # CHECK FOR ANY HARDWARE BUTTON PRESSES

  # Hardware buttons are only looked at if the player is in the lift
  # This is because your player can't reach the buttons
  # if they are not in the lift!
  # Note how the playerInLift() function is used in multiple places
  # inside this program, for different purposes
  if playerInLift():
    # Loop through all the floors, one by one
    for floor in range(NUM_FLOORS):
      # Read the hardware button for this floor number
      if GPIO.input(FLOOR_GPIO[floor]) == False:
        # False means 0V, which means the button is pressed
        # Set the appropriate Boolean in the lift requests
        # This remembers that there is a request for this floor
        # which will be processed elsewhere in this program
        lift_requests[floor] = True
   
  # To help us debug the program, the lift requests are printed
  # on the Python Shell Window every time this function is called
  print(str(lift_requests))

# Define a function that performs necessary actions when the lift
# is at a particular floor
# floor - the floor numbe that the lift is now at
def atFloor(floor):
  # This function will change the values in these variables
  # so they must be listed as global here
  global lift_requests, lift_state

  # If there is a lift request pending for this floor
  if lift_requests[floor]:
    # Set the lift request to False, so the lift doesn't stick here
    lift_requests[floor] = False
    
    # The lift is now stopped (this will be used elsewhere)
    lift_state = STOPPED
    
    # Update the display hardware with the floor number
    display.write(str(floor))
    
    # Wait a couple of seconds to allow the player to walk on/off
    time.sleep(2)


# Define a function that chooses the next direction to move the lift
# depending on what other requests are pending, and where the lift is.
# This is a very simple algorithm that prioritises floors below the
# player first in the journey. This is normal for a lift, because
# most buildings have a lobby on the ground floor that is more
# popular than all other floors
def chooseNext(floor):
  # This function changes the lift_state variable
  # so it must be listed as global here
  global lift_state
  
  # Loop through all floors from the lowest to the highest
  for f in range(NUM_FLOORS):
    # If there is a request pending for this floor number
    if lift_requests[f]:
      # work out which direction the lift needs to trave
      # in order to get to the floor
      if f > floor:
        lift_state = GOING_UP
      else:
        lift_state = GOING_DOWN
      
      # 'return' from function immediately once direction is chosen
      # This prevents the loop looking at all other floors and
      # possibly making the wrong decision on the direction to use
      return


# Define a function that can be used for service engineers
# This allows them to manually move the lift up and down
# Pressing the first hardware button moves it up 1 block
# Pressing the second hardware button moves it down 1 block
# The main game loop should either use manualLift() or it should
# use autoLift(), but never both at the same time
def manualLift():
  # This function will change the value in lift_requests
  # so it has to be listed as global here
  global lift_requests
  
  # If there is a request on floor 0 (first button pressed)
  if lift_requests[0]:
    # Move the lift up one block
    moveUp(True)
    
    # Clear the lift request, to prevent the lift moving forever
    lift_requests[0] = False

  # else if there is a request on floor 1 (second button pressed)  
  elif lift_requests[1]:
    # Move the lift down one block
    moveDown(True)
    
    # Clear the lift request, to prevent the lift moving forever
    lift_requests[1] = False
    
  # Keep the display updated with the floor number
  # This is useful so that the service engineer can test the display
  floor = getFloor(lift_y)
  if floor != None:
    display.write(str(floor))

# Define a function that automatically moves the lift
# This is used in the main game loop, and you should either use
# autoLift() or use manualLift() but never both at the same time
def autoLift(): 
  # If the player is in the lift, the movement will have to also
  # move the player as well. Store this in a Boolean withPlayer
  # that can be used to alter how the move functions work later
  withPlayer = playerInLift()

  # Work out if the lift is at a afloor, and if so, which floor
  floor = getFloor(lift_y)
  
  # If the lift is at a floor
  if floor != None:
    # Perform the at-floor processing
    # which will stop the lift for a while
    atFloor(floor)
  
  
  # DECIDE WHAT TO DO NEXT
  # The lift can be in one of 3 states: GOING_UP, GOING_DOWN, STOPPED
  # Decide what to do for each of those 3 states
  
  if lift_state == GOING_UP:
    # Writing "up" to the display module will display a '^' symbol
    # which looks a little bit like an up arrow
    display.write("up")
    
    # Move the lift up by one block (with the player too
    # if the withPlayer variable is True)
    moveUp(withPlayer)
    
  elif lift_state == GOING_DOWN:
    # Writing "down" to the display module will display a 'v' symbol
    # which looks a little bit like a down arrow
    display.write("down")
    
    # Move the lift down by one blok (with the player too
    # if the withPlayer variable is True)
    moveDown(withPlayer)
    
  else:
    # Anything else, means the lift must be STOPPED
    # So, choose which floor to travel to next.
    # chooseNext() will change lift_state to GOING_UP or GOING_DOWN
    # which will then be processed next time this function is used
    chooseNext(floor)


# Define a function that destroys the lift
# When the game finishes, the lift needs to be destroyed
# otherwise you might get lots of "dead" inactive lifts all over
# the Minecraft world. If you want to always build the lift at
# a fixed location, you can change the constants at the top of this
# program to hold the absolute coordinates of your lift inside your
# building (rather than relative coordinates based on your position)
def destroyLift():
  # Clear all the space in the lift shaft and around it
  # which will remove the lift and the diamond request blocks
  mc.setBlocks(LIFT_X-2, LIFT_Y, LIFT_Z-2, LIFT_X+2, 
    LIFT_Y+(NUM_FLOORS*FLOOR_HEIGHT), LIFT_Z+2, block.AIR.id)


# Game loop

try: # if this code fails, it jumps to "finally"
  # Use Broadcom pin numbering scheme for GPIOs
  GPIO.setmode(GPIO.BCM)
  
  # Set all button GPIOs to be inputs so you can read their state
  for p in FLOOR_GPIO:
    GPIO.setup(p, GPIO.IN)
    
  # Setup the display ready for use
  display.setup(GPIO, DISPLAY_GPIO, ON)

  # Create the lift shaft, diamond request blocks, and footplate
  createLift()
  drawLift(lift_y, block.STONE.id)

  # Loop forever (or until CTRL-C)
  while True:
    # Delay a short time (to prevent computer being too busy!)
    time.sleep(0.5)
    
    # Check if there are any pending requests to process
    checkRequests()
    
    # Move the lift in automatic mode
    autoLift() # change to manualLift() if you want "service mode"
    
finally: # if code fails it comes here (e.g. CTRL-C pressed)
  # Make sure all GPIOs are left in a safe state
  GPIO.cleanup()
  
  # Remove all evidence of the lift
  # This is so that you don't get lots of phantom lifts in the world!
  # You can remove this if you always build your lift at same position
  destroyLift()

# END


