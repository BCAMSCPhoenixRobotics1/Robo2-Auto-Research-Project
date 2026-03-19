from vex import *
from Subsystems import Chassis

# Brain definition

brain : Brain = Brain()


#////////
# Left Motor
kLeftMotorPort : int = 11
kLeftGearing = GearSetting.RATIO_18_1 # 18-1 gear ratio
kLeftReversal : bool = False
kLeftExtEncoder = Encoder(brain.three_wire_port.a)
#/////////

#////////
# Right Motor
kRightMotorPort : int = 1
kRightGearing = GearSetting.RATIO_18_1 # 18-1 gear ratio
kRightReversal : bool = False
kRightExtEncoder = Encoder(brain.three_wire_port.g)
#////////

#////////
# Chassis
kWheelTravel : float = 10.236220472 # inches
kTrackWidth : float = 11.875 # inches
kWheelBase : float = 9.5 # inches
kExternalGearing : int = 1
kUnits = DistanceUnits.IN
#///////

# PID
kP : float = 0.0
kI : float = 0.0
kD : float = 0.0

#///////
# misc
kDistSensPort : int = 21
kIMUPort : int = 10
kRadioPort : int = 9
# //////