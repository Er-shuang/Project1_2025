# Author: Nie Yujin
# Date: 10/4/25
# A reaction game with LED
# version 4: get player names

from gpiozero import LED,Button
from time import sleep
from random import uniform

# name the pin for LED and buttons
led=LED(4)
right_button=Button(15)
left_button=Button(14)

# input the name of player
left_name=input('left player name is ')
right_name=input('right player name is ')

# turn on the LED
led.on()
# light up the LED for random time(5~10 secomds)
sleep(uniform(5,10))
# turn off the LED
led.off()

# a function tell which pin the button was on, and which player win the game
def pressed(button):
    if button.pin.number==14:
        print(left_name+' won the game')
    else:
        print(right_name+' won the game')
    exit()

# press button and call the pressed function
right_button.when_pressed=pressed
left_button.when_pressed=pressed
