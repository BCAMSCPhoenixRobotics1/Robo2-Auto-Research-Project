from vex import *
import Constants

#/////////
# Distance sensor
print("Initalizing distance sensor...")
distSens : Distance = Distance(Constants.kDistSensPort)
print("Distance sensor initalized!")
#/////////

def getDist(dist):
    dist = distSens.object_distance
    return dist

def setDist(targetDist): 
    targetDist = float(targetDist)