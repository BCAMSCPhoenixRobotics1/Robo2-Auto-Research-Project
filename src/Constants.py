# from vex import *
# from Subsystems import Chassis

# # Brain definition

# brain : Brain = Brain()


# #////////
# # Left Motor
# kLeftMotorPort = 11
# kLeftGearing = GearSetting.RATIO_18_1 # 18-1 gear ratio
# kLeftReversal = False
# kLeftExtEncoder = Encoder(brain.three_wire_port.a)
# #/////////

# #////////
# # Right Motor
# kRightMotorPort : int = 1
# kRightGearing = GearSetting.RATIO_18_1 # 18-1 gear ratio
# kRightReversal = True
# kRightExtEncoder = Encoder(brain.three_wire_port.g)
# #////////

# #////////
# # Chassis
# kWheelTravel = 10.236220472 # inches
# kTrackWidth = 11.875 # inches
# kWheelBase = 9.5 # inches
# kExternalGearing = 1
# kUnits = DistanceUnits.IN
# #///////

# # PID
# kP  = 0.0
# kI = 0.0
# kD = 0.0

# #///////
# # misc
# kDistSensPort = 21
# kIMUPort = 10
# kRadioPort = 9
# # //////