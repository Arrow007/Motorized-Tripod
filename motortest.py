from machine import Pin, PWM
import time

# Motor control pins
IN1 = Pin(18, Pin.OUT)  # IN1 for direction control
IN2 = Pin(19, Pin.OUT)  # IN2 for direction control
ENA = PWM(Pin(21))      # ENA pin for speed control (connect to a PWM-capable pin)

# Configure PWM on ENA pin
ENA.freq(1000)  # Set PWM frequency to 1 kHz (common for motor control)

def motor_forward(speed):
    """
    Move the motor forward at a given speed.
    :param speed: Speed value (0 to 65535)
    """
    IN1.on()
    IN2.off()
    ENA.duty_u16(speed)  # Set the PWM duty cycle (16-bit)

def motor_backward(speed):
    """
    Move the motor backward at a given speed.
    :param speed: Speed value (0 to 65535)
    """
    IN1.off()
    IN2.on()
    ENA.duty_u16(speed)  # Set the PWM duty cycle (16-bit)

def motor_stop():
    """
    Stop the motor.
    """
    IN1.off()
    IN2.off()
    ENA.duty_u16(0)  # Set duty cycle to 0 to stop the motor


# Example usage
motor_stop()
time.sleep(3)
motor_forward(32768)
time.sleep(3)
motor_stop()
time.sleep(3)
motor_forward(65535)
time.sleep(3)
motor_stop()





