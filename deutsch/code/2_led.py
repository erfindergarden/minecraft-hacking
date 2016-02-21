#!/usr/bin/env python

import RPi.GPIO as GPIO 
from time import sleep
GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.OUT)

GPIO.output(17,1)
sleep(15)
GPIO.output(17,0)
GPIO.cleanup()
