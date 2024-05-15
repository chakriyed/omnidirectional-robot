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
SERVO_PIN = 4
TRIGGER_PIN = 27
ECHO_PIN = 17

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(MOTOR1_PIN1, GPIO.OUT)
GPIO.setup(MOTOR1_PIN2, GPIO.OUT)
GPIO.setup(MOTOR2_PIN1, GPIO.OUT)
GPIO.setup(MOTOR2_PIN2, GPIO.OUT)
GPIO.setup(MOTOR3_PIN1, GPIO.OUT)
GPIO.setup(MOTOR3_PIN2, GPIO.OUT)
GPIO.setup(SERVO_PIN, GPIO.OUT)
GPIO.setup(TRIGGER_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)

def ultrasonic_distance():
    GPIO.output(TRIGGER_PIN, GPIO.LOW)
    time.sleep(0.002)  # 2 microseconds delay
    GPIO.output(TRIGGER_PIN, GPIO.HIGH)
    time.sleep(0.000005)  # 5 microseconds delay
    GPIO.output(TRIGGER_PIN, GPIO.LOW)

    while GPIO.input(ECHO_PIN) == 0:
        signaloff = time.time()

    while GPIO.input(ECHO_PIN) == 1:
        signalon = time.time()

    timepassed = signalon - signaloff
    distance = (timepassed * 34300) / 2  # Speed of sound is approximately 343 m/s
    return distance

# Function to start camera recording
def start_recording():
    global camera
    if not camera.recording:
        camera.start_recording('test.h264')

# Function to stop camera recording
def stop_recording():
    global camera
    if camera.recording:
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

def servoultrasonic():
    # Center to left	
	for position in range(0, 180):  # Start from 125 (left) and go to 75 (right)
    		pwm.ChangeDutyCycle(position / 10.0)  # Convert position to duty cycle
        	time.sleep(0.01)	
	time.sleep(0.5)
	left = ultrasonic_distance()

     # Left to center
	for position in range(180, 0, -1):  # Start from 75 (right) and go to 125 (left)
        	pwm.ChangeDutyCycle(position / 10.0)  # Convert position to duty cycle
        	time.sleep(0.01)
	time.sleep(0.5)
	right = ultrasonic_distance()

      # Rest in center
	pwm.ChangeDutyCycle(7.5)  # Adjust duty cycle for center position (90 degrees)
	time.sleep(1)  # Rest at center position for 1 second

	if left>right:
		move_west()
	else:
		move_east()

# Create a PWM instance
pwm = GPIO.PWM(SERVO_PIN, 50)  # 50 Hz frequency

# Start PWM with center position
pwm.start(7.5)  # Adjust duty cycle for center position (90 degrees)
i=1
    
try:
    while True:
        command = raw_input("Enter command (n: north, s: south, e: east, w: west, ne : north - east, se: south-east, nw: north-west, sw: south-west, cw: clockwise rotate, aw: anti-clockwise rotate, S: stop, auto:autonomous): ")
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
	elif command == 'auto':
		di=ultrasonic_distance()	
		if di<=10:
			stop_motors()
      	   		servoultrasonic()
			continue
			
        elif command == 'S':
            stop_motors()
        else:
            print("Invalid command.")
except KeyboardInterrupt:
    print("\nStopping the robot.")
    stop_motors()
finally:
    GPIO.cleanup()
