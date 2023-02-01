class MotorDriver:
    def __init__(self, en_pin, in1pin, in2pin, timer):
        motorpin1 = pyb.Pin (in1pin, pyb.Pin.OUT_PP)
        motorpin2 = pyb.Pin (in2pin, pyb.Pin.OUT_PP)
        enablepin = pyb.Pin (en_pin, pyb.Pin.IN, pyb.Pin.PULL_UP)
        
        self.internaltimer = timer
        
        self.ch1 = timer.channel (1, pyb.Timer.PWM, pin=motorpin1)
        self.ch2 = timer.channel (2, pyb.Timer.PWM, pin=motorpin2)
        print("Creating a motor driver")
    
    def set_duty_cycle(self, level):
        if level >= 0:
            self.ch1.pulse_width_percent (level)
            self.ch2.pulse_width_percent (0)
        else:
            self.ch1.pulse_width_percent (0)
            self.ch2.pulse_width_percent (level)
        print(f"Setting duty cycle to {level}")
        
# if __name__ == '__main__':
#     import time
#   
#     enablePin = pyb.Pin.board.PA10
#     input1Pin = pyb.Pin.board.PB4
#     input2Pin = pyb.Pin.board.PB5
#     motorTimer = pyb.Timer(3, freq=20000)
#     
#     motor1 = MotorDriver(enablePin, input1Pin, input2Pin, motorTimer)
#     motor1.set_duty_cycle(50)

    