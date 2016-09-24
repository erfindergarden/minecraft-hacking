# Adventure 9: CraftyCrossing.py

# From the book: "Adventures in Minecraft"
# written by David Whale and Martin O'Hanlon, Wiley, 2014
# http://eu.wiley.com/WileyCDA/WileyTitle/productCd-111894691X.html

#import modules
import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.minecraftstuff as minecraftstuff
import time
import random
import thread

#arena constants
ARENAX = 10
ARENAZ = 20
ARENAY = 3

#Create the Arena
def createArena(pos):
    #create connection to minecraft
    mc = minecraft.Minecraft.create()
    
    #Create the floor
    mc.setBlocks(pos.x - 1 , pos.y, pos.z - 1,
                 pos.x + ARENAX + 1, pos.y - 3, pos.z + ARENAZ + 1,
                 block.GRASS.id)

    #Create the walls on the outside of the arena
    mc.setBlocks(pos.x - 1, pos.y + 1, pos.z - 1,
                 pos.x + ARENAX + 1, pos.y + ARENAY, pos.z + ARENAZ + 1,
                 block.GLASS.id)
    mc.setBlocks(pos.x, pos.y + 1, pos.z,
                 pos.x + ARENAX, pos.y + ARENAY, pos.z + ARENAZ,
                 block.AIR.id)

#Build the obstacles
#The Wall
def theWall(arenaPos, wallZPos):
    #create connection to minecraft
    mc = minecraft.Minecraft.create()

    #create the wall shape
    wallPos = minecraft.Vec3(arenaPos.x, arenaPos.y + 1, arenaPos.z + wallZPos)
    #create the wall blocks
    wallBlocks = []
    for x in range(0, ARENAX + 1):
        for y in range(1, ARENAY):
            wallBlocks.append(minecraftstuff.ShapeBlock(x,
                                                        y,
                                                        0,
                                                        block.BRICK_BLOCK.id))
    wallShape = minecraftstuff.MinecraftShape(mc, wallPos, wallBlocks)

    #move the wall up and down
    while not gameOver:
        wallShape.moveBy(0,1,0)
        time.sleep(1)
        wallShape.moveBy(0,-1,0)
        time.sleep(1)

#The River
def theRiver(arenaPos, riverZPos):
    #create connection to minecraft
    mc = minecraft.Minecraft.create()
    
    #constants
    RIVERWIDTH = 4
    BRIDGEWIDTH = 2

    #create the river
    mc.setBlocks(arenaPos.x, arenaPos.y - 2, arenaPos.z + riverZPos,
                 arenaPos.x + ARENAX, arenaPos.y, arenaPos.z + riverZPos + RIVERWIDTH - 1,
                 block.AIR.id)
    #fill with water
    mc.setBlocks(arenaPos.x, arenaPos.y - 2, arenaPos.z + riverZPos,
                 arenaPos.x + ARENAX, arenaPos.y - 2, arenaPos.z + riverZPos + RIVERWIDTH - 1,
                 block.WATER.id)
    #create the bridge shape
    bridgePos = minecraft.Vec3(arenaPos.x, arenaPos.y, arenaPos.z + riverZPos + 1)
    #create the bridge blocks
    bridgeBlocks = []
    for x in range(0, BRIDGEWIDTH):
        for z in range(0, RIVERWIDTH - 2):
            bridgeBlocks.append(minecraftstuff.ShapeBlock(x,
                                                          0,
                                                          z,
                                                          block.WOOD_PLANKS.id))
    bridgeShape = minecraftstuff.MinecraftShape(mc, bridgePos, bridgeBlocks)

    #move the bridge left and right
    #how many steps are there between the left and right side of the arena
    steps = ARENAX - BRIDGEWIDTH
    while not gameOver:
        for left in range(0, steps):
            bridgeShape.moveBy(1,0,0)
            time.sleep(1)
        for right in range(0, steps):
            bridgeShape.moveBy(-1,0,0)
            time.sleep(1)

