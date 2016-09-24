#TNT BUTTON CODE

import RPi.GPIO as GPIO
from time import sleep


import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
import mcpi.block as block

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(21)
    if input_state == False:
        print "Button Pressed"
        mc.postToChat("TNT")
        
        
        pos = mc.player.getPos() #bekomme die Spielerposition
        
        x = pos.x
        y = pos.y
        z = pos.z

        block = 46

        mc.setBlock(x, y, z, block,1)
        
        sleep(0.2)

#ENDE, veraendere den Blocktyp