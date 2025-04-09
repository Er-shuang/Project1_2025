# Version 7
# Author: Xuanru Guo
# Date: 9/4/2025
# add scores for both players

# import modules and libraries
import sys
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

# initialize players scores
left_score = 0
right_score = 0

can_press = False

# tell which player press the button
def pressed(button):
    global can_press, left_score, right_score
    if can_press:
        if button.pin.number == 14:
            print(left_name + ' won the game')
            left_score += 1
        else:
            print(right_name + ' won the game')
            right_score += 1
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
    sys.stdout.write("\r")  
    sys.stdout.flush()  
    print("Game over")
    print(f"{left_name}'s total score: {left_score}")
    print(f"{right_name}'s total score: {right_score}")
finally:
    led.close()
    right_button.close()
    left_button.close()
    
