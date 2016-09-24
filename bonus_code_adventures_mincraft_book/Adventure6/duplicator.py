# Adventure 6: duplicator.py

# From the book: "Adventures in Minecraft"
# written by David Whale and Martin O'Hanlon, Wiley, 2014
# http://eu.wiley.com/WileyCDA/WileyTitle/productCd-111894691X.html
#
# This program builds a huge 3D duplicating machine.
# The machine can be used to scan and to print 3D objects all around
# the Minecraft world. Objects can be saved to a CSV file, loaded
# back into the duplicator room, and duplicated all over the world.

# Import necessary modules
import mcpi.minecraft as minecraft
import mcpi.block as block
import glob # needed to handle filename wildcards
import time
import random

# Connect to the Minecraft game
mc = minecraft.Minecraft.create()

# Set some constants for the size of the duplicator room
SIZEX = 10
SIZEY = 10
SIZEZ = 10

# Set a default location for the duplicator room
roomx = 1
roomy = 1
roomz = 1


# Define a function that builds the duplicator room
# It will build it at x,y,z
def buildRoom(x, y, z):
  # These 3 variables will have their value changed by this function
  # so they have to be listed as global here
  global roomx, roomy, roomz
  
  # Remember where the room has been built
  # so that it can be demolished later on
  roomx = x
  roomy = y
  roomz = z
  
  # Build the duplicator room out of glass
  mc.setBlocks(roomx, roomy, roomz, 
    roomx+SIZEX+2, roomy+SIZEY+2, roomz+SIZEZ+2, block.GLASS.id)
    
  # Carve the insides and front face out with air
  mc.setBlocks(roomx+1, roomy+1, roomz, 
    roomx+SIZEX+1, roomy+SIZEY+1, roomz+SIZEZ+1, block.AIR.id)    


# Define a function that demolishes the room
def demolishRoom():
  # Set the whole area, including walls and contents, to air
  # Note how the roomx, roomy and roomz are used to remember
  # where the room was built in the first place
  mc.setBlocks(roomx, roomy, roomz, 
    roomx+SIZEX+2, roomy+SIZEY+2, roomz+SIZEZ+2, block.AIR.id)


# Define a function to clean just the contents of the room
def cleanRoom():
  # Set the whole inside area to AIR
  mc.setBlocks(roomx+1, roomy+1, roomz+1, 
    roomx+SIZEX+1, roomy+SIZEY+1, roomz+SIZEZ+1, block.AIR.id)
  
  
# Define a function that lists all CSV files
def listFiles():
  print("\nFILES:")

  # Get a list of files matching the wildcard *.csv into 'files'
  files = glob.glob("*.csv")
  
  # Loop through each filename in the list
  for filename in files:
    print(filename)
    
  # Print a blank line at the end
  # This is so that it separates the file list from the menu display
  print("\n")    
    
    
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
    mc.postToChat("scan:" + str(y)) # so you can see it working
    
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
  
  
# Define a function that will print the contents of any file
# at any x,y,z coordinate in the Minecraft world
# filename - is the name of the file to open
# x,y,z - these are the coordinates of the origin (bottom corner)  
def print3D(filename, originx, originy, originz):
  # Open the data file in read mode  
  f = open(filename, "r")
  
  # Read all lines from the file into a 'lines' list variable  
  lines = f.readlines()

  # The first line in the file is the metadata, it holds the 3 sizes
  # Split this line into parts, and set 3 variables, one for each size
  coords = lines[0].split(",")
  sizex = int(coords[0])
  sizey = int(coords[1])
  sizez = int(coords[2])
  
  # Use the 'lineidx' variable to keep track of the line number
  # in the loop below. Each time arount the loop, this will set to
  # the next line number, so that your loop processes one line at a time
  lineidx = 1
  
  # This first for loop scans through each vertical layer of the file  
  for y in range(sizey):
    mc.postToChat("print:" + str(y)) # so you can see what it is doing
    
    # Advance to the next line index    
    lineidx = lineidx + 1
    
    # This inner loop reads through each east/west position in a line    
    for x in range(sizex):
      # Get the whole line at this 'lineidx'      
      line = lines[lineidx]
      
      # Advance to the next line index      
      lineidx = lineidx + 1
      
      # Split this line into separate cells, at each comma      
      data = line.split(",")
      
      # This (third) inner loop reads through each north/south position      
      for z in range(sizez):
        blockid = int(data[z])
        mc.setBlock(originx+x, originy+y, originz+z, blockid)
  
  
# Define a function that displays the menu
# This function will also ask the user for a choice number
# and it will check if the number in range or not.
# If it is not in range it will display the menu and try again
def menu():
  while True:
    print("DUPLICATOR MENU")
    print(" 1. BUILD the duplicator room")
    print(" 2. LIST files")
    print(" 3. SCAN from duplicator room to file")
    print(" 4. LOAD from file into duplicator room")
    print(" 5. PRINT from duplicator room to player.pos")
    print(" 6. CLEAN the duplicator room")
    print(" 7. DEMOLISH the duplicator room")
    print(" 8. QUIT")
  
    choice = int(raw_input("please choose: "))
    if choice < 1 or choice > 8:
      print("Sorry, please choose a number between 1 and 8")
    else:
      return choice
      

# Game loop

# The anotherGo boolean variable decides if we want to go round 
# the game loop another time
anotherGo = True

while anotherGo:
  # Display the menu and get a choice from the user
  choice = menu()
  
  if choice == 1: # BUILD
    # Build the room at the players position
    pos = mc.player.getTilePos()
    buildRoom(pos.x, pos.y, pos.z)
    
  elif choice == 2: # LIST
    # List all matching CSV files
    listFiles()
    
  elif choice == 3: # SCAN
    # Ask the user for a file to scan into
    filename = raw_input("filename?")
    
    # Scan from the duplicator room into the file
    scan3D(filename, roomx+1, roomy+1, roomz+1)
    
  elif choice == 4: # LOAD
    # Ask the user for a file to load from
    filename = raw_input("filename?")
    
    # Load the file into the duplicator room
    print3D(filename, roomx+1, roomy+1, roomz+1)
    
  elif choice == 5: # PRINT
    # Note, this is a really neat solution here, by reusing
    # the scan3D and print3D functions, and scanning via a temporary
    # file called 'scantemp' - it means you don't have to write
    # lots of extra printing and scanning code in order to offer this
    # option to your user
    
    # Scan the room into a temporary file called 'scantemp'
    scan3D("scantemp", roomx+1, roomy+1, roomz+1)
    
    # Get the position of the player
    pos = mc.player.getTilePos()
    
    # Print the contents of the temporary file 'scantemp' here
    print3D("scantemp", pos.x+1, pos.y, pos.z+1)
    
  elif choice == 6: # CLEAN
    # Clean out just the insides of the room
    cleanRoom()
    
  elif choice == 7: # DEMOLISH
    # Remove all trace of the room by demolishing it
    # This makes sure you don't leave lots of "dead" rooms in your world
    demolishRoom()
    
  elif choice == 8: # QUIT
    # Finish the program
    # When anotherGo is False, the while loop (above) will finish
    anotherGo = False
    
# END

