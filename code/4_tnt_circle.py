#TNT Circle

import RPi.GPIO as GPIO
from time import sleep
import mcpi.minecraft as minecraft
import mcpi.minecraftstuff as minecraftstuff
mc = minecraft.Minecraft.create()
mcdrawing = minecraftstuff.MinecraftDrawing(mc)
import mcpi.block as block
radius = 10
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
while True:
    input_state = GPIO.input(24)
    if input_state == False:
        print "Button Pressed"
        mc.postToChat("TNT")
        pos = mc.player.getPos()
        x = pos.x
        y = pos.y
        z = pos.z
        block = 46
        mc.setBlock(x, y, z, block,1)	
        mcdrawing.drawCircle(x, y, z, radius, block, 1)
        sleep(0.2)
#mehr Aufgaben bald https://github.com/piclubmunich/tnt_button