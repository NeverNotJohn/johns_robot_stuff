from machine import Pin, PWM
from time import sleep

# Pin initialization
led = Pin("LED", Pin.OUT)
p0 = Pin(0)
p0 = PWM(p0)
p1 = Pin(1)
p1 = PWM(p1)

p0.freq(70)
p0.duty_u16(3227) # 50% duty cycle... max is 65535
sleep(5)

max = 6000

for i in range(5000, max):
    print(i)
    sleep(0.01)
    p0.duty_u16(i)
    p1.duty_u16(i)
    
sleep(1)

for i in range(max, 5000, -1):
    print(i)
    sleep(0.01)
    p0.duty_u16(i)
    p1.duty_u16(i)