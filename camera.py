import RPi.GPIO as GPIO
import time
from picamera import PiCamera

#initialising camera
camera = PiCamera()

# GPIO pins for the motors
MOTOR1_PIN1 = 5
MOTOR1_PIN2 = 6
MOTOR2_PIN1 = 13
MOTOR2_PIN2 = 19
MOTOR3_PIN1 = 20
MOTOR3_PIN2 = 21

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(MOTOR1_PIN1, GPIO.OUT)
GPIO.setup(MOTOR1_PIN2, GPIO.OUT)
GPIO.setup(MOTOR2_PIN1, GPIO.OUT)
GPIO.setup(MOTOR2_PIN2, GPIO.OUT)
GPIO.setup(MOTOR3_PIN1, GPIO.OUT)
GPIO.setup(MOTOR3_PIN2, GPIO.OUT)

# Functions to start and stop camera recording
def start_recording():
    camera.start_recording('test.h264')  

def stop_recording():
    camera.stop_recording()


start_recording()


# Function to move the robot towards north
def move_north():
    GPIO.output(MOTOR1_PIN1, GPIO.LOW)
    GPIO.output(MOTOR1_PIN2, GPIO.LOW)
    GPIO.output(MOTOR2_PIN1, GPIO.LOW)
    GPIO.output(MOTOR2_PIN2, GPIO.HIGH)
    GPIO.output(MOTOR3_PIN1, GPIO.LOW)
    GPIO.output(MOTOR3_PIN2, GPIO.HIGH)

# Function to move the robot south
def move_south():
    GPIO.output(MOTOR1_PIN1, GPIO.LOW)
    GPIO.output(MOTOR1_PIN2, GPIO.LOW)
    GPIO.output(MOTOR2_PIN1, GPIO.HIGH)
    GPIO.output(MOTOR2_PIN2, GPIO.LOW)
    GPIO.output(MOTOR3_PIN1, GPIO.HIGH)
    GPIO.output(MOTOR3_PIN2, GPIO.LOW)

# Function to move the robot east
def move_east():
    turn_clock_wise()
    time.sleep(3.1)
    stop_motors()
    move_north()

# Function to move the robot west
def move_west():
    turn_anticlock_wise()
    time.sleep(3.1)
    stop_motors()
    move_north()

# Function to turn the robot north-east
def move_north_east():
    GPIO.output(MOTOR1_PIN1, GPIO.LOW)
    GPIO.output(MOTOR1_PIN2, GPIO.HIGH)
    GPIO.output(MOTOR2_PIN1, GPIO.LOW)
    GPIO.output(MOTOR2_PIN2, GPIO.HIGH)
    GPIO.output(MOTOR3_PIN1, GPIO.LOW)
    GPIO.output(MOTOR3_PIN2, GPIO.LOW)

# Function to turn the robot south-east
def move_south_east():
    GPIO.output(MOTOR1_PIN1, GPIO.LOW)
    GPIO.output(MOTOR1_PIN2, GPIO.HIGH)
    GPIO.output(MOTOR2_PIN1, GPIO.LOW)
    GPIO.output(MOTOR2_PIN2, GPIO.LOW)
    GPIO.output(MOTOR3_PIN1, GPIO.HIGH)
    GPIO.output(MOTOR3_PIN2, GPIO.LOW)

# Function to turn the robot north-west
def move_north_west():
    GPIO.output(MOTOR1_PIN1, GPIO.HIGH)
    GPIO.output(MOTOR1_PIN2, GPIO.LOW)
    GPIO.output(MOTOR2_PIN1, GPIO.LOW)
    GPIO.output(MOTOR2_PIN2, GPIO.LOW)
    GPIO.output(MOTOR3_PIN1, GPIO.LOW)
    GPIO.output(MOTOR3_PIN2, GPIO.HIGH)

# Function to turn the robot south-west
def move_south_west():
    GPIO.output(MOTOR1_PIN1, GPIO.HIGH)
    GPIO.output(MOTOR1_PIN2, GPIO.LOW)
    GPIO.output(MOTOR2_PIN1, GPIO.HIGH)
    GPIO.output(MOTOR2_PIN2, GPIO.LOW)
    GPIO.output(MOTOR3_PIN1, GPIO.LOW)
    GPIO.output(MOTOR3_PIN2, GPIO.LOW)

# Function to rotate the robot clockwise
def turn_clock_wise():
    GPIO.output(MOTOR1_PIN1, GPIO.LOW)
    GPIO.output(MOTOR1_PIN2, GPIO.HIGH)
    GPIO.output(MOTOR2_PIN1, GPIO.HIGH)
    GPIO.output(MOTOR2_PIN2, GPIO.LOW)
    GPIO.output(MOTOR3_PIN1, GPIO.LOW)
    GPIO.output(MOTOR3_PIN2, GPIO.HIGH)

# Function to rotate the robot anti-clockwise
def turn_anticlock_wise():
    GPIO.output(MOTOR1_PIN1, GPIO.HIGH)
    GPIO.output(MOTOR1_PIN2, GPIO.LOW)
    GPIO.output(MOTOR2_PIN1, GPIO.LOW)
    GPIO.output(MOTOR2_PIN2, GPIO.HIGH)
    GPIO.output(MOTOR3_PIN1, GPIO.HIGH)
    GPIO.output(MOTOR3_PIN2, GPIO.LOW)


# Function to stop all motors
def stop_motors():
    GPIO.output(MOTOR1_PIN1, GPIO.LOW)
    GPIO.output(MOTOR1_PIN2, GPIO.LOW)
    GPIO.output(MOTOR2_PIN1, GPIO.LOW)
    GPIO.output(MOTOR2_PIN2, GPIO.LOW)
    GPIO.output(MOTOR3_PIN1, GPIO.LOW)
    GPIO.output(MOTOR3_PIN2, GPIO.LOW)
    stop_recording()
    
try:
    while True:
        command = raw_input("Enter command (n: north, s: south, e: east, w: west, ne : north - east, se: south-east, nw: north-west, sw: south-west, cw: clockwise rotate, aw: anti-clockwise rotate, S: stop): ")
        if command == 'n':
            move_north()
        elif command == 's':
            move_south()
        elif command == 'e':
            move_east()
        elif command == 'w':
            move_west()
        elif command == 'ne':
            move_north_east()
        elif command == 'se':
            move_south_east()
        elif command == 'nw':
            move_north_west()
        elif command == 'sw':
            move_south_west()
        elif command == 'cw':
            turn_clock_wise()
        elif command == 'aw':
            turn_anticlock_wise()
        elif command == 'S':
            stop_motors()
        else:
            print("Invalid command.")
except KeyboardInterrupt:
    print("\nStopping the robot.")
    stop_motors()
finally:
    GPIO.cleanup()