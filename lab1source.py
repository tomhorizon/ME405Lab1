import time
import pyb
from motor_driver import MotorDriver
from encoder_reader import EncoderReader

# motor pins
enablePin = pyb.Pin.board.PA10
input1Pin = pyb.Pin.board.PB4
input2Pin = pyb.Pin.board.PB5
# encoder pins
encoder1Pin = pyb.Pin.board.PB6
encoder2Pin = pyb.Pin.board.PB7

# set up timers
motorTimer = pyb.Timer(3, freq=20000)
encoderTimer = pyb.Timer(4, prescaler = 0, period = 0xFFFF)

#initialize motor and timer
motor1 = MotorDriver(enablePin, input1Pin, input2Pin, motorTimer)
encoder1 = EncoderReader(encoder1Pin, encoder2Pin, 0, 0)

#main loop:
encoder1.zero()
count_previous = 0
delta = 0
position_old = 0

motor1.set_duty_cycle(50)

while True:
    count = encoder1.read()
    delta = count - count_previous
    if abs(delta) > 30000:
        delta = delta % 65535
    position = position_old + delta
    count_previous = count
    pyb.delay(1)
    
