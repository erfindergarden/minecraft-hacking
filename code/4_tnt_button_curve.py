#TNT BUTTON CODE

#gpio zero


from gpiozero import Button

from time import sleep

import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
import mcpi.block as block



button = Button(21)


while True:
    if button.is_pressed:
        print("Button gedrueckt")
        mc.postToChat("TNT")
        pos = mc.player.getPos() #bekomme die Spielerposition
        
        x = pos.x
        y = pos.y
        z = pos.z

        block = 46

        for i in range(1,100):
            mc.setBlock(x*i-i, y-i*i, z*i-i, block,1)
        
        sleep(0.2)

    else:
        print("druecke den button")
sleep(0.1)

       

#ENDE, veraendere den Blocktyp