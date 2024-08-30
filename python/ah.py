from machine import Pin, PWM
import time

# Define the PWM pin connected to the ESC signal wire
esc_pin = Pin(0)  # Replace with your actual GPIO pin
esc = PWM(esc_pin)

# Set PWM frequency to 50Hz (20ms period)
esc.freq(50)

def set_pwm_pulse_width(pulse_width_us):
    # Convert microseconds to duty cycle
    # duty = (pulse_width_us / 20000) * 65535
    duty = int((pulse_width_us / 20000) * 65535)
    esc.duty_u16(duty)

print("Calibration start!")

# Initialization: Send zero throttle
set_pwm_pulse_width(1000)  # 1 ms
time.sleep(2)  # Wait for ESC to initialize

# Calibration Procedure
# Step 1: Set full throttle
set_pwm_pulse_width(2000)  # 2 ms
time.sleep(2)  # Wait for ESC to recognize full throttle

# Step 2: Set zero throttle
set_pwm_pulse_width(1000)  # 1 ms
time.sleep(2)  # Wait for ESC to recognize zero throttle

# Calibration complete
print("ESC Calibration Complete")

# Optionally, set to zero throttle after calibration
set_pwm_pulse_width(1000)