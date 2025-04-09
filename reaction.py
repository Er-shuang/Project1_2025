# Version 4
# Author: Xuanru Guo
# Date: 9/4/2025
# get players name using input

# import modules and libraries
from gpiozero import LED, Button
from time import sleep
from random import uniform

# set up the pin
led = LED(4)
right_button = Button(15)
left_button = Button(14)

# get the players name
left_name = input("left player name is ")
right_name = input("right player name is ")

# wait for 5 seconds and turn the LED on
led.on()
# the length of time is random
sleep(uniform(5,10))
led.off()

# tell which player press the button
def pressed(button):
	if button.pin.number == 14:
		print(left_name + ' won the game')
	else:
		print(right_name + ' won the game')
	exit()

# when the button is pressed, the funtion is called
right_button.when_pressed = pressed
left_button.when_pressed = pressed
