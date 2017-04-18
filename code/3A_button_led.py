from gpiozero import LED, Button
from time import sleep

button = Button(21)
led = LED(24)

while True:
    if button.is_pressed:
        print("led an")
        led.on()
    else:
        print("druecke den button")
        led.off()
sleep(0.1)