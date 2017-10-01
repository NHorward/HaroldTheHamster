import time
import RPi.GPIO as io
io.setmode(io.BCM)

wheelpin = 17

print('hi!')

io.setup(wheelpin, io.IN, pull_up_down=io.PUD_UP)

turns = 0

while True:
        if (io.input(wheelpin) == 0):
            turns += 1
            print(turns)
        
        time.sleep(0.1)

        
