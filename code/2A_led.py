
from gpiozero import LED
from time import sleep

led = LED(21)

while True:
    led.on()
    print ("blink")
    sleep(1)
    led.off()
    sleep(1)




#oder
#while True:
#   led.blink()
#   print "blink"
#   sleep(2)

#oder
#from signal import pause
#led.blink()
#pause()
