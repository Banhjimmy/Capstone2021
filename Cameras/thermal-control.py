import Jetson.GPIO as GPIO
import time
import os
import drone_options as drone

GPIO.setwarnings(False)

# Prime GPIO to read input.
GPIO.setmode(GPIO.BOARD)
GPIO.setup(33, GPIO.OUT)
GPIO.setup(32, GPIO.OUT)

# Instantiate PWM variables.
color_pwm = GPIO.PWM(32, 50)  # PWM3
record_pwm = GPIO.PWM(33, 50)  # PWM4

## Initialize color depending on value from text file ##
current = drone.read_file()
mode_value = drone.mode_dict.get(drone.get_mode_value(current))

if mode_value == 1:
    color_pwm.start(5)  # White Hot View
if mode_value == 2:
    color_pwm.start(7.5)  # Green Hot View
if mode_value == 3:
    color_pwm.start(10)  # Fusion View
else:
    color_pwm.start(0)  # Don't Care

# Start Recording
record_pwm.start(10)

# Record for 2 seconds
time.sleep(2)

# Stop Recording
record_pwm.ChangeDutyCycle(5)
color_pwm.stop()


# Post-data processing; cleanup
GPIO.cleanup()
