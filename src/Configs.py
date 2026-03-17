from vex import *
import Constants

#////////
#Left Motor
print("Starting left motor constructor...")
LeftMotor : Motor = Motor(Constants.kLeftMotorPort,
                          Constants.kLeftGearing,
                          Constants.kLeftReversal)
print("Left motor constructor initalized!")
#////////

#////////
#Right Motor
print("Starting right motor constructor...")
RightMotor : Motor = Motor(Constants.kRightMotorPort,
                           Constants.kRightGearing,
                           Constants.kRightReversal)
print("Right motor constructor initalized!")
#////////

#////////
print("Initalizing IMU constructor...")
IMU : Inertial = Inertial(Constants.kIMUPort)
print("IMU constructor initalized!")
#////////

#////////
#left encoder
print("Initalizing left encoder...")
leftEncoder = Constants.kLeftExtEncoder
print("Left encoder initalized!")
#////////

#////////
#right encoder
print("Initalizing right encoder...")
rightEncoder = Constants.kRightExtEncoder
print("Right encoder initalized!")
#////////