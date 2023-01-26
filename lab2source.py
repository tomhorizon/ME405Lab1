# code

import utime
def encoder():
    pinB6 = pyb.Pin (pyb.Pin.board.PB6, pyb.Pin.IN)
    pinB7 = pyb.Pin (pyb.Pin.board.PB7, pyb.Pin.IN)

    timer = pyb.Timer(4, prescaler = 0, period = 0xFFFF)

    ch1 = timer.channel(1, pyb.Timer.ENC_AB, pin = pinB6)
    ch2 = timer.channel(2, pyb.Timer.ENC_AB, pin = pinB7)
    
    return timer

count_old = 0

def motor_control():
    pinB4 = pyb.Pin (pyb.Pin.board.PB4, pyb.Pin.OUT_PP)
    pinB5 = pyb.Pin (pyb.Pin.board.PB5, pyb.Pin.OUT_PP)
    pinA10 = pyb.Pin (pyb.Pin.board.PA10, pyb.Pin.IN, pyb.Pin.PULL_UP)

    timer3 = pyb.Timer(3, freq=20000)
    ch1 = timer3.channel (1, pyb.Timer.PWM, pin=pinB4)
    ch2 = timer3.channel (2, pyb.Timer.PWM, pin=pinB5)

    ch1.pulse_width_percent (30)
    ch2.pulse_width_percent (0)
    
    
if __name__ == "__main__":
    enc_timer = encoder()
    motor_control()
    while True:
        count = enc_timer.counter()
        if count_old != count:
           print("Count 1: " + str(count))
            
        count_old = count
