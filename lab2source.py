# code

import utime

pinB6 = pyb.Pin (pyb.Pin.board.PB6, pyb.Pin.IN)
pinB7 = pyb.Pin (pyb.Pin.board.PB7, pyb.Pin.IN)

timer = pyb.Timer(4, prescaler = 0, period = 0xFFFF)

ch1 = timer.channel(1, pyb.Timer.ENC_AB, pin = pinB6)
ch2 = timer.channel(2, pyb.Timer.ENC_AB, pin = pinB7)

count_old = 0

while True:
    count = timer.counter()
    if count_old != count:
       print("Count 1: " + str(count))
        
    count_old = count