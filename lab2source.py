# code

pinB6 = pyb.Pin (pyb.Pin.board.PB6, pyb.Pin.IN)
pinB7 = pyb.Pin (pyb.Pin.board.PB7, pyb.Pin.IN)

timer = pyb.Timer(4, prescalar = 0, period = 0xFFFF)

ch1 = timer.channel(1, pyb.Timer.ENC_A, pin = pinB6)
ch2 = timer.channel(2, pyb.Timer.ENC_B, pin = pinB7)

while True:
    count1 = ch1.counter()
    count2 = ch2.counter()
    print(count1 + "\t" + count2)