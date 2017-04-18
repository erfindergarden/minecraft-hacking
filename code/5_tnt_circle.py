#TNT Circle


from gpiozero import Button

from time import sleep


import mcpi.minecraft as minecraft
import mcpi.minecraftstuff as minecraftstuff
mc = minecraft.Minecraft.create()
mcdrawing = minecraftstuff.MinecraftDrawing(mc)
import mcpi.block as block

radius = 10

radius = 10
button = Button(25)

while True:
    if button.is_pressed:
        print("Button gedrueckt")
        mc.postToChat("TNT")
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
sleep(0.1)
