from vex import *

# Brain definition
brain: Brain = Brain()

# ////////
# Left Motor
kLeftMotorPort = 11
kLeftGearing = GearSetting.RATIO_18_1  # 18-1 gear ratio
kLeftReversal = False
kLeftExtEncoder = Encoder(brain.three_wire_port.a)
# /////////

# ////////
# Right Motor
kRightMotorPort: int = 1
kRightGearing = GearSetting.RATIO_18_1  # 18-1 gear ratio
kRightReversal = True
kRightExtEncoder = Encoder(brain.three_wire_port.g)
# ////////

# ////////
# Chassis
kWheelTravel = 10.236220472  # inches
kTrackWidth = 11.875  # inches
kWheelBase = 9.5  # inches
kExternalGearing = 1
kUnits = DistanceUnits.IN
# ///////

# Turning PID
kTurnP = 1.52
kTurnI = 0.0
kTurnD = 0.6

#Driving PID
kDriveP = 0.0
kDriveI = 0.0
kDriveD = 0.0


# set up
# ////////
imu = Inertial(Ports.PORT10)
imu.calibrate()  # zeroes the IMU
wait(3000, MSEC)
# ////////


def getHeading():
    currHeading = imu.heading()
    return currHeading


def setheading(targetHeading):
    return float(targetHeading) % 360


# /////////
# Distance sensor
distSens = Distance(Ports.PORT21)
# /////////


def getDist():
    dist = distSens.object_distance
    return dist


def setDist(targetDist):
    targetDist = float(targetDist)




# ////////
# Left Motor
leftMotor = Motor(Ports.PORT1, kLeftGearing, kLeftReversal)
leftMotor.reset_position()
# ////////

# ////////
# Right Motor
rightMotor = Motor(Ports.PORT11, kRightGearing, kRightReversal)
rightMotor.reset_position()
# ////////

# ////////
# left encoder
leftEncoder = kLeftExtEncoder
leftEncoder.reset_position()

# ////////

# ////////
# right encoder
rightEncoder = kRightExtEncoder
rightEncoder.reset_position()
# ////////

# ////////
# Chassis configuration
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

        motorPower = (kTurnP * error) + (kTurnI * error) + (kTurnD * derivative)
        motorPower = max(
            min(motorPower, 100), -100
        )  # Motor power is limited to between -100, 100

        leftMotor.spin(FORWARD, motorPower, PERCENT)
        rightMotor.spin(
            FORWARD, -motorPower, PERCENT
        )  # Intentionally powers the opposite direction so it turns

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
    # wait(5, SECONDS)
    turnToHeading(90)
    # wait(5, SECONDS)
    # turnToHeading(0)
