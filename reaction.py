# Version 6
# Author: Xuanru Guo
# Date: 9/4/2025
# use loop to play game again
# use flag to stop pressing button when the LED is still on

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

can_press = False

# tell which player press the button
def pressed(button):
    global can_press
    if can_press:
        if button.pin.number == 14:
            print(left_name + ' won the game')
        else:
            print(right_name + ' won the game')
        can_press = False


# when the button is pressed, the function is called
right_button.when_pressed = pressed
left_button.when_pressed = pressed

try:
    while True:
        print("Game starts...")
        led.on()
        can_press = False
        sleep(uniform(5, 10))
        led.off()
        can_press = True
        # rest time before next game
        sleep(1.5)
except KeyboardInterrupt:
    print("Game over")
    led.close()
    right_button.close()
    left_button.close()
    
