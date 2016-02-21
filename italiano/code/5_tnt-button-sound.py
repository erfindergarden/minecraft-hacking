#!/usr/bin/env python

#lade dir einen schoenen Sound herunter es sollte ein mp3 sein
# mit Internet Verbindung tippe folgendens sudo apt-get install mpg123 (wir muessen noch das Modul mpg123 installieren)
#du kannst es den song so abspielen mpg123 MySong.mp3


import RPi.GPIO as GPIO
import time
import o

import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
import mcpi.block as block


GPIO.setmode(GPIO.BCM)

GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)



while True:
    input_state = GPIO.input(24)
    if input_state == False:
        print "Button Pressed"
        pos = mc.player.getPos()
        os.system('mpg123 minecraft_short.mp3 &')
        x = pos.x
        y = pos.y
        z = pos.z

        block = 46

        mc.setBlock(x, y, z, block,1)
        time.sleep(0.2)
