class Vehicle:
    def __init__(self, name, thruster, sensor, birth, hydrophones):
        self.name=name
        self.thruster=thruster
        self.sensor=sensor
        self.birth=birth
        self.hydrophones=hydrophones

    def infoAUV(self):
        ''' this will define my row(the auv info) for the table '''
        return [self.name, self.thruster, self.sensor, self.birth,
        self.hydrophones]

    def showThisAUV(self):
        return [self.name, self.thruster, self.sensor, self.birth, self.hydrophones]
    
    def birthInfo(self):
        return [self.birth,[self.name, self.thruster, self.sensor, self.birth,
        self.hydrophones]]
    
    def sensorsAUV(self):
        return [self.name, self.sensor]

# robots
v1 = Vehicle("Lua",8 ,["SENSOR X1", "SENSOR X2"], 2022,4)
v2 = Vehicle("BrHUE",6,["SENSOR Y1", "SENSOR Y2"], 2021,4)

AUVs = [v1,v2]
numAUVs= range(0,len(AUVs))

def tableOfAUVs():
    ''' return a table with all auvs '''
    AUVsTable=[]
    for i in numAUVs:
        AUVsTable.append(AUVs[i].infoAUV())
    return AUVsTable
print(tableOfAUVs())
def anAUV(x=0):
    ''' default argument to avoid errors '''
    if x < len(AUVs):
        return AUVs[x].showThisAUV()
    else:
        return str.format('Invalid index. The max. index that you can choose is {}', len(AUVs) - 1)
print(anAUV())
def newer():
    ''' adds all years to the list, sorts the list, deletes the year that was used only for sorting, and reverses the order of the list '''
    sortedBirth=[]
    for i in numAUVs:
        sortedBirth.append(AUVs[i].birthInfo())
    sortedBirth.sort()
    for i in numAUVs:
        del sortedBirth[i][0]
    return sortedBirth[::-1]
print(newer())
def AUVsensor():
    ''' returns the robot's name and sensors '''
    sensors=[]
    for i in numAUVs:
        sensors.append(AUVs[i].sensorsAUV())
    return sensors
print(AUVsensor())
