# Adventure 7: MinecraftClock.py

# From the book: "Adventures in Minecraft"
# written by David Whale and Martin O'Hanlon, Wiley, 2014
# http://eu.wiley.com/WileyCDA/WileyTitle/productCd-111894691X.html

import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.minecraftstuff as minecraftstuff
import time
import datetime
import math

def findPointOnCircle(cx, cy, radius, angle):
    x = cx + math.sin(math.radians(angle)) * radius
    y = cy + math.cos(math.radians(angle)) * radius
    x = int(round(x, 0))
    y = int(round(y, 0))
    return(x,y)

#create connection to minecraft
mc = minecraft.Minecraft.create()

#create minecraft drawing object
mcdrawing = minecraftstuff.MinecraftDrawing(mc)

#get the players position
pos = mc.player.getTilePos()

#create clock face above the player
clockMiddle = pos
clockMiddle.y = clockMiddle.y + 25

CLOCK_RADIUS = 20
HOUR_HAND_LENGTH = 10
MIN_HAND_LENGTH = 18
SEC_HAND_LENGTH = 20

#use mc drawing object to draw the circle of the clock face
mcdrawing.drawCircle(clockMiddle.x, clockMiddle.y, clockMiddle.z,
                     CLOCK_RADIUS, block.DIAMOND_BLOCK.id)

#loop forever
while True:
    #Find the time
    # get the time
    timeNow = datetime.datetime.now()
    # hours
    hours = timeNow.hour
    if hours >= 12:
        hours = timeNow.hour - 12
    # minutes
    minutes = timeNow.minute
    # seconds
    seconds = timeNow.second
    
    #hour hand
    # what angle would a hour hand point to
    hourHandAngle = (360 / 12) * hours
    # use findPointOnCircle function to find the angle
    hourHandX, hourHandY = findPointOnCircle(clockMiddle.x, clockMiddle.y,
                                             HOUR_HAND_LENGTH, hourHandAngle)
    # draw hour hand
    mcdrawing.drawLine(clockMiddle.x, clockMiddle.y, clockMiddle.z,
                       hourHandX, hourHandY, clockMiddle.z,
                       block.DIRT.id)

    #minute hand
    # what angle would a minute hand point to
    minHandAngle = (360 / 60) * minutes
    # use findPointOnCircle function to find the angle
    minHandX, minHandY = findPointOnCircle(clockMiddle.x, clockMiddle.y,
                                           MIN_HAND_LENGTH, minHandAngle)
    # draw minute hand
    mcdrawing.drawLine(clockMiddle.x, clockMiddle.y, clockMiddle.z - 1,
                       minHandX, minHandY, clockMiddle.z-1,
                       block.WOOD_PLANKS.id)

    #second hand
    # what angle would a second hand point to
    secHandAngle = (360 / 60) * seconds
    # use findPointOnCircle function to find the angle
    secHandX, secHandY = findPointOnCircle(clockMiddle.x, clockMiddle.y,
                                           SEC_HAND_LENGTH, secHandAngle)
    # draw second hand
    mcdrawing.drawLine(clockMiddle.x, clockMiddle.y, clockMiddle.z+1,
                       secHandX, secHandY, clockMiddle.z+1,
                       block.STONE.id)

    #wait for 1 second
    time.sleep(1)

    #clear the time by drawing over the hands with AIR
    mcdrawing.drawLine(clockMiddle.x, clockMiddle.y, clockMiddle.z,
                       hourHandX, hourHandY, clockMiddle.z,
                       block.AIR.id)
    mcdrawing.drawLine(clockMiddle.x, clockMiddle.y, clockMiddle.z-1,
                       minHandX, minHandY, clockMiddle.z-1,
                       block.AIR.id)
    mcdrawing.drawLine(clockMiddle.x, clockMiddle.y, clockMiddle.z+1,
                       secHandX, secHandY, clockMiddle.z+1,
                       block.AIR.id)
