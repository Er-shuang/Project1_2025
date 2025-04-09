# Version 3
# Author: Xuanru Guo
# Date: 9/4/2025
# detect the buttons

# import modules and libraries
from gpiozero import LED, Button
from time import sleep
from random import uniform

# set up the pin
led = LED(4)
right_button = Button(15)
left_button = Button(14)

# wait for 5 seconds and turn the LED on
led.on()
# the length of time is random
sleep(uniform(5,10))
led.off()

# tell which pin the button is on
def pressed(button):
	print(str(button.pin.number) + ' won the game')

# when the button is pressed, the funtion is called
right_button.when_pressed = pressed
left_button.when_pressed = pressed
