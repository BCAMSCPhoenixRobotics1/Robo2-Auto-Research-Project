from vex import *
import Constants
import Configs

# Chassis configuration
print("Starting Chassis constructor...")
Chassis : SmartDrive = SmartDrive(Configs.LeftMotor,
                                  Configs.RightMotor,
                                  Configs.IMU,
                                  Constants.kWheelTravel,
                                  Constants.kTrackWidth,
                                  Constants.kWheelBase,
                                  Constants.kUnits,
                                  Constants.kExternalGearing)

print("Chassis Constructor initalized!")
