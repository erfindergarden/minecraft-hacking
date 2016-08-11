# Adventure 7: MinecraftPyramids.py

# From the book: "Adventures in Minecraft"
# written by David Whale and Martin O'Hanlon, Wiley, 2014
# http://eu.wiley.com/WileyCDA/WileyTitle/productCd-111894691X.html

#import python modules
import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.minecraftstuff as minecraftstuff
import math

#find point on circle function
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

#pyramid variables
#the midde of the pyramid will be the position of the player
pyramidMiddle = mc.player.getTilePos()

PYRAMID_RADIUS = 20
PYRAMID_HEIGHT = 10
PYRAMID_SIDES = 4

#loop through the number of sides, each side will become a triangle
for side in range(0,PYRAMID_SIDES): 
    #find the first point of the triangle
    point1Angle = int(round((360 / PYRAMID_SIDES) * side,0))
    point1X, point1Z = findPointOnCircle(pyramidMiddle.x, pyramidMiddle.z,
                                         PYRAMID_RADIUS, point1Angle)

    #find the second point of the triangle
    point2Angle = int(round((360 / PYRAMID_SIDES) * (side + 1),0))
    point2X, point2Z = findPointOnCircle(pyramidMiddle.x, pyramidMiddle.z,
                                         PYRAMID_RADIUS, point2Angle)

    #draw the triangle
    # create the triangle points
    trianglePoints = []
    trianglePoints.append(minecraft.Vec3(point1X, pyramidMiddle.y, point1Z))
    trianglePoints.append(minecraft.Vec3(point2X, pyramidMiddle.y, point2Z))
    trianglePoints.append(minecraft.Vec3(pyramidMiddle.x,
                                         pyramidMiddle.y + PYRAMID_HEIGHT,
                                         pyramidMiddle.z))
    # draw the triangle
    mcdrawing.drawFace(trianglePoints, True, block.SANDSTONE.id)

