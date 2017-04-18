import curses
from gpiozero import Robot

from time import sleep 

import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
import mcpi.block as block



robot = Robot(left=(4, 14), right=(17, 18))

actions = {
    curses.KEY_UP:    robot.forward,
    curses.KEY_DOWN:  robot.backward,
    curses.KEY_LEFT:  robot.left,
    curses.KEY_RIGHT: robot.right,
    }

def main(window):
    next_key = None
    while True:
        curses.halfdelay(1)
        if next_key is None:
            key = window.getch()
        else:
            key = next_key
            next_key = None
            sleep(0.2)
        if key != -1:
            # KEY DOWN
            curses.halfdelay(3)
            action = actions.get(key)
            if action is not None:
#                action()
                pos = mc.player.getPos()
                x = pos.x
                y = pos.y
                z = pos.z
                mc.setBlock(x,y,z block,1)

            next_key = key
            while next_key == key:
                next_key = window.getch()
            # KEY UP
            robot.stop()

curses.wrapper(main)