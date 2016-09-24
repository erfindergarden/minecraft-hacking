
from gpiozero import LED, Button

from time import sleep


import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
mcdrawing = minecraftstuff.MinecraftDrawing(mc)
import mcpi.block as block

radius = 10
button = Button(21)
led = LED(24)

while True:
    if button.is_pressed:
        print("Button gedrueckt")
        mc.postToChat("TNT")
        led.on()
        pos = mc.player.getPos() #bekomme die Spielerposition
        
        x = pos.x
        y = pos.y
        z = pos.z

        block = 46

        mc.setBlock(x, y, z, block,1)    
        mcdrawing.drawCircle(x, y, z, radius, block, 1)
        
        sleep(0.2)

    else:
        print("druecke den button")
        led.off()
sleep(0.1)
