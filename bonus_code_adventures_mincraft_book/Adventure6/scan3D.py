# Adventure 6: scan3D.py

# From the book: "Adventures in Minecraft"
# written by David Whale and Martin O'Hanlon, Wiley, 2014
# http://eu.wiley.com/WileyCDA/WileyTitle/productCd-111894691X.html
#
# This program scans a region of the Minecraft world and stores
# a representation of the object in a CSV file.

# Import necessary modules
import mcpi.minecraft as minecraft
import mcpi.block as block

# Connect to the Minecraft game
mc = minecraft.Minecraft.create()

# Create some constants for the name of the file you want to scan to
# and the size of the object you want to scan
FILENAME = "tree.csv"
SIZEX = 5
SIZEY = 5
SIZEZ = 5

# Define a function that will scan at an x,y,z position to a file
# filename - name of the file to create
# originx,originy,originz - x,y,z coordinates of start of object to scan
def scan3D(filename, originx, originy, originz):
  # Open the file in write mode
  f = open(filename, "w")
  
  # Write the metadata line that has 3 sizes in it seprated by commas
  # the \n is a newline character (it presses ENTER for you at end)
  f.write(str(SIZEX) + "," + str(SIZEY) + "," + str(SIZEZ) + "\n")
  
  # Loop through all the y coordinates of the space to be scanned
  for y in range(SIZEY):
    # Write a blank line at the start of each layer of data
    f.write("\n")
    
    # Loop through all x coordinates of the space to be scanned
    for x in range(SIZEX):
      # Build up a "line" variable, it starts off empty
      line = ""
      
      # Loop through all z coordinates of the space to be scanned
      for z in range(SIZEZ):
        # get the block id at this x,y,z position
        blockid = mc.getBlock(originx+x, originy+y, originz+z)
        
        # If the "line" variable is empty, this is the first block
        # on this line, so it doesn't need a comma
        if line != "":
          # 'line' is not empty, so you must need a comma, so add it
          line = line + ","

        # Add the block id of this block to the end of 'line' variable
        line = line + str(blockid)
        
      # Note the indention. This is part of the 'for x' loop
      # write the whole line and press 'ENTER' at the end of it
      f.write(line + "\n")
      
  # Note the indentation. This is not part of any loop
  # Close the file when finished, so other programs can use it
  f.close()
  
  
# Get the position of the player
pos = mc.player.getTilePos()

# Scan an area into the file FILENAME
# It spans SIZEX,SIZEY,SIZEZ centered around the player,
# but note that it does not "dig down" under the player,
# which is why pos.y is used here
scan3D(FILENAME, pos.x-(SIZEX/2), pos.y, pos.z-(SIZEZ/2))

# END
