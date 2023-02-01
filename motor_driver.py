class MotorDriver:
    def _init__(self, en_pin, in1pin, in2pin, timer):
        self.motorpin1 = pyb.Pin (pyb.Pin.board.in1pin, pyb.Pin.OUT_PP)
        self.motorpin2 = pyb.Pin (pyb.Pin.board.in2pin, pyb.Pin.OUT_PP)
        self.enablepin = pyb.Pin (pyb.Pin.board.en_pin, pyb.Pin.IN, pyb.Pin.PULL_UP)
        
        self.internaltimer = timer
        
        self.ch1 = timer.channel (1, pyb.Timer.PWM, pin=motorpin1)
        self.ch2 = timer.channel (2, pyb.Timer.PWM, pin=motorpin2)
        print("Creating a motor driver")
    
    def set_duty_cycle(self, level):
        if level >= 0:
            ch1.pulse_width_percent (level)
            ch2.pulse_width_percent (0)
        else:
            ch1.pulse_width_percent (0)
            ch2.pulse_width_percent (level)
        print(f"Setting duty cycle to {level}")
        
    