from machine import Pin, PWM
from time import sleep

# Pin initialization
led = Pin("LED", Pin.OUT)
p0 = Pin(0)
p0 = PWM(p0)
p1 = Pin(1)
p1 = PWM(p1)
p16 = Pin(16, Pin.IN, Pin.PULL_DOWN)
p17 = Pin(17, Pin.IN, Pin.PULL_DOWN)

freq = 50

p0.freq(freq)
p1.freq(freq)

# max = 32768
# min = 3227
# programming mode at 8192
    
# Interrupt handling
def high(pin):
    print("High")
    p0.duty_u16(8000)
    p1.duty_u16(8000)
def low(pin):
    print("Low")
    p0.duty_u16(3227)
    p1.duty_u16(3227)
    
sleep(5)


p16.irq(trigger=Pin.IRQ_RISING, handler=high)
p17.irq(trigger=Pin.IRQ_RISING, handler=low)

while True:
    print("Hallo!")
    sleep(5)