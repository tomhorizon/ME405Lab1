import time
from motor_driver import MotorDriver
from encoder_reader import EncoderReader

# motor pins
enablePin = PB4
input1Pin = PB5
input2Pin = PA10
# encoder pins
encoder1Pin = PB6
encoder2Pin = PB7

# set up timers
motorTimer = pyb.Timer(3, freq=20000)
encoderTimer = pyb.Timer(4, prescaler = 0, period = 0xFFFF)

#initialize motor and timer
motor1 = MotorDriver(enablePin, input1Pin, input2Pin, motorTimer)
encoder1 = EncoderReader(encoder1Pin, encoder2Pin, encoderTimer)

#main loop:
encoder1.zero()
count_previous = 0
delta = 0
position_old

motor1.set_duty_cycle(50)

while True:
    count = encoder1.read()
    delta = count - count_previous
    if abs(delta) > 30000:
        delta = delta % 65535
    position = position_old + delta
    count_previous = count
    delay(1)
    
