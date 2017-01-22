#!/usr/bin/env python

#lass einen Text schreiben mit einem Knopfdruck


#wenn man keine pull-up oder pull-down Widerstaende verwendet ist der Status des Inputs nicht klar definiert ist
#der Input kann sich deshalb aendern lediglich, durch die statische Ladung von dir und der Button koennte willkuerlich ausgeloest werden
#wenn wir keine Widerstaende verwenden wollen, koennen wir Software im Raspberry Pi verwenden, um dem Input einen
#klaren Status zu geben

import RPi.GPIO as GPIO # importiere das RPi.GPIO Modul
from time import sleep # damit du Pausen einbauen kannst in deinen Code

GPIO.setmode(GPIO.BCM) #du kannst zwischen zwei Pin Nummerierungsmodes waehlen, hier waehlen wir BCM

GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP) #setzt GPIO24 als Input mit pull-up


try: 
    while True:  # das ist eine Endlosschleife, die mit CTRL+C stoppen kannst   
        button_state = GPIO.input(21) #setze GPIO21 gleich der Variable button_state
        if button_state == False:  #wenn Button nicht nicht gedrueckt wird
            print "Button gedrueckt"  #schreibe Button gedrueck ins Terminal
        else:
            print "Button nicht gedrueckt" #schreibe Button nicht gedrueckt ins Terminal
        sleep(0.1)

finally:
        GPIO.cleanup()  #resete die GPOs wieder
