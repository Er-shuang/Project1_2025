# Author: Nie Yujin
# Date: 10/4/25
# A reaction game with LED
# version 2: light up the LED for random time(5~10seconds)

from gpiozero import LED,Button
from time import sleep
from random import uniform

# name the pin
led=LED(4)
# turn on the LED
led.on()
# light up the LED for random time(5~10 secomds)
sleep(uniform(5,10))
# turn off the LED
led.off()

