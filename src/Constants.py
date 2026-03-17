from vex import *
import Configs

# Brain definition

brain : Brain = Brain()

#///////
# Port numbers
kLeftMotorPort : int = 11
kRightMotorPort : int = 1
kDistSensPort : int = 21
kIMUPort : int = 10
kRadioPort : int = 9
# //////

#////////
# Left Motor
kLeftGearing = GearSetting.RATIO_18_1 # 18-1 gear ratio
kLeftReversal : bool = False
kLeftMotor : Motor = Configs.LeftMotor
kLeftExtEncoder = brain.three_wire_port.a
#/////////

#////////
# Right Motor
kRightGearing = GearSetting.RATIO_18_1 # 18-1 gear ratio
kRightReversal : bool = False
kRightMotor : Motor = Configs.RightMotor
kRightExtEncoder = brain.three_wire_port.g
#////////

#////////
# Chassis
kWheelTravel : float = 10.236220472 # inches
kTrackWidth : float = 11.875 # inches
kWheelBase : float = 9.5 # inches
kExternalGearing : int = 1
kUnits = DistanceUnits.IN
#///////

