# Adventure 8: BlockFriend.py

# From the book: "Adventures in Minecraft"
# written by David Whale and Martin O'Hanlon, Wiley, 2014
# http://eu.wiley.com/WileyCDA/WileyTitle/productCd-111894691X.html

import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.minecraftstuff as minecraftstuff
import math
import time

#function get the distance between 2 points
def distanceBetweenPoints(point1, point2):
    xd = point2.x - point1.x
    yd = point2.y - point1.y
    zd = point2.z - point1.z
    return math.sqrt((xd*xd) + (yd*yd) + (zd*zd))

#constants
# how far away the block has to be before he stops following
TOO_FAR_AWAY = 15

#create minecraft and minecraftstuff objects
mc = minecraft.Minecraft.create()
mcdrawing = minecraftstuff.MinecraftDrawing(mc)

#set the blocks mood
blockMood = "happy"

#create the block next to the player
friend = mc.player.getTilePos()
friend.x = friend.x + 5
# find out the height of the world at x, y, so the friend is on top
friend.y = mc.getHeight(friend.x, friend.z)
# create the block 
mc.setBlock(friend.x, friend.y, friend.z, block.DIAMOND_BLOCK.id)
# say hello
mc.postToChat("<block> Hello friend")
# the friends target is where he currently is
target = friend.clone()

while True:

    #get players position
    pos = mc.player.getTilePos()
    distance = distanceBetweenPoints(pos, friend)
    #apply the rules to work out where the block should be doing next
    # am I happy?
    if blockMood == "happy":
        #where is the player?  Are they near enough to me or should I move to them?
        if distance < TOO_FAR_AWAY:
            target = pos.clone()
        if distance >= TOO_FAR_AWAY:
            blockMood = "sad"
            mc.postToChat("<block> Come back. You are too far away. I need a hug!")
    # am I sad?
    elif blockMood == "sad":
        #if Im sad, I'll wait for my friend to come close and give me a hug before I'm happy again
        #print distance
        if distance <= 1:
            blockMood = "happy"
            mc.postToChat("<block> Awww thanks. Lets go.")

    #move block to the target
    if friend != target:
        #get the blocks in between block friend and player, by 'drawing' an imaginary line
        blocksBetween = mcdrawing.getLine(friend.x, friend.y, friend.z,
                                          target.x, target.y, target.z)
        #loop through the blocks in between the friend and the target
        # loop to the last but 1 block (:-1) otherwise the friend will be sitting on top of the player
        for blockBetween in blocksBetween[:-1]:
            #move the block friend to the next block
            # clear the old block by making it air
            mc.setBlock(friend.x, friend.y, friend.z, block.AIR.id)
            # set the position of the block friend to be the next block in-line
            friend = blockBetween.clone()
            # get the height of the land at the new position
            friend.y = mc.getHeight(friend.x, friend.z)
            # draw the block friend in the new position 
            mc.setBlock(friend.x, friend.y, friend.z, block.DIAMOND_BLOCK.id)
            # time to sleep between each block move
            time.sleep(0.25)
        # we have reached our target, so set the target to be friend's position
        target = friend.clone()

    #sleep for a little bit to give the computer a rest!
    time.sleep(0.25)
    
