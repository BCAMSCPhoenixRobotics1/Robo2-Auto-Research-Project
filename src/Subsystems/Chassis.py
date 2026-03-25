# from vex import *
# from Subsystems import InertialSens
# import Constants

# imu = InertialSens.imu

# kP = Constants.kP
# kI = Constants.kI
# kD = Constants.kD

# # ////////
# # Left Motor
# #print("Starting left motor constructor...")
# leftMotor = Motor(
#     Constants.kLeftMotorPort, Constants.kLeftGearing, Constants.kLeftReversal
# )
# leftMotor.reset_position()
# #print("Left motor constructor initalized!")
# # ////////

# # ////////
# # Right Motor
# #print("Starting right motor constructor...")
# rightMotor = Motor(
#     Constants.kRightMotorPort, Constants.kRightGearing, Constants.kRightReversal
# )
# rightMotor.reset_position()
# #print("Right motor constructor initalized!")
# # ////////

# # ////////
# # left encoder
# #print("Initalizing left encoder...")
# leftEncoder = Constants.kLeftExtEncoder
# leftEncoder.reset_position()
# #print("Left encoder initalized!")

# # ////////

# # ////////
# # right encoder
# #print("Initalizing right encoder...")
# rightEncoder = Constants.kRightExtEncoder
# rightEncoder.reset_position()
# #print("Right encoder initalized!")
# # ////////

# # ////////
# # Chassis configuration
# #print("Starting Chassis constructor...")
# chassis = SmartDrive(
#     leftMotor,
#     rightMotor,
#     imu,
#     Constants.kWheelTravel,
#     Constants.kTrackWidth,
#     Constants.kWheelBase,
#     Constants.kUnits,
#     Constants.kExternalGearing,
# )

# #print("Chassis Constructor initalized!")
# # ////////


# def turnToHeading(targetHeading):

#     totalError = 0
#     prevError = 0
#     settleTimer = 0

#     while InertialSens.getHeading() != InertialSens.setheading(targetHeading):
#         error = targetHeading - InertialSens.getHeading()
#         error = (
#             error + 180
#         ) % 360 - 180  # gets the error between the range (-180, 180)

#         totalError += error
#         derivative = error - prevError
#         prevError = error

#         motorPower = (kP * error) + (kI * error) + (kD * derivative)
#         motorPower = max(
#             min(motorPower, 100), -100
#         )  # Motor power is limited to between -100, 100

#         leftMotor.spin(FORWARD, motorPower, PERCENT)
#         rightMotor.spin(FORWARD, -motorPower, PERCENT)  # Intentionally turns the opposite direction so it turns

#         if abs(error) < 1:
#             settleTimer += 20
#         else:
#             settleTimer = 0

#         if settleTimer >= 200:
#             break

#         wait(20, MSEC)

#     chassis.stop(HOLD)
