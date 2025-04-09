# Version 1
# Author: Xuanru Guo

# import modules and libraries
from gpiozero import LED, Button
from time import sleep

# set up the pin
led = LED(4)

# wait for 5 seconds and turn the LED on
led.on()
sleep(5)
led.off()


