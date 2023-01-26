class MotorDriver:
    def _init__(self, en_pin, in1pin, in2pin, timer):
        in1pin = pyb.Pin (pyb.Pin.board.PB4, pyb.Pin.OUT_PP)
        in2pin = pyb.Pin (pyb.Pin.board.PB5, pyb.Pin.OUT_PP)
        en_pin = pyb.Pin (pyb.Pin.board.PA10, pyb.Pin.IN, pyb.Pin.PULL_UP)
        
        timer3 = pyb.Timer(3, freq=20000)
        
        ch1 = timer3.channel (1, pyb.Timer.PWM, pin=pinB4)
        ch2 = timer3.channel (2, pyb.Timer.PWM, pin=pinB5)
        print("Creating a motor driver")
    
    def set_duty_cycle(self, level):
        if level >= 0:
            ch1.pulse_width_percent (level)
            ch2.pulse_width_percent (0)
        else:
            ch1.pulse_width_percent (0)
            ch2.pulse_width_percent (level)
        print(f"Setting duty cycle to {level}")
        
    