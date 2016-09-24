# Adventure 8: WoodenHorse.py

# From the book: "Adventures in Minecraft"
# written by David Whale and Martin O'Hanlon, Wiley, 2014
# http://eu.wiley.com/WileyCDA/WileyTitle/productCd-111894691X.html

import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.minecraftstuff as minecraftstuff
import time

#create minecraft and minecraftdrawing objects
mc = minecraft.Minecraft.create()

#create the shape for our flying saucer
horseBlocks = [minecraftstuff.ShapeBlock(0,0,0,block.WOOD_PLANKS.id),
               minecraftstuff.ShapeBlock(-1,0,0,block.WOOD_PLANKS.id),
               minecraftstuff.ShapeBlock(1,0,0,block.WOOD_PLANKS.id),
               minecraftstuff.ShapeBlock(-1,-1,0,block.WOOD_PLANKS.id),
               minecraftstuff.ShapeBlock(1,-1,0,block.WOOD_PLANKS.id),
               minecraftstuff.ShapeBlock(1,1,0,block.WOOD_PLANKS.id),
               minecraftstuff.ShapeBlock(2,1,0,block.WOOD_PLANKS.id)]

#set the horses position
horsePos = mc.player.getTilePos()
horsePos.z = horsePos.z + 1
horsePos.y = horsePos.y + 1

#create the horseShape
horseShape = minecraftstuff.MinecraftShape(mc, horsePos, horseBlocks)

#make the horse move
for count in range(1,10):
    time.sleep(1)
    horseShape.moveBy(1,0,0)

horseShape.clear()
