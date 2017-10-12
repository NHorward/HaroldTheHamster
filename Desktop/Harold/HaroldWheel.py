import time
import datetime
import RPi.GPIO as io
io.setmode(io.BCM)

print("Hi, this is a tracker for Harold the Hamster")

#Setup the pins of the Raspberry
wheelpin = 17
io.setup(wheelpin, io.IN, pull_up_down=io.PUD_UP)

# Circumferance of Harold's wheel
# 18cm diameter * PI = 56.52 cm = 0.5652 m
wheelsize = 0.5652

# Number of wheel rotations
rotations = 0

# Distance covered in hamsterwheel
distance = 0

# Set the starttime to now
starttime = datetime.datetime.now()


# Function to calculate the current speed of the hamsterwheel
def calculateSpeed(spintime):
    global wheelsize
    seconds = spintime.days * 24 * 60 * 60 + spintime.seconds + spintime.microseconds / 1000000.
    return wheelsize / (seconds/60./60.)

while True:
        if (io.input(wheelpin) == 0):
            endtime = datetime.datetime.now()
            spintime = endtime - starttime
            starttime = endtime
            speed = calculateSpeed(spintime)
            distance = distance + wheelsize
            rotations += 1
            print(datetime.datetime.now, distance, speed, rotations)


        
