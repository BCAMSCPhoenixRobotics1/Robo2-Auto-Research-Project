from vex import *
import Constants

# set up
#////////
print("Initalizing IMU constructor...")
imu : Inertial = Inertial(Constants.kIMUPort)
imu.calibrate() # zeroes the IMU
wait(3000, MSEC)
print("IMU constructor initalized and calibrated!")
#////////

def getHeading():
    currHeading = imu.heading()
    return currHeading

def setheading(targetHeading): 
    return float(targetHeading) % 360