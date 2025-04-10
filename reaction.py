# Author: Nie Yujin
# Date: 10/4/25
# A reaction game with LED
# version 3: detect the buttons

from gpiozero import LED,Button
from time import sleep
from random import uniform

# name the pin for LED and buttons
led=LED(4)
right_button=Button(15)
left_button=Button(14)

# turn on the LED
led.on()
# light up the LED for random time(5~10 secomds)
sleep(uniform(5,10))
# turn off the LED
led.off()

# a function tell which pin the button was on
def pressed(button):
    print(str(button.pin.number) + ' won the game')

# press button and call the pressed function
right_button.when_pressed=pressed
left_button.when_pressed=pressed
