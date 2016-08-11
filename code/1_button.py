#!/usr/bin/env python

#jetzt verbessern wir den Code indem wir pull-ups verwenden
#wenn man keine pull-up oder pull-down Widerstaende verwendet ist der Status des Inputs nicht klar definiert er floatet
#der Input kann sich deshalb aendern lediglich, durch die Statische Ladung von dir und der Button koennte willkuerlich ausgeloest werden
#wenn wir keine Widerstaende verwenden wollen, koennen wir Software im Raspberry Pi verwenden, um dem Input einen
#klaren Status zu geben

import RPi.GPIO as GPIO # importiere das RPi.GPIO Modul
from time import sleep # damit du Pausen einbauen kannst in deinen Code

GPIO.setmode(GPIO.BCM) #du kannst zwischen zwei Pin Nummerierungsmodes wählen, hier waehlen wir BCM

GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP) #setzt GPIO24 als Input mit pull-up


try: 
    while True:  # das ist eine Endlosschleife, die mit CTRL+C stoppen kannst   
        button_state = GPIO.input(24) #setze GPIO24 gleich der Variable button_state
        if button_sate == False:  #wenn Button nicht nicht gedrueckt wird 
            print "Button gedrueckt"  #schreibe Button gedrueckt


  
        else: 
            print "Button nicht gedrueckt" #wenn Button nicht gedrueckt, wenn du willst kannst due jetzt auch das ganze Else wegloeschen
        sleep(0.1)

finally:
        GPIO.cleanup()  #resete den GPIO24 wieder