def theHoles(arenaPos, holesZPos):
    #create connection to minecraft
    mc = minecraft.Minecraft.create()
    
    #constants
    HOLES = 15
    HOLESWIDTH = 3
    
    while not gameOver:
        #create random holes which open up for a few seconds, close, then change to a different set of holes
        holes = []
        #find some random holes
        for count in range(0,HOLES):
            x = random.randint(arenaPos.x, arenaPos.x + ARENAX)
            z = random.randint(arenaPos.z + holesZPos, arenaPos.z + holesZPos + HOLESWIDTH)
            holes.append(minecraft.Vec3(x, arenaPos.y, z))
        #turn the holes black before opening them up
        for hole in holes:
            mc.setBlock(hole.x, hole.y, hole.z, block.WOOL.id, 15)
        time.sleep(0.25)
        #open up the holes
        for hole in holes:
            mc.setBlocks(hole.x, hole.y, hole.z,
                         hole.x, hole.y - 2, hole.z,
                         block.AIR.id)
        time.sleep(2)
        #close up the holes
        for hole in holes:
            mc.setBlocks(hole.x, hole.y, hole.z,
                         hole.x, hole.y - 2, hole.z,
                         block.GRASS.id)
        time.sleep(0.25)

#Place the diamonds
def createDiamonds(arenaPos, number):
    #create connection to minecraft
    mc = minecraft.Minecraft.create()

    #create the number of diamonds required
    for diamond in range(0, number):
        #create a random position
        x = random.randint(arenaPos.x, arenaPos.x + ARENAX)
        z = random.randint(arenaPos.z, arenaPos.z + ARENAZ)
        #create the diamond block
        mc.setBlock(x, arenaPos.y + 1, z, block.DIAMOND_BLOCK.id)

#Main program
#create minecraft object
mc = minecraft.Minecraft.create()

#create the gameOver flag
gameOver = False

#arena pos
arenaPos = mc.player.getTilePos()

#build the arena
createArena(arenaPos)

#create the wall
WALLZ = 10
#theWall(arenaPos, WALLZ)
thread.start_new_thread(theWall, (arenaPos, WALLZ))

#create the river
RIVERZ = 4
#theRiver(arenaPos, RIVERZ)
thread.start_new_thread(theRiver, (arenaPos, RIVERZ))

#create the holes
HOLESZ = 15
#theHoles(arenaPos, HOLESZ)
thread.start_new_thread(theHoles, (arenaPos, HOLESZ))

#level constants
LEVELS = 3
DIAMONDS = [3,5,9]
TIMEOUTS = [30,25,20]

#set level and points
level = 0
points = 0

#game loop, while not game over
while not gameOver:
    #create the diamonds
    createDiamonds(arenaPos, DIAMONDS[level])
    diamondsLeft = DIAMONDS[level]
    
    #position the player at the start of the arena
    mc.player.setPos(arenaPos.x + 1, arenaPos.y + 1, arenaPos.z + 1)

    #start the clock
    start = time.time()

    #set the level complete flag
    levelComplete = False
    #level loop
    while not gameOver and not levelComplete:
        #sleep for a bit
        time.sleep(0.1)

        #has player hit a diamond?
        hits = mc.events.pollBlockHits()
        for hit in hits:
            blockHitType = mc.getBlock(hit.pos.x, hit.pos.y, hit.pos.z)
            if blockHitType == block.DIAMOND_BLOCK.id:
                #turn the block to AIR
                mc.setBlock(hit.pos.x,hit.pos.y, hit.pos.z, block.AIR.id)
                #reduce the diamonds to collect by 1
                diamondsLeft = diamondsLeft - 1

        #get the players position
        pos = mc.player.getTilePos()
        
        #has player fallen down
        if pos.y < arenaPos.y:
            #put them back to the start
            mc.player.setPos(arenaPos.x + 1, arenaPos.y + 1, arenaPos.z + 1)
            
        #has the player got to the end of the arena and got all the diamonds?
        if pos.z == arenaPos.z + ARENAZ and diamondsLeft == 0:
            levelComplete = True

        #has the time expired
        secondsLeft = TIMEOUTS[level] - (time.time() - start)
        if secondsLeft < 0:
            gameOver = True
            mc.postToChat("Out of time...")

    #level complete?
    if levelComplete:
        #calculate points
        #1 points for every diamond
        #1 x multipler for every second left on the clock
        points = points + (DIAMONDS[level] * int(secondsLeft))
        mc.postToChat("Level Complete - Points = " + str(points))
        #set it to the next level
        level = level + 1
        #if its the last level, set it to gameOver
        if level == LEVELS:
            gameOver = True
            mc.postToChat("Congratulations - All levels complete")

#its game over
mc.postToChat("Game Over - Points = " + str(points))
