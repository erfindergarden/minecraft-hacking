# Adventure 8: AlienInvasion.py

# From the book: "Adventures in Minecraft"
# written by David Whale and Martin O'Hanlon, Wiley, 2014
# http://eu.wiley.com/WileyCDA/WileyTitle/productCd-111894691X.html

import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.minecraftstuff as minecraftstuff
import math
import time
import random

#function get the distance between 2 points
def distanceBetweenPoints(point1, point2):
    xd = point2.x - point1.x
    yd = point2.y - point1.y
    zd = point2.z - point1.z
    return math.sqrt((xd*xd) + (yd*yd) + (zd*zd))

#constants
# will go here!
HOVER_HEIGHT = 15
ALIEN_TAUNTS = ["<aliens>You cant run forever",
                "<aliens>Resistance is useless",
                "<aliens>We only want to be friends"]

#create minecraft and minecraftdrawing objects
mc = minecraft.Minecraft.create()
mcdrawing = minecraftstuff.MinecraftDrawing(mc)

#set the aliens position
alienPos = mc.player.getTilePos()
alienPos.y = alienPos.y + 50

#set the flying saucer's mode
mode = "landing"

#create the shape for our flying saucer
alienBlocks = [minecraftstuff.ShapeBlock(-1,0,0,block.WOOL.id, 5),
               minecraftstuff.ShapeBlock(0,0,-1,block.WOOL.id, 5),
               minecraftstuff.ShapeBlock(1,0,0,block.WOOL.id, 5),
               minecraftstuff.ShapeBlock(0,0,1,block.WOOL.id, 5),
               minecraftstuff.ShapeBlock(0,-1,0,block.GLOWSTONE_BLOCK.id),
               minecraftstuff.ShapeBlock(0,1,0,block.GLOWSTONE_BLOCK.id)]

alienShape = minecraftstuff.MinecraftShape(mc, alienPos, alienBlocks)

#loop
while mode != "missionaccomplished":
    #get the players position
    playerPos = mc.player.getTilePos() 

    # if its landing, set target to be above players head
    if mode == "landing":
        mc.postToChat("<aliens> We dont come in peace - please panic")
        alienTarget = playerPos.clone()
        alienTarget.y = alienTarget.y + HOVER_HEIGHT
        mode = "attack"
    elif mode == "attack":
        #check to see if the alien ship is above the player
        if alienPos.x == playerPos.x and alienPos.z == playerPos.z:
            #the alienship is above the player
            mc.postToChat("<aliens>We have you now!")
            
            # create a room
            mc.setBlocks(0,50,0,6,56,6,block.BEDROCK.id)
            mc.setBlocks(1,51,1,5,55,5,block.AIR.id)
            mc.setBlock(3,55,3,block.GLOWSTONE_BLOCK.id)
            
            #beam up player
            mc.player.setTilePos(3,51,5)
            time.sleep(10)
            mc.postToChat("<aliens>Not very interesting at all - send it back")
            time.sleep(2)

            #send the player back to the original position
            mc.player.setTilePos(playerPos.x, playerPos.y, playerPos.z)

            #clear the room
            mc.setBlocks(0,50,0,6,56,6,block.AIR.id)
            mode = "missionaccomplished"

        else:
            #the player got away
            mc.postToChat(ALIEN_TAUNTS[random.randint(0,len(ALIEN_TAUNTS)-1)])
            alienTarget = playerPos.clone()
            alienTarget.y = alienTarget.y + HOVER_HEIGHT

    #move the flying saucer towards its target
    if alienPos != alienTarget:
        #get the blocks in between block friend and player, by 'drawing' an imaginary line
        blocksBetween = mcdrawing.getLine(alienPos.x, alienPos.y, alienPos.z,
                                          alienTarget.x, alienTarget.y, alienTarget.z)
        #loop through the blocks in between the alien and the target
        for blockBetween in blocksBetween:
            #move the block friend to the next block
            # move the alien shape to the new position
            alienShape.move(blockBetween.x, blockBetween.y, blockBetween.z)
            # time to sleep between each block move
            time.sleep(0.25)
        # we have reached our target, so set the target to be friend's position
        alienPos = alienTarget.clone()

#clear the alien ship
alienShape.clear()


