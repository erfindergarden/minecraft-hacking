

#http://gpiozero.readthedocs.io/en/v1.3.1/


from gpiozero import Button
from time import sleep

button = Button(21)

while True:
    if button.is_pressed:
        print("hey")
    else:
        print("hooooo")
     sleep(0.1)