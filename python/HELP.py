from machine import Pin, PWM
from time import sleep

# Pin initialization
led = Pin("LED", Pin.OUT)
p0 = Pin(0)
p0 = PWM(p0)
p1 = Pin(1)
p1 = PWM(p1)

p0.freq(100)
p1.freq(100)
p0.duty_u16(6800) 
p1.duty_u16(6800)
print("Set to low!")
sleep(10)

max = 16384

for i in range(6800, max):
    print(i)
    sleep(0.01)
    p0.duty_u16(i)
    p1.duty_u16(i)
    
sleep(1)

for i in range(max, 6800, -1):
    print(i)
    sleep(0.01)
    p0.duty_u16(i)
    p1.duty_u16(i)