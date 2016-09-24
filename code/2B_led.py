
#http://gpiozero.readthedocs.io/en/v1.3.1/

from gpiozero import LED
from time import sleep

led = LED(21)

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)




#oder
#while True:
#   led.blink()

#oder
#from signal import pause
#led.blink()
#pause()
