from machine import Pin, PWM
import time

# Motor 1 Pin Mappings
IN1 = Pin(23, Pin.OUT)
IN2 = Pin(22, Pin.OUT)
EN1 = PWM(Pin(32))

# Motor 2 Pin Mappings
IN3 = Pin(33, Pin.OUT)
IN4 = Pin(25, Pin.OUT)
EN2 = PWM(Pin(26))

# Configure PWM on EN pins
EN1.freq(1000)  # Set PWM frequency to 1 kHz
EN2.freq(1000)  # Set PWM frequency to 1 kHz

def move(motor, direction, speed):
    """
    Move a motor, or ALL motors, in a particular direction at a particular speed.

    Motor:
        0: ALL Motors
        1: IN1/IN2/EN1
        2: IN3/IN4/EN2
        3: IN5/IN6/EN3

    Direction:
        0: Forward
        1: Backward
        
    Speed:
        0-100 [0-65535 (2^16)]
    """
    
    binary_speed = (int)(((speed / 100) * (2 ** 16)) - 1)
    
    if(motor == 0):
        if(direction == 0):
            IN1.on()
            IN2.off()
            IN3.on()
            IN4.off()
            
            EN1.duty_u16(binary_speed)
            EN2.duty_u16(binary_speed)
        else:
            IN1.off()
            IN2.on()
            IN3.off()
            IN4.on()
            
            EN1.duty_u16(binary_speed)
            EN2.duty_u16(binary_speed)
    
    elif(motor == 1):
        if(direction == 0):
            IN1.on()
            IN2.off()
            EN1.duty_u16(binary_speed)
        else:
            IN1.off()
            IN2.on()
            EN1.duty_u16(binary_speed)
    
    elif(motor == 2):
        if(direction == 0):
            IN3.on()
            IN4.off()
            EN2.duty_u16(binary_speed)
            
        else:
            IN3.off()
            IN4.on()
            EN2.duty_u16(binary_speed)

def stop(motor):
    """
    Stops a single motor or ALL motors.

    Motor:
        0: ALL Motors
        1: IN1/IN2
        2: IN3/IN4
        3: IN5/IN6
    """
    if(motor == 0):
        IN1.off()
        IN2.off()
        IN3.off()
        IN4.off()
        
    elif(motor == 1):
        IN1.off()
        IN2.off()
    
    elif(motor == 2):
        IN3.off()
        IN4.off()

# Example usage
stop(0)
move(1, 0, 50)
move(2, 0, 100)
time.sleep(3)
stop(2)
time.sleep(3)
stop(1)





