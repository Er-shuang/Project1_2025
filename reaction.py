# Author: Nie Yujin
# Date: 11/4/25
# A reaction game with LED
# version 5: record the time that player pressed button after LED turned off

from gpiozero import LED,Button
from time import sleep,time
from random import uniform

# name the pin for LED and buttons
led=LED(4)
right_button=Button(15)
left_button=Button(14)

# time of LED turn off
off_time=0

# input the name of player
left_name=input('left player name is ')
right_name=input('right player name is ')

# turn on the LED
led.on()
# light up the LED for random time(5~10 secomds)
sleep(uniform(5,10))
# turn off the LED
led.off()
off_time=time()

# a function tell which pin the button was on, and which player win the game
def pressed(button):
    if button.pin.number==14:
        # reaction time
        reaction_time=time()-off_time
        print(f"{left_name} won the game. Reaction time is {reaction_time}s")
    else:
        # reaction time
        reaction_time=time()-off_time
        print(f"{right_name} won the game. Reaction time is {reaction_time}s")
    exit()

# press button and call the pressed function
right_button.when_pressed=pressed
left_button.when_pressed=pressed
