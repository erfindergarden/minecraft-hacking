# Adventure 6: csvBuild.py

# From the book: "Adventures in Minecraft"
# written by David Whale and Martin O'Hanlon, Wiley, 2014
# http://eu.wiley.com/WileyCDA/WileyTitle/productCd-111894691X.html
#
# This program builds mazes in the Minecraft world.
# The maze data is stored in a CSV file.

# Import necessary modules
import mcpi.minecraft as minecraft
import mcpi.block as block

# Connect to the Minecraft game
mc = minecraft.Minecraft.create()

# Define some constants for the different blocks you will use
# to build your maze out of. This allows you to experiment with
# different blocks and create interesting mazes
GAP   = block.AIR.id
WALL  = block.GOLD_BLOCK.id
FLOOR = block.GRASS.id

# This is the name of the file to read maze data from.
# It is a constant, so that you can change it easily to read from
# other data files in the future
FILENAME = "maze1.csv"

# Open the file containing your maze data
f = open(FILENAME, "r")

# Get the player position, and work out coordinates of the bottom corner
# The x and z are moved slightly to make sure that the maze doesn't get
# built on top of your players head
pos = mc.player.getTilePos()
ORIGIN_X = pos.x+1
ORIGIN_Y = pos.y
ORIGIN_Z = pos.z+1

# The z coordinate will vary at the end of each line of data
# So start it off at the origin of the maze
z = ORIGIN_Z

# Loop around every line of the file
for line in f.readlines():
  # Split the line into parts, wherever there is a comma
  data = line.split(",")
  
  # Restart the x coordinate every time round the "for line" loop
  x = ORIGIN_X
  
  # This is a nested loop (a loop inside another loop)
  # It loops through every item in the "data" list
  # It loops through cells, just like cells in a spreadsheet
  for cell in data:
    # Check if this cell of data is a gap or a wall
    if cell == "0": # f.readlines read it in as a string, so use quotes
      # choose the gap block id
      b = GAP
    else:
      # otherwise choose the wall block id
      b = WALL
      
    # build two layers of the required block id (held in the b variable)
    mc.setBlock(x, ORIGIN_Y, z, b)
    mc.setBlock(x, ORIGIN_Y+1, z, b)
    
    # build one layer of floor underneat it
    mc.setBlock(x, ORIGIN_Y-1, z, FLOOR)
    
    # move to the next x coordinate at the end of this "for cell" loop
    x = x + 1
    
  # move to the next z coordinate at the end of this "for line" loop
  z = z + 1

# END
