from gpiozero import LED, Button
from time import sleep

button = Button(21)
led = LED(24)

while True:
    if button.is_pressed:
        print("led an")
    else:
        print("druecke den button")
     sleep(0.1)