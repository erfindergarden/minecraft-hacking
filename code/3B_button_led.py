from gpiozero import LED, Button
from signal import pause

button = Button(25)
led = LED(24)


button.when_pressed = led.on
button.when_released = led.off

pause()