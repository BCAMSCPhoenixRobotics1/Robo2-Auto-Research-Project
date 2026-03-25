from vex import *

# Brain definition
brain : Brain = Brain()

#////////
# Left Motor
kLeftMotorPort = 11
kLeftGearing = GearSetting.RATIO_18_1 # 18-1 gear ratio
kLeftReversal = False
kLeftExtEncoder = Encoder(brain.three_wire_port.a)
#/////////

#////////
# Right Motor
kRightMotorPort : int = 1
kRightGearing = GearSetting.RATIO_18_1 # 18-1 gear ratio
kRightReversal = True
kRightExtEncoder = Encoder(brain.three_wire_port.g)
#////////

#////////
# Chassis
kWheelTravel = 10.236220472 # inches
kTrackWidth = 11.875 # inches
kWheelBase = 9.5 # inches
kExternalGearing = 1
kUnits = DistanceUnits.IN
#///////

# PID
kP  = 0.5
kI = 0.0
kD = 0.0



# set up
#////////
#print("Initalizing IMU constructor...")
imu = Inertial(Ports.PORT10)
imu.calibrate() # zeroes the IMU
wait(3000, MSEC)
#print("IMU constructor initalized and calibrated!")
#////////

def getHeading():
    currHeading = imu.heading()
    return currHeading

def setheading(targetHeading): 
    return float(targetHeading) % 360

#/////////
# Distance sensor
#print("Initalizing distance sensor...")
distSens = Distance(Ports.PORT21)
#print("Distance sensor initalized!")
#/////////

def getDist(dist):
    dist = distSens.object_distance
    return dist

def setDist(targetDist): 
    targetDist = float(targetDist)


# ////////
# Left Motor
#print("Starting left motor constructor...")
leftMotor = Motor(
    Ports.PORT1, kLeftGearing, kLeftReversal
)
leftMotor.reset_position()
#print("Left motor constructor initalized!")
# ////////

# ////////
# Right Motor
#print("Starting right motor constructor...")
rightMotor = Motor(
    Ports.PORT11, kRightGearing, kRightReversal
)
rightMotor.reset_position()
#print("Right motor constructor initalized!")
# ////////

# ////////
# left encoder
#print("Initalizing left encoder...")
leftEncoder = kLeftExtEncoder
leftEncoder.reset_position()
#print("Left encoder initalized!")

# ////////

# ////////
# right encoder
#print("Initalizing right encoder...")
rightEncoder = kRightExtEncoder
rightEncoder.reset_position()
#print("Right encoder initalized!")
# ////////

# ////////
# Chassis configuration
#print("Starting Chassis constructor...")
chassis = SmartDrive(
    leftMotor,
    rightMotor,
    imu,
    kWheelTravel,
    kTrackWidth,
    kWheelBase,
    kUnits,
    kExternalGearing,
)

#print("Chassis Constructor initalized!")
# ////////


def turnToHeading(targetHeading):

    totalError = 0
    prevError = 0
    settleTimer = 0

    while getHeading() != setheading(targetHeading):
        error = targetHeading - getHeading()
        error = (
            error + 180
        ) % 360 - 180  # gets the error between the range (-180, 180)

        totalError += error
        derivative = error - prevError
        prevError = error

        motorPower = (kP * error) + (kI * error) + (kD * derivative)
        motorPower = max(
            min(motorPower, 100), -100
        )  # Motor power is limited to between -100, 100

        leftMotor.spin(FORWARD, motorPower, PERCENT)
        rightMotor.spin(FORWARD, -motorPower, PERCENT)  # Intentionally powers the opposite direction so it turns

        if abs(error) < 1:
            settleTimer += 20
        else:
            settleTimer = 0

        if settleTimer >= 200:
            break

        wait(20, MSEC)

    chassis.stop(HOLD)

brain.screen.print("Hello V5")

while True:
    wait(5, SECONDS)
    turnToHeading(90)
    wait(5, SECONDS)
    turnToHeading(0)

        
