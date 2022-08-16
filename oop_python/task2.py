import numpy as np
from tabulate import tabulate as tab

class Vehicle:
    def __init__(self, name, thruster, sensor, birth, hydrophones):
        self.name=name
        self.thruster=thruster
        self.sensor=sensor
        self.birth=birth
        self.hydrophones=hydrophones

    def infoAUV(self):
        ''' this will define my row(the auv info) for the table '''
        return np.array([self.name, self.thruster, self.sensor, self.birth,
        self.hydrophones])
    
    def birthInfo(self):
        return self.birth 
    
    def sensorsAUV(self):
        return np.array([self.name, self.sensor])

v1 = Vehicle("Lua",8 ,"SENSOR X1, SENSOR X2", 2022,4)
v2 = Vehicle("BrHUE",6,"SENSOR Y1, SENSOR Y2", 2021,4)

AUVs1 = [v1,v2]

AUVs = [v1.infoAUV(), v2.infoAUV()]

def tableOfAUVs():
    ''' return a table with all auvs '''
    tHeader = ["Name", "Thruster", "Sensors", "Birth", "Hydrophones"]
    return tab(AUVs, headers=tHeader, tablefmt="fancy_grid")

def anAUV():
    ''' return a row table of an auv ''' 
    tHeader = ["Name", "Sensor", "Thruster", "Birth", "Hydrophones"]
    return tab([v2.infoAUV()], headers=tHeader, tablefmt="fancy_grid")

def newer():
    tHeader = ["Name", "Sensor", "Thruster", "Birth", "Hydrophones"]
    l =[]
    sortedB=[]
    for i in range(0, len(AUVs1)):
        l.append(str(AUVs1[i].birthInfo()))
    for i in range(0, len(l)):
        if max(l) in AUVs1[i].infoAUV():
           sortedB.append(AUVs1[i].infoAUV())
           l.remove(max(l))
    if len(l) > 0:
        for i in range(0,len(l)):
            if max(l) in AUVs1[i].infoAUV():
                sortedB.append(AUVs1[i].infoAUV())
                l.remove(max(l))
    return tab(sortedB, headers=tHeader, tablefmt="fancy_grid") 

def AUVsensor():
    sensors=[]
    tHeader=["Name", "Sensor"]
    for i in range(0,len(AUVs1)):
        sensors.append(AUVs1[i].sensorsAUV())
    return tab(sensors,headers=tHeader, tablefmt="fancy_grid")
