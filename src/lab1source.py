"""!
@file lab1source.py
This file is Lab 1 for ME 405. The goal of the exercise was to control
a 12V DC motor with an external power supply and STM32 PWM output. The
motor has a built-in encoder which gives position feedback. STM32 timers
are used to control the encoder input and PWM output.

Once the motor was running well, the motor driver and encoder reader
were separated into two independent files as classes. This enables the
main script to be relatively brief and the motor driver or encoder reader
to be easily used in a later project.

After defining pins and starting timer channels, the encoder is cleared
and the motor is set to +50%.

An infinite loop requests the current position from the encoder, calculates a
delta from the previous reading, checks and corrects for overflow, updates
the new motor position, and delays for a small amount of time.

@author Tom Taylor
@author Jonathan Fraser
@author Dylan Weiglein

@date   2022-02-01
"""

import pyb
from encoder_reader import EncoderReader
from motor_driver import MotorDriver

# motor pins
enablePin = pyb.Pin.board.PA10
input1Pin = pyb.Pin.board.PB4
input2Pin = pyb.Pin.board.PB5
# encoder pins
encoder1Pin = pyb.Pin.board.PB6
encoder2Pin = pyb.Pin.board.PB7

# set up timers
motorTimer = pyb.Timer(3, freq=20000)
encoderTimer = pyb.Timer(4, prescaler=0, period=0xFFFF)

# initialize motor and timer
motor1 = MotorDriver(enablePin, input1Pin, input2Pin, motorTimer)
encoder1 = EncoderReader(encoder1Pin, encoder2Pin, 0, 0)

# main loop:
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
