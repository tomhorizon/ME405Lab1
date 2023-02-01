class EncoderReader:
    def __init__ (self, pin1, pin2, position, old_count):
        self.pin1 = pyb.Pin (pin1, pyb.Pin.IN)
        self.pin2 = pyb.Pin (pin2, pyb.Pin.IN)

        self.timer = pyb.Timer(4, prescaler = 0, period = 0xFFFF)

        self.ch1 = self.timer.channel(1, pyb.Timer.ENC_AB, pin = pin1)
        self.ch2 = self.timer.channel(2, pyb.Timer.ENC_AB, pin = pin2)
        
        self.position = position
        self.old_count = old_count
        
        
    
    def read(self):
        counter = self.timer.counter()
        if counter > self.old_count + 4000:
            self.position = self.position + counter
            print('+')
        if counter < self.old_count - 4000:
            self.position = self.position - counter
            print('-')
        self.old_count = counter
        print(self.position)
        return self.position
    
            
    def zero(self):
        self.timer.counter(0)
        
if __name__ == '__main__':
     p1 = pyb.Pin.board.PB6
     p2 = pyb.Pin.board.PB7
     enc = EncoderReader(p1, p2, 0, 0)
     while (True):
         pos = enc.read()
         print(pos)
         if pos > 40000:
             print('reset')
             enc.zero()
    



