from machine import Pin, PWM
from time import sleep

# Pin initialization
led = Pin("LED", Pin.OUT)
p0 = Pin(0)
p0 = PWM(p0)
p1 = Pin(1)
p1 = PWM(p1)

# 32768
# 16384
# Min = 3227


def calibrate(pin_array):
    print("Calibration started...")
    for pin in pin_array:
        pin.freq(100)
        pin.duty_u16(13107)
    sleep(5)
    for pin in pin_array:
        pin.duty_u16(6554)
    # Unplug the battery and plug it back in
    print("Calibration finished!")


""" Main """
calibrate([p0, p1])

